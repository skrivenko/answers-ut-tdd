from app.game import Game
from app.cell import Cell


class CreateGame:
    _game: Game

    def __init__(self):
        self._cells = []

    def with_cell(self, x, y):
        self._cells.append(Cell(x, y))
        return self

    def please(self):
        return Game(self._cells)