""""
File: day09.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-09-2021
Description: https://adventofcode.com/2021/day/9
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

def p1(data):
    sum_risk = 0
    row_limit = len(data)
    col_limit = len(data[0])
    for i,j in [(i,j) for i in range(row_limit) for j in range(col_limit)]:
        if (i-1) < 0 or data[i-1][j] > data[i][j]:
            if (i+1) >= row_limit or data[i+1][j] > data[i][j]:
                if (j-1) < 0 or data[i][j-1] > data[i][j]:
                    if (j+1) >= col_limit or data[i][j+1] > data[i][j]:
                        # numer is local minimum
                        sum_risk += data[i][j] + 1
    return sum_risk

def p2(data):
    # get minimum of each basin
    minima = []
    row_limit = len(data)
    col_limit = len(data[0])
    for i,j in [(i,j) for i in range(row_limit) for j in range(col_limit)]:
        if (i-1) < 0 or data[i-1][j] > data[i][j]:
            if (i+1) >= row_limit or data[i+1][j] > data[i][j]:
                if (j-1) < 0 or data[i][j-1] > data[i][j]:
                    if (j+1) >= col_limit or data[i][j+1] > data[i][j]:
                        # numer is local minimum
                        minima.append( (i,j) )
    # expand from the basin for each
    basins = []
    for minimum in minima:
        basin = []
        check_points = [ minimum ]
        while len(check_points) != 0:
            i,j = check_points.pop()
            if data[i][j] != 9:
                basin.append( (i,j) )
                for di, dj in ( (-1,0), (1,0), (0,-1), (0,1) ):
                    if (i+di, j+dj) not in basin and (i+di, j+dj) not in check_points:
                        if 0 <= i+di < len(data) and 0 <= j+dj < len(data[0]):
                            check_points.append( (i+di, j+dj) )
        basins.append(basin)

    # calculate size of each basin
    basin_size = []
    for basin in basins:
        basin_size.append(len(basin))
    basin_size.sort()
    basin_size_product = 1
    for i in range(len(basin_size) - 1, len(basin_size) - 4, -1):
        basin_size_product *= basin_size[i]
    return basin_size_product

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day09.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input()
    if len(data_in) < 1:
        raise BadInputException()

    # parse input data
    data_in = [[int(char) for char in line] for line in data_in]

    solution1 = p1(data_in)
    solution2 = p2(data_in)

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()