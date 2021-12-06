""""
File: day06.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-06-2021
Description: https://adventofcode.com/2021/day/06
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day06.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    if len(data_in) < 1:
        raise BadInputException()

if __name__ == '__main__':
    main()