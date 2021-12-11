""""
File: day11.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 12-11-2021
Description: https://adventofcode.com/2021/day/11
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

MAX_BRIGHT = 9

def inc_brightness(data, flash_grid, i, j):
    if i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
        return 0
    if flash_grid[i][j]:
        return 0
    num_flashes = 0
    if data[i][j] == MAX_BRIGHT:
        num_flashes += 1
        flash_grid[i][j] = True
        data[i][j] = 0
        for di, dj in [ (i,j) for i in (-1,0,1) for j in (-1,0,1)]:
            num_flashes += inc_brightness(data, flash_grid, i+di, j+dj)
    else:
        data[i][j] += 1
    return num_flashes

def tick(data):
    num_flashes = 0
    flash_grid = [ [False for _ in range(len(data[0])) ] for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(len(data[i])):
            num_flashes += inc_brightness(data, flash_grid, i, j)
    synced = count(data) == 0
    return (num_flashes, count(data) == 0 )

def p1(data):
    octo_matrix = [ [int(char) for char in line] for line in data]
    num_flashes = 0
    for _ in range(100):
        num_flashes += tick(octo_matrix)[0]
    return num_flashes

def count(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count += matrix[i][j]
    return count


def p2(data):
    octo_matrix = [ [int(char) for char in line] for line in data]
    synced = False
    i = 0
    while (not synced and i < 100000):
        synced = tick(octo_matrix)[1]
        i += 1
    return i

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day11.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input()
    if len(data_in) < 1:
        raise BadInputException()

    solution1 = p1(data_in)
    solution2 = p2(data_in)

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()