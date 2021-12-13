""""
File: day13.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 12-13-2021
Description: https://adventofcode.com/2021/day/13
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os


def fx(xs, x): #2fold - y
    for i in range(len(xs)):
        if xs[i] >= x:
            xs[i] = 2 * x - xs[i]
def fy(ys, y):
    for i in range(len(ys)):
        if ys[i] >= y:
            ys[i] = 2 * y - ys[i]

def p1(data):
    coords = []
    xs = []
    ys = []
    for line in data:
        if "x=" in line:
            fx(xs, int(line[13:]))
        elif "y=" in line:
            fy(ys, int(line[13:]))
        else:
            coords = line.split(',')
            xs.append(int(coords[0]))
            ys.append(int(coords[1]))
        
    display_points(xs, ys)

def display_points(xs, ys):
    max_x = max(xs)
    max_y = max(ys)
    display = [ ["  " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for i in range(len(xs)):
        display[ys[i]][xs[i]] = "||"
    for line in display:
        print("".join(line))

def p2(data):
    pass

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day13.py <I/O file identifier>")
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