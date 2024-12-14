# from enum import Enum
# import math

# class Mark(Enum):
#     X = 2
#     O = 4
#     EMPTY = 8

# class State(Enum):
#     DRAW = 1
#     ONGOING = 2
#     OVER = 3

# class TicTacBoard:

#     def __init__(self):
#         # self.size = size
#         # self.size_per_square = size / 3
#         self.boardMatrix = [[Mark.EMPTY.value for x in range(3)] for y in range(3)]
#         self.turnToPlay = Mark.O
#         # self.mark_size = int(self.size_per_square / 2)
#         self.winningMarks = []
#         self.state = State.ONGOING
#         self.winner = None
#         self.moves = []

#     def get_turn_to_play(self):
#         return self.turnToPlay

#     def get_state(self):
#         return self.state

#     def get_winner(self):
#         return self.winner

#     def get_board(self):
#         return self.boardMatrix

#     def get_possible_moves(self):
#         possibleMoves = []
#         for x in range(0,3):
#             for y in range(0,3):
#                 if self.boardMatrix[x][y] is Mark.EMPTY.value:
#                     possibleMoves.append((x,y))
#         return possibleMoves

#     def make_move(self, coordinates):
#         x = coordinates[0]
#         y = coordinates[1]
#         if (self.boardMatrix[x][y] == Mark.EMPTY.value):
#             self.boardMatrix[x][y] = self.turnToPlay.value
#             self.__switch_players()
#             self.__update_board_state()
#             self.moves.append(coordinates)

#     def undo(self):
#         lastMove = self.moves.pop()
#         if lastMove:
#             self.boardMatrix[lastMove[0]][lastMove[1]] = Mark.EMPTY.value
#             self.__switch_players()
#             self.__update_board_state()

#     def __update_board_state(self):
#         board_eval = self.evaluate_board_state()
#         self.state = board_eval[0]
#         self.winningMarks = []
#         self.winner = None
#         if (self.state is State.OVER):
#             self.winningMarks = board_eval[2:]
#             self.winner = board_eval[1]

#     def __switch_players(self):
#         self.turnToPlay = Mark.X if self.turnToPlay is Mark.O else Mark.O

#     def evaluate_board_state(self):
#         draw = True
#         for x in range(3):
#             for y in range(3):
#                 mark = Mark(self.boardMatrix[x][y])
#                 if mark is Mark.EMPTY:
#                     draw = False
#                     continue
#                 else:
#                     # Horizontal
#                     try:
#                         if (mark.value | self.boardMatrix[x+1][y] | self.boardMatrix[x+2][y]) == mark.value:
#                             return (State.OVER, mark, (x, y), (x+1, y), (x+2, y))
#                     except:
#                         pass

#                     # Vertical
#                     try:
#                         if (mark.value | self.boardMatrix[x][y+1] | self.boardMatrix[x][y+2]) == mark.value:
#                             return (State.OVER, mark, (x, y), (x, y+1), (x, y+2))
#                     except:
#                         pass

#                     # Diagonal
#                     if x == 0 and y == 0 and (mark.value | self.boardMatrix[x+1][y+1] | self.boardMatrix[x+2][y+2] == mark.value):
#                         return (State.OVER, mark, (x, y), (x+1, y+1), (x+2, y+2))
#                     elif x == 0 and y == 2 and (mark.value | self.boardMatrix[x+1][y-1] | self.boardMatrix[x+2][y-2] == mark.value):
#                         return (State.OVER, mark, (x, y), (x+1, y-1), (x+2, y-2))

#         return [State.DRAW if draw else State.ONGOING]

# def minimax(isMaxTurn, maximizerMark, board):
#     state = board.get_state()
#     if (state is State.DRAW):
#         return 0
#     elif (state is State.OVER):
#         return 1 if board.get_winner() is maximizerMark else -1

#     scores = []
#     for move in board.get_possible_moves():
#         board.make_move(move)
#         scores.append(minimax(not isMaxTurn, maximizerMark, board))
#         board.undo()
#         if (isMaxTurn and max(scores) == 1) or (not isMaxTurn and min(scores) == -1):
#             break

#     return max(scores) if isMaxTurn else min(scores)

# def make_best_move(ticTacBoard):
#     bestScore = -math.inf
#     bestMove = None
#     for move in ticTacBoard.get_possible_moves():
#         ticTacBoard.make_move(move)
#         score = minimax(False, aiPlayer, ticTacBoard)
#         ticTacBoard.undo()
#         if (score > bestScore):
#             bestScore = score
#             bestMove = move
#     return bestMove
#     # ticTacBoard.make_move(bestMove)

# Python3 program to find the next optimal move for a player 
player, opponent = 'o', 'x'

# This function returns true if there are moves 
# remaining on the board. It returns false if 
# there are no moves left to play. 
def isMovesLeft(board) : 

	for i in range(3) : 
		for j in range(3) : 
			if (board[i][j] == '_') : 
				return True
	return False

