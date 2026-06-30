from app import *
from tests.test_dice_game import game_with_player, player_has_exactly_chips, player_with_five_chips


def test_player_looses_when_he_played_non_winning_score(monkeypatch):
    player = player_with_five_chips()
    game = game_with_player(player)
    game.bet(player, Bet(Chip(3), 2))
    monkeypatch.setattr(Dice, "roll", staticmethod(lambda: 5))

    game.play()

    assert player_has_exactly_chips(player, Chip(2))


def test_player_wins_when_he_played_winning_score(monkeypatch):
    player = player_with_five_chips()
    game = game_with_player(player)
    game.bet(player, Bet(Chip(3), 5))
    monkeypatch.setattr(Dice, "roll", staticmethod(lambda: 5))

    game.play()

    assert player_has_exactly_chips(player, Chip(2 + 3*6))


/// TODO: реализация приват функций
