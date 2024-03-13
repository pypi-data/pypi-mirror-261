import logging
from abc import abstractmethod
from typing import Optional

from azure.eventhub import EventData
from azure.eventhub.aio import (
    EventHubProducerClient,
    EventHubConsumerClient,
    PartitionContext,
)
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore

from myeventhub.interface import IProducer, IConsumer

logger = logging.getLogger(__name__)


class BaseEventHubProducer(IProducer):
    def __init__(self, connection_string: str, event_hub_name: str):
        self._connection_string = connection_string
        self._event_hub_name = event_hub_name
        self._event_hub_producer_client = EventHubProducerClient.from_connection_string(
            conn_str=connection_string,
            eventhub_name=event_hub_name,
            on_error=self.on_error,
            on_success=self.on_success,
        )

    async def start(self):
        partition_ids = await self._event_hub_producer_client.get_partition_ids()
        logger.info(
            f"Successfully start {self.__class__.__name__}. Number of Partitions: {len(partition_ids)}"
        )

    async def stop(self):
        await self._event_hub_producer_client.close()
        logger.info(f"Successfully stop {self.__class__.__name__}")

    async def on_success(self, events, partition_id):
        logger.debug(
            f"Successfully sent events={events} to partition_id={partition_id}",
            extra={
                "messaging.event_type": "produce_message",
                "messaging.event_hub_name": self._event_hub_name,
                "messaging.partition_id": partition_id,
                "messaging.status": "success",
                "messaging.event_count": len(events),
            },
        )

    async def on_error(self, events, partition_id, exc):
        logger.error(
            f"Error when sending events={events} to partition_id={partition_id}. Exception: {exc}",
            extra={
                "messaging.event_type": "produce_message",
                "messaging.event_hub_name": self._event_hub_name,
                "messaging.partition_id": partition_id,
                "messaging.status": "failure",
                "messaging.event_count": len(events),
                "error.message": str(exc),
                "error.stack": exc.__traceback__,
                "error.kind": type(exc).__qualname__,
            },
        )

    async def send(self, event: str, event_key: str = None):
        """
        Send an event to the event hub
        :param event:
        :param event_key:
        :return:
        """

        async with self._event_hub_producer_client as client:
            await client.send_event(
                partition_key=event_key, event_data=EventData(event)
            )


class BaseEventHubConsumer(IConsumer):
    _EARLIEST_MODE = "-1"
    _LATEST_MODE = "@latest"

    def __init__(
        self,
        config: dict,
        consumer_config: dict,
    ):
        self._event_hub_name = consumer_config["topic"]
        self._consumer_group = consumer_config["group"]
        self._starting_position = (
            self._EARLIEST_MODE
            if consumer_config["start_from_beginning"]
            else self._LATEST_MODE
        )
        self._max_wait_time_seconds = consumer_config["max_wait_time_seconds"]
        self._event_hub_consumer_client = EventHubConsumerClient.from_connection_string(
            conn_str=config["connection_string"],
            consumer_group=self._consumer_group,
            eventhub_name=self._event_hub_name,
            checkpoint_store=BlobCheckpointStore.from_connection_string(
                conn_str=config["checkpoint_store_connection_string"],
                container_name=consumer_config["checkpoint_store_container_name"],
            ),
        )
        self.__consume_task = None

    @abstractmethod
    async def on_event(
        self, partition_context: PartitionContext, event: Optional[EventData]
    ):
        raise NotImplementedError

    async def on_error(self, partition_context: PartitionContext, exc: Exception):
        logger.error(
            f"Error when receiving event from event_hub_name={self._event_hub_name}. Exception: {exc}",
            extra={
                "messaging.event_type": "consume_message",
                "messaging.event_hub_name": self._event_hub_name,
                "messaging.partition_id": partition_context.partition_id,
                "messaging.status": "failure",
                "messaging.consumer_group": self._consumer_group,
                "error.message": str(exc),
                "error.stack": exc.__traceback__,
                "error.kind": type(exc).__qualname__,
            },
        )

    async def on_partition_initialize(self, partition_context):
        logger.info(
            f"Partition: {partition_context.partition_id} has been initialized.",
            extra={
                "messaging.event_type": "partition_initialize",
                "messaging.event_hub_name": self._event_hub_name,
                "messaging.consumer_group": self._consumer_group,
                "messaging.partition_id": partition_context.partition_id,
            },
        )

    async def on_partition_close(self, partition_context, reason):
        logger.info(
            f"Partition: {partition_context.partition_id} has been closed, reason for closing: {reason}",
            extra={
                "messaging.event_type": "partition_close",
                "messaging.event_hub_name": self._event_hub_name,
                "messaging.consumer_group": self._consumer_group,
                "messaging.partition_id": partition_context.partition_id,
            },
        )

    async def start(self):
        import asyncio

        logger.info(f"Running {self.__class__.__name__}...")
        self.__consume_task = asyncio.ensure_future(self.receive())

    async def stop(self):
        logger.info(f"Stopping {self.__class__.__name__}...")
        self.__consume_task.cancel()

    async def receive(self):
        async with self._event_hub_consumer_client as client:
            await client.receive(
                on_event=self.on_event,
                on_error=self.on_error,
                on_partition_initialize=self.on_partition_initialize,
                on_partition_close=self.on_partition_close,
                starting_position=self._starting_position,
                max_wait_time=self._max_wait_time_seconds,
            )
