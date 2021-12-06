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

    fish_in = [int(num) for line in aoc_handler.get_input() for num in line.split(",") ]

    if len(fish_in) < 1:
        raise BadInputException()

    # count the number of lanternsfish with each possible timer value
    fishes = {}
    for i in range(9):
        fishes[i] = 0
    for fish in fish_in:
        fishes[fish] += 1

    # simulate fish creation
    for _ in range(256):
        new_fish = fishes[0]
        # age fish
        for age in range(1,9):
            fishes[age-1] = fishes[age]
        fishes[6] += new_fish
        fishes[8] = new_fish

    num_fish = 0
    for count in fishes.values():
        num_fish += count

    aoc_handler.write_output(num_fish, verbose=True)

if __name__ == '__main__':
    main()