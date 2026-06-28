import pytest
from app.game import Game


def test_empty_game_is_empty_in_next_generation():
    game = Game([])
    game.next_generation()
    assert game == Game([])
