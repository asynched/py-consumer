from typing import List
from core.providers import Provider
from core.consumers import Consumer
from core.queues import Queue

from impl.models import Game


class GameProvider(Provider[Game]):
    m_queue: Queue[Game]
    m_consumers: List[Consumer[Game]]

    def __init__(self, queue: Queue[Game]):
        self.m_queue = queue
        self.m_consumers = []

        self.m_queue.subscribe(self.notify)

    def notify(self, message: Game):
        for consumer in self.m_consumers:
            consumer.notify(message)

    def subscribe(self, consumer: Consumer[Game]):
        self.m_consumers.append(consumer)
