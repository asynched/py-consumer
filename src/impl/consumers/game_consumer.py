from core.consumers import Consumer
from impl.models import Game
from impl.utils.logger import Logger

LOGGING_FORMAT = ""


class GameConsumer(Consumer[Game]):
    m_logger: Logger

    def __init__(self):
        self.m_logger = Logger("GAME CONSUMER")

    def notify(self, message: Game):
        self.m_logger.info(message.__dict__)
