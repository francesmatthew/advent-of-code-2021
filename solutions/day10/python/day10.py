""""
File: day10.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-10-2021
Description: https://adventofcode.com/2021/day/10
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

def p1(data):
    pass

def p2(data):
    pass

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day10.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input()
    if len(data_in) < 1:
        raise BadInputException()

    # parse input data

    solution1 = p1(data_in)
    solution2 = p2(data_in)

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()