from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    m_items: List[T]
    m_subscribers: List[Callable[["T"], None]]

    def __init__(self):
        self.m_items = []
        self.m_subscribers = []

    def enqueue(self, item: T) -> None:
        self.m_items.append(item)

        for subscriber in self.m_subscribers:
            subscriber(self.dequeue())

    def dequeue(self) -> T:
        item = self.m_items[0]
        self.m_items = self.m_items[1:]

        return item

    def subscribe(self, subscriber: Callable[["T"], None]):
        self.m_subscribers.append(subscriber)
