b = [
    [0, 0, 3, 4, 5, 6, 7, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [7, 8, 0, 1, 0, 0, 0, 0, 0],
    [2, 0, 4, 0, 0, 5, 8, 0, 0],
    [3, 6, 0, 0, 9, 7, 0, 0, 0],
    [8, 9, 0, 2, 1, 4, 0, 6, 5],
    [0, 3, 1, 0, 0, 0, 0, 7, 0],
    [0, 0, 2, 9, 0, 0, 0, 0, 1],
    [0, 0, 8, 0, 3, 1, 6, 4, 2]
]

def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(num)
            else:
                print(str(num) + " ", end="")

def is_valid(board, num, row, column):
    if num not in get_subboard(board, row, column):
        if num not in get_column(board, column):
            if num not in board[row]:
                return True
    return False

def get_column(board, index):
    return [row[index] for row in board]

def get_subboard(board, row, column):
    sub = []
    row, column = (row // 3) * 3, (column // 3) * 3
    for r in board[row:row + 3]:
        sub.extend(r[column:column + 3])
    return sub

def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def solve(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for i in range(1, 10):
        if is_valid(board, i, row, col):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def main():
    result = solve(b)
    if result:
        print_board(b)
        print("Sudoku has been solved!")
    else:
        print("Your Sudoku is wrong!")

main()