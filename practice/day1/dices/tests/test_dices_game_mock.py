from mockito import mock, times, verify, when, ANY

from app import *
from tests.test_dice_game import player_has_exactly_chips


# test for behavior 
def test_game_calls_win_for_all_winners_and_loosers_loose(monkeypatch):
    game = RollDiceGame()
    when(Dice).roll().thenReturn(5)
    winner_1 = mocked_player_with_bet(game, 5)
    winner_2 = mocked_player_with_bet(game, 5)
    looser_1 = mocked_player_with_bet(game, 1)
    looser_2 = mocked_player_with_bet(game, 2)

    game.play()

    verify(winner_1, times(1)).win(Chip(18))
    verify(winner_2, times(1)).win(Chip(18))
    verify(looser_1, times(0)).win(ANY)
    verify(looser_2, times(0)).win(ANY)


### private functions to set up test data

def mocked_player() -> player:
    player = mock(Player)
    when(player).has(ANY).thenReturn(True)
    when(player).join(ANY).doNothing()
    when(player).take(ANY).doNothing()
    when(player).win(ANY).doNothing()
    return player


def mocked_player_with_bet(game:RollDiceGame, bet_score: int) -> player:
    player = mocked_player()
    player.join(game)
    game.bet(player, Bet(Chip(3), bet_score))
    return player
