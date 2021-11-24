import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from IterativeDeepeningAI import IterativeDeepeningAI
from ChessGame import ChessGame


import sys

## test 1 [experimenting]: HumanPlayer vs. RandomAI
# player1 = HumanPlayer()
# player2 = RandomAI()

# ---------------------------------------------------------------------------------------------------------------------

## test 2 [minimaxAI + eval]: MinimaxAI vs. RandomAI (depth 1)
# player1 = MinimaxAI(1, True)
# player2 = RandomAI()

## test 3 [minimaxAI + eval]: MinimaxAI vs. RandomAI (depth 2)
# player1 = MinimaxAI(2, True)
# player2 = RandomAI()

## test 4 [minimaxAI + eval]: MinimaxAI vs. RandomAI (depth 3)
# player1 = MinimaxAI(3, True)
# player2 = RandomAI()

# ---------------------------------------------------------------------------------------------------------------------

## test 5 [alpha-beta deeper]: AlphaBetaAI vs. RandomAI (depth 3)
player1 = RandomAI()
player2 = AlphaBetaAI(3, False)

## test 6 [alpha-beta deeper]: AlphaBetaAI vs. RandomAI (depth 4)
player1 = AlphaBetaAI(4, True)
player2 = RandomAI()

## test 7 [alpha-beta deeper]: AlphaBetaAI vs. RandomAI (depth 5)
player1 = AlphaBetaAI(5, True)
player2 = RandomAI()

# ---------------------------------------------------------------------------------------------------------------------

## test 8 [same depth]: MinimaxAI vs. AlphaBetaAI (depth 2)
## run a few times, make sure that minimax does not consistently win
player1 = AlphaBetaAI(2, True)
player2 = MinimaxAI(2, False)

## test 9 [same depth]: MinimaxAI vs. AlphaBetaAI (depth 3)
## run a few times, make sure that minimax does not consistently win
player1 = AlphaBetaAI(3, True)
player2 = MinimaxAI(3, False)

# ---------------------------------------------------------------------------------------------------------------------

## test 10.1 [same value]: MinimaxAI vs. HumanPlayer (depth 3)
## check that the values are exact same for MinimaxAI and AlphaBetaAI given same initial state
player1 = HumanPlayer()
player2 = MinimaxAI(3, False)

## test 10.2 [same value]: AlphaBetaAI vs. HumanPlayer (depth 3)
## check that the values are exact same for MinimaxAI and AlphaBetaAI given same initial state
player1 = HumanPlayer()
player2 = AlphaBetaAI(3, False)

# ---------------------------------------------------------------------------------------------------------------------

## test 11: Iterative deepening (depth 3)
## Verify that for some start states, best_move changes (and hopefully improves) as deeper levels are searched.
player1 = IterativeDeepeningAI(3, True)
player2 = RandomAI()

## test 12: Iterative deepening (depth 4)
## Verify that for some start states, best_move changes (and hopefully improves) as deeper levels are searched.
player1 = IterativeDeepeningAI(4, True)
player2 = RandomAI()

# ---------------------------------------------------------------------------------------------------------------------

## test 13: Me vs. AlphaBetaAI
player1 = HumanPlayer()
player2 = AlphaBetaAI(4, False)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()

# print(hash(str(game.board)))