# This is the evaluation function as discussed 
# in the previous article ( http://goo.gl/sJgv68 ) 
def evaluate(b) : 
	
	# Checking for Rows for X or O victory. 
	for row in range(3) :	 
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :		 
			if (b[row][0] == player) : 
				return 10
			elif (b[row][0] == opponent) : 
				return -10

	# Checking for Columns for X or O victory. 
	for col in range(3) : 
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) : 
		
			if (b[0][col] == player) : 
				return 10
			elif (b[0][col] == opponent) : 
				return -10

	# Checking for Diagonals for X or O victory. 
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) : 
	
		if (b[0][0] == player) : 
			return 10
		elif (b[0][0] == opponent) : 
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) : 
	
		if (b[0][2] == player) : 
			return 10
		elif (b[0][2] == opponent) : 
			return -10

	# Else if none of them have won then return 0 
	return 0

# This is the minimax function. It considers all 
# the possible ways the game can go and returns 
# the value of the board 
def minimax(board, depth, isMax) : 
	score = evaluate(board) 

	# If Maximizer has won the game return his/her 
	# evaluated score 
	if (score == 10) : 
		return score 

	# If Minimizer has won the game return his/her 
	# evaluated score 
	if (score == -10) : 
		return score 

	# If there are no more moves and no winner then 
	# it is a tie 
	if (isMovesLeft(board) == False) : 
		return 0

	# If this maximizer's move 
	if (isMax) :	 
		best = -1000

		# Traverse all cells 
		for i in range(3) :		 
			for j in range(3) : 
			
				# Check if cell is empty 
				if (board[i][j]=='_') : 
				
					# Make the move 
					board[i][j] = player 

					# Call minimax recursively and choose 
					# the maximum value 
					best = max( best, minimax(board, 
											depth + 1, 
											not isMax) ) 

					# Undo the move 
					board[i][j] = '_'
		return best 

	# If this minimizer's move 
	else : 
		best = 1000

		# Traverse all cells 
		for i in range(3) :		 
			for j in range(3) : 
			
				# Check if cell is empty 
				if (board[i][j] == '_') : 
				
					# Make the move 
					board[i][j] = opponent 

					# Call minimax recursively and choose 
					# the minimum value 
					best = min(best, minimax(board, depth + 1, not isMax)) 

					# Undo the move 
					board[i][j] = '_'
		return best 

# This will return the best possible move for the player 
def findBestMove(board) : 
	bestVal = -1000
	bestMove = (-1, -1) 

	# Traverse all cells, evaluate minimax function for 
	# all empty cells. And return the cell with optimal 
	# value. 
	for i in range(3) :	 
		for j in range(3) : 
		
			# Check if cell is empty 
			if (board[i][j] == '_') : 
			
				# Make the move 
				board[i][j] = player 

				# compute evaluation function for this 
				# move. 
				moveVal = minimax(board, 0, False) 

				# Undo the move 
				board[i][j] = '_'

				# If the value of the current move is 
				# more than the best value, then update 
				# best/ 
				if (moveVal > bestVal) :				 
					bestMove = (i, j) 
					bestVal = moveVal 
	return bestMove 
# Driver code 


# This code is contributed by divyesh072019


sample_string = """I am a bot who plays tic-tac-toe using advanced randomized algorithms. Can you beat me?

Game [1/250]
_ x o 
_ _ _ 
_ _ _ 
Enter the block you want to mark as row,column. Eg: 0,2
"""

def process_string(string: str):
    # returns a 3x3 array with each entry either 'o', 'x', or '_' (empty)
    lines = string.strip().split("\n")
    return [line.split() for line in lines[-4: -1]]
    # for row in range(3):
    #     for col in range(3):
    #         if board[row][col] == 'o':
    #             board[row][col] = Mark.O.value
    #         elif board[row][col] == 'x':
    #             board[row][col] = Mark.X.value
    #         else:
    #             board[row][col] = Mark.EMPTY.value
    # return board

# ticTacBoard = TicTacBoard()
# ticTacBoard.boardMatrix = process_string(sample_string)

# board = process_string(sample_string)

# bestMove = findBestMove(board) 

# print("The Optimal Move is :") 
# print("ROW:", bestMove[0], " COL:", bestMove[1]) 


# print(make_best_move())
# make_best_move()
# make_best_move()
# make_best_move()
# make_best_move()
# make_best_move()
# make_best_move()
# make_best_move()
# print(ticTacBoard.boardMatrix)
# print(process_string(sample_string))

from concurrent.futures import process
from pwn import * 
context.log_level = "critical"
from time import sleep

pty = process.PTY
s = process("./ttt", stdin=pty, stdout=pty)
# ticTacBoard = TicTacBoard()
s.recv()
# playAs = Mark.O
# aiPlayer = Mark.X

for _ in range(249):
    # instruction = s.recv().decode('latin-1')
    # print(instruction)
    s.sendline("0,2".encode())
	
    new_instruction = s.recvuntil("Eg: 0,2".encode()).decode('latin-1')
    while "Game" not in new_instruction:
        print(new_instruction)
        current_board = process_string(new_instruction)
        best_move = findBestMove(current_board)
        # ticTacBoard.make_move(best_move)
        s.sendline((str(best_move[0]) + "," + str(best_move[1])).encode())
        # sleep(0.1)
        new_instruction = s.recvuntil("Eg: 0,2".encode()).decode('latin-1')
        print(new_instruction)
		
s.interactive()
# s.recv().decode('latin-1')
# s.close()
