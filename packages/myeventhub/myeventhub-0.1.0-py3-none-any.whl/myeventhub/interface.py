from abc import ABC, abstractmethod


class IProducer(ABC):
    @abstractmethod
    async def send(self, event: str, event_key: str = None):
        raise NotImplementedError


class IConsumer(ABC):
    @abstractmethod
    async def receive(self) -> None:
        raise NotImplementedError
