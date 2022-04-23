from typing import Generic, TypeVar, Protocol

T = TypeVar("T")


class Consumer(Protocol, Generic[T]):
    def __init__(self):
        ...

    def notify(self, message: T):
        ...
