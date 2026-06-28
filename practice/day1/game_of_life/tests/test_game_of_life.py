import pytest
from app.game import Game
from tests.create_builder import Create


def test_empty_game_is_empty_in_next_generation():
    game = Game([])
    game.next_generation()
    assert game == Game([])


def test_lonely_cell_dies():
    game = Create.game().with_cell(1,1).please()
    game.next_generation()
    assert game == Game([])


def test_two_neighbours_cell_survives():
    game = Create.game().with_cell(1,1).with_cell(2,2).with_cell(3,3).please()
    game.next_generation()
    assert game ==  Create.game().with_cell(2,2).please()
