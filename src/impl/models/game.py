from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Score:
    score_player1: int = 0
    score_player2: int = 0


@dataclass
class Game:
    player1: str
    player2: str
    score: Score = field(default_factory=Score)
    id: str = field(default_factory=uuid4)
