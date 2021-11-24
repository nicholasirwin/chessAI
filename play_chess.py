import random, sys
from ChessGame import ChessGame
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from HumanPlayer import HumanPlayer
from RandomAI import RandomAI

# python3 play_chess.py player1 depth1 player2 depth2
if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Input: python3 [player1] [depth1] [player2] [depth2]")
        sys.exit()

    isAI1 = True
    if int(sys.argv[2]) == -1:
        isAI1 = False
    elif int(sys.argv[2]) > 5 or int(sys.argv[2]) < 1:
        print("Usage: depth1 must be between 1 and 5 (inclusive)")
        sys.exit()

    isAI2 = True
    if int(sys.argv[4]) == -1:
        isAI2 = False
    elif int(sys.argv[4]) > 5 or int(sys.argv[4]) < 1:
        print("Usage: depth2 must be between 1 and 5 (inclusive)")
        sys.exit()

    if str(sys.argv[1]).lower() == "human" and not isAI1:
        player1 = HumanPlayer()
    elif str(sys.argv[1]).lower() == "random" and not isAI1:
        player1 = RandomAI()
    elif str(sys.argv[1]).lower() == "minimax" and isAI1:
        player1 = MinimaxAI(int(sys.argv[2]), True)
    elif str(sys.argv[1]).lower() == "alphabeta" and isAI1:
        player1 = AlphaBetaAI(int(sys.argv[2]), True)
    else:
        print("Usage: 'human' and 'random' with depth -1, 'minimax' and 'alphabeta' with 0 < depth < 6")
        sys.exit()

    if str(sys.argv[3]).lower() == "human" and not isAI2:
        player2 = HumanPlayer()
    elif str(sys.argv[3]).lower() == "random" and not isAI2:
        player2 = RandomAI()
    elif str(sys.argv[3]).lower() == "minimax" and isAI2:
        player2 = MinimaxAI(int(sys.argv[4]), False)
    elif str(sys.argv[3]).lower() == "alphabeta" and isAI2:
        player2 = AlphaBetaAI(int(sys.argv[4]), False)
    else:
        print("Usage: 'human' and 'random' with depth -1, 'minimax' and 'alphabeta' with 0 < depth < 6")
        sys.exit()

    game = ChessGame(player1, player2)

    while not game.is_game_over():
        print(game)
        game.make_move()


