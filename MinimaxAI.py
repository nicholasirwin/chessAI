import chess
import math


class MinimaxAI():
    def __init__(self, depth, color):
        self.depth = depth
        self.color = color      # true for white, false for black
        self.nodes_visited = 0
        self.num_moves = 0

    # function to return best move given board
    def choose_move(self, board):

        self.nodes_visited = 0
        self.num_moves += 1

        # find maximal value and associated move
        best_val = - math.inf
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            self.nodes_visited += 1
            self.depth -= 1
            val = self.min_value(board)
            self.depth += 1
            if val >= best_val:
                best_val = val
                best_move = move
            board.pop()

        print("MinimaxAI recommending move " + str(best_move) + " with value " + str(best_val))
        print("nodes visited " + str(self.nodes_visited))
        print("num moves: " + str(self.num_moves))
        return best_move

    # function for penalizing/rewarding checkmate accordingly
    def cutoff_test(self, board):
        if board.is_checkmate:
            if board.outcome().winner == self.color:
                return math.inf
            else:
                return -math.inf
        return 0

    # returns a utility value
    def max_value(self, board):
        # case 1: we have reached a terminal state (a win or a draw)
        # we need to see if checkmate and reward/penalize accordingly
        if board.is_game_over():
            return self.cutoff_test(board)

        # case 2: we have reached the specified max depth
        if self.depth == 0:
            return self.eval(board)

        # get maximal next move
        v = -math.inf
        for move in board.legal_moves:
            # v = max(v, min-value(result(s, a)))
            board.push(move)
            self.nodes_visited += 1
            self.depth -= 1
            v = max(v, self.min_value(board))
            self.depth += 1
            board.pop()
        return v

    # returns a utility value
    def min_value(self, board):
        # case 1: we have reached a terminal state (a win or a draw)
        # we need to see if checkmate and reward/penalize accordingly
        if board.is_game_over():
            return self.cutoff_test(board)

        # case 2: we have reached the specified max depth
        if self.depth == 0:
            return self.eval(board)

        # minimize next move
        v = math.inf
        for move in board.legal_moves:
            board.push(move)
            self.nodes_visited += 1
            self.depth -= 1
            v = min(v, self.max_value(board))
            self.depth += 1
            board.pop()

        return v

    # material value heuristic function: simply add up these feature values to obtain the evaluation of the player
    # account for which color is player and which color is opponent
    def eval(self, board):

        white_score = 0
        black_score = 0
        pieces_dict = {"p": 1, "n": 3, "b": 3, "r": 5, "q": 9, "k": 200}

        # for each square,
        for square in chess.SQUARES:
            # grab piece on square if there
            piece = board.piece_at(square)
            if piece is not None:
                # increment color scores accordingly
                if piece.color == chess.WHITE:
                    white_score += pieces_dict[piece.symbol().lower()]
                else:
                    black_score += pieces_dict[piece.symbol()]

            # otherwise, no piece so continue

        # return appropriate score for player's color
        if self.color:
            return white_score - black_score
        else:
            return black_score - white_score
