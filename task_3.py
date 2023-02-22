from time import sleep
from copy import deepcopy


def info(data, turn_counter):
    print()
    print("-------- {} --------".format(turn_counter))
    for row in data:
        for element in row:
            print(f"{element} ", end="")
        print()


def make_turn(board):
    new_board = deepcopy(board)
    size_y, size_x = len(board), len(board[0])

    adj_cells_count = 0
    for i in range(size_y):
        for j in range(size_x):
            neighbourhood = get_adj_cells(i, j, size_y, size_x)
            for point in neighbourhood:
                if board[point[0]][point[1]] == "X":
                    adj_cells_count += 1
            if adj_cells_count > 3 or adj_cells_count < 2:
                new_board[i][j] = "."
            elif adj_cells_count == 3:
                new_board[i][j] = "X"

            adj_cells_count = 0

    return new_board


def get_adj_cells(i, j, m, n):
    adj_cells = []
    if i > 0:
        adj_cells.append((i - 1, j))
    if i + 1 < m:
        adj_cells.append((i + 1, j))
    if j > 0:
        adj_cells.append((i, j - 1))
    if j + 1 < n:
        adj_cells.append((i, j + 1))
    if i > 0 and j > 0:
        adj_cells.append((i - 1, j - 1))
    if i + 1 < m and j + 1 < n:
        adj_cells.append((i + 1, j + 1))
    if i > 0 and j + 1 < n:
        adj_cells.append((i - 1, j + 1))
    if i + 1 < m and j > 0:
        adj_cells.append((i + 1, j - 1))

    return adj_cells


def play(starting_board, turns):
    current_board = starting_board
    info(current_board, 0)

    for i in range(turns):
        sleep(1)
        current_board = make_turn(current_board)
        info(current_board, i + 1)

    return current_board


def play_forever(starting_board, interval):
    current_board = starting_board
    current_turn = 0
    info(current_board, current_turn)

    while True:
        sleep(interval)
        current_board = make_turn(current_board)
        current_turn += 1
        info(current_board, current_turn)


board = [
            [".", ".", ".", ".", ".", ".", ".", ],
            [".", "X", ".", "X", "X", "X", ".", ],
            [".", "X", ".", "X", ".", ".", ".", ],
            [".", "X", "X", "X", "X", "X", ".", ],
            [".", ".", ".", "X", ".", "X", ".", ],
            [".", "X", "X", "X", ".", "X", ".", ],
            [".", ".", ".", ".", ".", ".", ".", ],
        ]

play(board, 6)
