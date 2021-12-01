""""
File: day01.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-01-2021
Description:
"""
import sys
sys.path.append('..')
from AOCHandler import AOCHandler

def main():
    aoc_handler = AOCHandler("input.txt", "output.txt")
    input = aoc_handler.get_input()

    solution = 0
    for i in range(1, len(input)):
        if (input[i] > input[i-1]):
            solution += 1

    aoc_handler.write_output(str(solution))


if __name__ == '__main__':
    main()