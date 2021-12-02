""""
File: day03.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-03-2021
Description:
"""
from AOCHandler import AOCHandler
import sys
import os


def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day03.py <I/O file identifier>")
        return
    # enter matt,nick,example to choose input
    aoc_handler = AOCHandler(sys.argv[1])
    #returns data as list of strings, can do int list too
    data_in = aoc_handler.get_input()
    #writes to output directory, if verbose = True, print to console
    aoc_handler.write_output(solution, verbose=True)


if __name__ == '__main__':
    main()
