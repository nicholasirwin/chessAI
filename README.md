CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Methods
 * Testing
 

INTRODUCTION
------------
In this project, I write a program for playing chess using two adversarial search methods, minimax and minimax with alpha-beta pruning. I use the Python chess package (https://pypi.org/project/python-chess/) to wrap the game. The game can be visualized and played at the command line following the instructions below.

METHODS
------------
- `MinimaxAI(depth, color)`:
    - `choose_move(board)`: Given a current board state, return the move for the player with the maximum expected utility up to a certain depth.
    - `max_value(board)`: Given a current board, find the maximum utility value associated with each move.
    - `min_value(board)`: Given a current board, find the minimum utility value associated with each move.
    - `eval(board)`: Material value heuristic function. Given current board, return the score for the current player - score for opponent. Count pawn as 1, knight as 3, bishop as 3, rook as 5, queen as 9, and king as 200.
    - `cutoff_test(board)`: Given a current board, score infinity if player has checkmated opponent or -infinity if opponent has checkmated player. Otherwise, score 0.
- `AlphaBetaAI(depth, color)`:
    - `max_value(board, alpha, beta)`: Given a current board, find the maximum utility value associated with each move. Track best move utility in alpha and update accordingly.
    - `min_value(board, alpha, beta)`: Given a current board, find the minimum utility value associated with each move. Track worst move utility in beta and update accordingly.
    
TESTING
------------
In order to play my chess AI, first go to the command line then navigate to the directory where this project is stored. You can play by executing the command line sequence: `python3 [player1] [depth1] [player2] [depth2]`, where players 1 and 2 can be one of 'human', 'random', 'minimax', 'alphabeta'. Similarly, if playing as a human or random AI, depth needs to be -1. When playing Minimax or AlphaBeta, depth can be any integer between 1 and 5, inclusive. Enjoy!
