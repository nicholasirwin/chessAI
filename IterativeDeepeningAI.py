# IterativeDeepeningAI - Iterative adversarial search to visualize move selection/scoring in MinimaxAI.
#
# Inputs: search depth and boolean for player's color (white = True, black = False)
#
# Author: Nicholas Irwin, October 2021

from MinimaxAI import MinimaxAI


class IterativeDeepeningAI:
    def __init__(self, depth, color):
        self.depth = depth
        self.best_move = None
        self.MinimaxAI = MinimaxAI(0, color)  # minimax instance

    def choose_move(self, board):
        for i in range(1, self.depth + 1):  # loop over depths
            self.MinimaxAI.depth = i
            self.best_move = self.MinimaxAI.choose_move(board)  # choose move!
            print("depth " + str(i) + " " + str(self.best_move))

        print("IterativeDeepening AI recommending move " + str(self.best_move) + " at depth " + str(self.depth))
        return self.best_move
