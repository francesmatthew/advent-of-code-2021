""""
File: day13.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 12-13-2021
Description: https://adventofcode.com/2021/day/13
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

def exec_instruction(points, instruction):
    if "x=" in instruction:
        # reflect all points to the right of the given x-coordinate
        xline = int(instruction[13:])
        for point in points:
            if point[0] >= xline:
                point[0] = 2*xline - point[0]
    if "y=" in instruction:
        # reflect all points below the given y-coordinate
        yline = int(instruction[13:])
        for point in points:
            if point[1] >= yline:
                point[1] = 2*yline - point[1]

def p1(points, instructions):
    # execute only first fold
    exec_instruction(points, instructions[0])
    return len(set([(x,y) for x,y in points]))

def p2(points, instructions):
    for instruction in instructions:
        exec_instruction(points, instruction)
    # defer to monkey brain for letter recognition
    display_points(points)
    return input("What do you see? ")

def display_points(points):
    max_x = max([x for x,y in points])
    max_y = max([y for x,y in points])
    # create a matrix of blank spaces and fill in where a point is present
    display = [ ["  " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x,y in points:
        display[y][x] = "||"
    for line in display:
        print("".join(line))

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day13.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input_raw()
    if len(data_in) < 1:
        raise BadInputException()

    # parse input data
    points_in, instructions = data_in.split("\n\n")
    points_in = points_in.split("\n")
    instructions = instructions.split("\n")
    points = []
    for line in points_in:
        x,y = line.split(",")
        points.append( [int(x), int(y)] )

    solution1 = p1(points, instructions)
    solution2 = p2(points, instructions)

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()