# Step 5
# ----------------------------------------------------
# flag: "flag{f34r1355_5ud0ku_c0nqu3r0r}"
# ----------------------------------------------------

"""
PROCEDURE (do this 420 times)
1. Get input from interface with the sudoku executable (pwntools + process) 
2. Process string to get 2D array of characters with each entry either a digit ka character or a "." which means empty
3. Run algorithm (pure backtracking, no logical shit cuz that doesn't complete all sudoku puzzles, and also because there's no time limit for this). 
This should return a list of strings "<row> <col> <num>" for sendline
4. Iterate over this list, and keep sendlining 
5. Profit (look above procedure)
"""

# Imports
# ----------------------------------------------------
from concurrent.futures import process
from pwn import * 
context.log_level = "critical"
from time import sleep
# ----------------------------------------------------

# Step 2
# ----------------------------------------------------
def process_string(string):
    lines = string.split("\n")
    lines = lines[-13:-10] + lines[-9:-6] + lines[-5:-2]

    digits_arr = []

    for line in lines:
        row_chars = []
        for ch in line:
            if ch not in ['|', ' ']: 
                row_chars.append(ch)

        digits_arr.append(row_chars)
    return digits_arr
# ----------------------------------------------------

# Step 3
# ----------------------------------------------------

def next(grid, row, col):
    # gets the indices of next fillable cell
    for i in range(row,9):
        for j in range(col,9):
            if grid[i][j] == '.':
                return (i, j)
            
    # if we are already at cell (8,8)             
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j] == '.':
                return i,j

    # nahi mila -> full     
    return (-1, -1)


def get_square_indices(row, col):
    # helper for check_digit
    # returns list of all indices of 3x3 square in which (row, col) lies
    row_start = row - row%3
    col_start = col - col%3

    indices = []

    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            indices.append((i, j))

    return indices

def check_digit(chars_list, row, col, digit):
    # check if digit can fit in chars_list[row][col]

    row_check_failed = (digit in chars_list[row])
    col_check_failed = (digit in [chars_list[i][col] for i in range(9)])
    square_check_failed = (digit in [chars_list[k][r] for (k, r) in get_square_indices(row, col)])

    return not (row_check_failed or col_check_failed or square_check_failed)


def solveSudoku(grid, i=0, j=0):
    i,j = next(grid, i, j)

    if i == -1: # everything full
        return True 
    
    for num in [str(i) for i in range(1,10)]:

        if check_digit(grid,i,j,num):
            grid[i][j] = num

            if solveSudoku(grid, i, j): # tries to solve grid with num at i, j
                return True
            
            grid[i][j] = '.' # grid didn't solve, so replace it with blank to try again

    return False

def compare_and_send_entries(empty, full):
    # if cell was empty in the grid we received, its data must be sent
    entries_to_send = []
    for i in range(9):
        for j in range(9):
            if empty[i][j] == '.':
                entries_to_send.append(f"{i} {j} {full[i][j]}")

    return entries_to_send

def solved(exec_string):
    # combines all processes of algorithm
    cleaned = process_string(exec_string)
    received_grid = [] 

    # idk why but list copy doesn't work :( so i have to do this
    for i in range(9):
        this_row = []
        for j in range(9):
            this_row.append(cleaned[i][j])
        received_grid.append(this_row)

    solveSudoku(received_grid)

    entries = compare_and_send_entries(cleaned, received_grid)
    return entries


# Step 1
# ----------------------------------------------------
pty = process.PTY
s = process("./sudoku", stdin=pty, stdout=pty)

for _ in range(421):

    instruction = s.recv().decode('latin-1')
    print(instruction)
    digit_positions = solved(instruction)

    num_entries = len(digit_positions)

    # Step 4
    # ----------------------------------------------------
    for digit_position_index in range(num_entries):
        s.sendline(digit_positions[digit_position_index].encode())
        sleep(0.001)
        if digit_position_index != num_entries - 1:
            print(s.recv().decode('latin-1'))
    # ----------------------------------------------------

s.close()
# ----------------------------------------------------
