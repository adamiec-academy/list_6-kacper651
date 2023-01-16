from time import sleep
from copy import deepcopy


def info(data, turn_counter):
    print()
    print("-------- {} --------".format(turn_counter))
    for row in data:
        for element in row:
            print(element, end="")
        print()


def make_turn(board):
    new_board = deepcopy(board)
    size_y, size_x = len(board), len(board[0])

    # TODO: Make a turn
    
    return new_board


def play(starting_board, turns):
    
    current_board = starting_board

    for _ in range(turns):
        current_board = make_turn(current_board)

    return current_board


def play_forever(starting_board, interval):
    
    current_board = starting_board
    current_turn = 0
    info(current_board, current_turn)

    while True:
        current_board = make_turn(current_board)
        current_turn += 1
        info(current_board, current_turn)
        sleep(interval)
