""""
File: BingoBoard.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-04-2021
Description: BingoBoard class for Advent of Code Day 04
"""

class GameWin(Exception):
    def __init__(self, winning_board):
        self.winning_board = winning_board
        super().__init__()


class BingoBoard:
    """
    BingoBoard is a square matrix of numbers used to play bingo
    self.size is the square dimension of the matrix (the number of row/columns)
    self.numbers if a 2-dimentional matrix of integers on the bingo board
    self.marks is a 2-dimentional matrix of booleans marking which numbers have been called
    self.last_call is the last number to be called, used in score calculation
    """
    def __init__(self, size):
        self.size = size
        self.numbers = [ [0 for _ in range(size)] for _ in range(size)]
        self.marks = [ [False for _ in range(size)] for _ in range(size)]
        self.last_call = 0

    def set_row(self, row_data, row_index):
        """
        Put data into a row of the bingo board
        row_data is a list of numbers
        row_index is the zero-indexed row number to insert data into
        """
        if len(row_data) != self.size:
            raise Exception(f"data is not the same length as board size (size={self.size})")
        self.numbers[row_index] = row_data

    def call_num(self, num):
        """
        mark in a seperate matrix all numbers that match the called number
        """
        for row in range(self.size):
            for column in range(self.size):
                # iterate through each number in the board...
                # ...and mark numbers that match the called number
                if self.numbers[row][column] == num:
                    self.marks[row][column] = True
        self.last_call = num # also keep track of this number as the last one that was called

    def check_win(self):
        """
        check if any row or column has all numbers contiguously marked
        return boolean if this board meets the win condition
        """
        # count the number of marks in each column and in each row
        # ...and compare the number of marks to the size of the matrix

        # matches in a **column** are counted **in parallel**
        column_matches = [0 for _ in range(self.size)]

        for row in range(self.size):
            # matches in a **row** are counted **serially**
            row_matches = 0
            for column in range(self.size):
                if self.marks[row][column]:
                    # mark is preset, increment the count for this row and column
                    row_matches += 1
                    column_matches[column] += 1
            if row_matches == self.size:
                # win if the row has all marks
                return True

        for i_column_matches in column_matches:
            if i_column_matches == self.size:
                # win if any column has all marks
                return True
        return False # default condition

    def get_score(self):
        """
        Calcualte the score of the bingo board after a win
        This function does **not** check if win condition is met
        Returns an integer score
        Return value is only guaranteed to be right if this function is called
        ...immediatly after the call to call_num() that triggered a win
        """
        # find sum of unmarked numbers
        unmarked_sum = 0
        for row in range(self.size):
            for column in range(self.size):
                if not(self.marks[row][column]):
                    unmarked_sum += self.numbers[row][column]
        # return product of sum and last number to be called
        return unmarked_sum* self.last_call

    def __str__(self):
        return str(self.numbers)
