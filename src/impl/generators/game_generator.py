from random import randint, choice

from impl.models import Game
from impl.utils import country_names


class GameGenerator:
    m_game: Game

    def __init__(self):
        self.m_game = Game(player1=choice(country_names), player2=choice(country_names))

    def generate(self):
        while True:
            if randint(0, 1) == 1:
                self.m_game.score.score_player1 += 1
            else:
                self.m_game.score.score_player2 += 1

            yield self.m_game
