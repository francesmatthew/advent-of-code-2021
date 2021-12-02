""""
File: day02.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-02-2021
Description: https://adventofcode.com/2021/day/2
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__)))))
from AOCHandler import AOCHandler


FORWARD = "forward"
UP = "up"
DOWN = "down"


def main():
    # Part 1
    # forward X increases the horizontal position by X units.
    # down X increases the depth by X units.
    # up X decreases the depth by X units.

    # Part 2
    # down X increases your aim by X units.
    # up X decreases your aim by X units.
    # forward X does two things:
    #   It increases your horizontal position by X units.
    #   It increases your depth by your aim multiplied by X.

    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day02.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])
    data_in = aoc_handler.get_input()

    hpos = 0
    bad_depth = 0
    good_depth = 0
    aim = 0

    for line in data_in:
        (instruction, num) = line.split(' ')
        num = int(num)

        if instruction == FORWARD:
            hpos += num
            good_depth += (aim*num)
        elif instruction == UP:
            bad_depth -= num
            aim -= num
        elif instruction == DOWN:
            bad_depth += num
            aim += num

    solution1 = hpos * bad_depth
    solution2 = hpos * good_depth
    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()
