""""
File: day05.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-05-2021
Description: https://adventofcode.com/2021/day/05
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day05.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])


if __name__ == '__main__':
    main()