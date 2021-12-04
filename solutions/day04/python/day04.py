""""
File: day04.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-04-2021
Description: https://adventofcode.com/2021/day/4
"""
from AOCHandler import AOCHandler, BadInputException
from BingoBoard import BingoBoard, GameWin
import sys
import os

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day04.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])
    data_in = aoc_handler.get_input()

    if len(data_in) < 2:
        raise BadInputException()

    # get the list of called numbers from the first line
    call_num_list = [int(num_str) for num_str in data_in[0].split(',')]

    # size of the bingo board is determined by the number of entries in second line
    board_size = len([0 for data_str in data_in[1].split(" ") if data_str != ""])

    # get all possible bingo boards from subsequent lines
    boards = []
    for board_start in range(1, len(data_in), board_size):
        new_board = BingoBoard(board_size)
        for i in range(board_size):
            # board_start is the index of the first row of board data in data_in
            # i is the row index for this specific board
            board_row = data_in[board_start + i].split(" ")
            # convert list of strings to numbers, ignoring empty strings
            board_row = [int(num_str) for num_str in board_row if num_str != ""]
            new_board.set_row(board_row, i)
        boards.append(new_board)

    # find first board to win by calling each number for each board...
    # ...until a GameWin exception is raised
    call_index = 0
    try:
        while (call_index < len(call_num_list)):
            call_num = call_num_list[call_index]
            for board in boards:
                # call the current number and check if that number triggered a win
                board.call_num(call_num)
                if board.check_win():
                    raise GameWin(board)
            # increment to the next call number only if all boards have been called with this number
            call_index += 1
    except GameWin as win:
        # get the score of the first board to win
        first_score = win.winning_board.get_score()
        # remove it from the list of boards to find the last board to win
        boards.remove(win.winning_board)
    else:
        # somehow all numbers have been called without a GameWin exception being raised
        first_score = 0

    # find the last board to win
    # the last board to win must have all its winning numbers called in order to get the score...
    # ...so keep track of the previous board that won until there are no more boards left
    last_win = None
    while ( (len(boards) > 0) and (call_index < len(call_num_list))):
        call_num = call_num_list[call_index]
        for board in boards[:]:
            board.call_num(call_num)
            if board.check_win():
                last_win = board
                boards.remove(board)
        call_index += 1

    # last board to win should have been found
    if (last_win is not None) and (len(boards) == 0):
        last_score = last_win.get_score()
    else:
        last_score = 0

    aoc_handler.write_output(first_score, last_score, verbose=True)

if __name__ == '__main__':
    main()