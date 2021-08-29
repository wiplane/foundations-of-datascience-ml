import draw

from draw import draw_board as db
from draw import initalize_game
import players


def play_game():
    board = db()
    game = initialize_game()
    pass


def create_result():
    result = players()
    if draw.P1.if_check_mate():
        endgame()
        return "P2 Wins"
    elif draw.p2.if_check_mate():
        endgame()
        return "P1 Wins"

    ...

