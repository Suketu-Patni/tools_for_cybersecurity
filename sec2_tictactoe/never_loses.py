sample_string = """I am a bot who plays tic-tac-toe using advanced randomized algorithms. Can you beat me?

Game [1/250]
_ _ o 
_ x _ 
_ _ _ 
Enter the block you want to mark as row,column. Eg: 0,2
"""

def process_string(string):
    # returns a 3x3 array with each entry either 'o', 'x', or '_' (empty)
    lines = string.strip().split("\n")
    return [line.split() for line in lines[-4: -1]]

def locations(board):
    x_locs = []
    o_locs = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'x':
                x_locs.append((row, col))
            elif board[row][col] == 'o':
                o_locs.append((row, col))

    return (x_locs, o_locs)

def get_move(board):
    # accepts ttt board, returns move to play for 'o'
    # will always have 'o' at (0, 2)
    x_s, o_s = locations(board)
    o_count = len(o_s)
    # in any unfinished game, whenever we accept string, number of 'o's == number of 'x's
    
    ...

def get_new_move(old_board, new_board):
    for row in range(3):
        for col in range(3):
            if old_board[row][col] == '_' and new_board[row][col] == 'x':
                return (row, col)
            





print(process_string(sample_string))

def get_x_position():
    ...

# Step 1: take input

from concurrent.futures import process
from pwn import * 
context.log_level = "critical"
from time import sleep

pty = process.PTY
s = process("./ttt", stdin=pty, stdout=pty)

for _ in range(250):

    instruction = s.recv().decode('latin-1')
    print(instruction)
    s.sendline("0,2")
    

s.close()

# algorithm -> always start with 0,2
# 