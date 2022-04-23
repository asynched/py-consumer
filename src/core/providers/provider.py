from typing import Protocol, TypeVar, Generic

from core.consumers import Consumer
from core.queues import Queue

T = TypeVar("T")


class Provider(Protocol, Generic[T]):
    def __init__(self, queue: Queue[T]):
        ...

    def subscribe(self, consumer: Consumer[T]):
        ...
