import time, random

from impl.queues import GameQueue
from impl.providers import GameProvider
from impl.consumers import GameConsumer
from impl.generators import GameGenerator

from concurrency.decorators import thread


@thread
def main():
    queue = GameQueue()
    consumer = GameConsumer()
    generator = GameGenerator()
    provider = GameProvider(queue)

    provider.subscribe(consumer)

    for game in generator.generate():
        queue.enqueue(game)
        time.sleep(random.randint(10, 30))


if __name__ == "__main__":
    CONCURRENT_GAMES = 16

    for _ in range(CONCURRENT_GAMES):
        main()
