""""
File: day11.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 121-2021
Description: https://adventofcode.com/2021/day/11
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

def light(octo, row, col):
    flashes = 0
    octo[row][col][1] = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0) and row+i in range(len(octo)) and col+j in range(len(octo[row])):
                if octo[row+(i)][col+(j)][1] == 9 and octo[row+(i)][col+(j)][0] == False:
                    octo[row+(i)][col+(j)][0] = True
                    flashes += light(octo, row+(i), col+(j)) + 1
                elif octo[row+(i)][col+(j)][0] == False:
                    octo[row+(i)][col+(j)][1] += 1
    return(flashes)

def p1(data):
    flashes = 0
    octo = [[[False, int (char)] for char in line] for line in data]
    for i in range(100):
        octo = [[[False, octo[row][col][1]] for col in range(len(octo[row]))] for row in range(len(octo))]
        for row in range(len(octo)):
            for col in range(len(octo[row])):
                if octo[row][col][1] == 9 and octo[row][col][0] == False:
                    octo[row][col][0] = True
                    flashes += light(octo, row, col) + 1
                elif octo[row][col][0] == False:
                    octo[row][col][1] += 1
        # for row in octo:
        #     for col in row:
        #         print(str(int(col[0])) + ", " + str(col[1]), end=" | ")
        #     print()
    return(flashes)

def p2(data):
    sync = False
    flashes = 0
    steps = 0
    octo = [[[False, int (char)] for char in line] for line in data]
    while sync == False:
        steps += 1
        sync = True
        octo = [[[False, octo[row][col][1]] for col in range(len(octo[row]))] for row in range(len(octo))]
        for row in range(len(octo)):
            for col in range(len(octo[row])):
                if octo[row][col][1] == 9 and octo[row][col][0] == False:
                    octo[row][col][0] = True
                    flashes += light(octo, row, col) + 1
                elif octo[row][col][0] == False:
                    octo[row][col][1] += 1
        for row in octo:
            for col in row:
                if not (sync == True and col[0] == True):
                    sync = False

    return(steps)

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day11.py <I/O file identifier>")
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