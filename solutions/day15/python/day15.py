""""
File: day15.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 12-15-2021
Description: https://adventofcode.com/2021/day/15
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

class Path:
    def __init__(self, start:tuple=None, copy=None):
        if copy is None:
            self.nodes = [start]
            self.cost = 0
        else:
            self.cost = copy.cost
            self.nodes = copy.nodes[:]

    def extend(self, pos, cost):
        rpath = Path(copy=self)
        rpath.nodes.append(pos)
        rpath.cost += cost
        return rpath

    def __str__(self):
        rstring = str(self.cost) + ":"
        rstring += " " + str(self.nodes)
        return rstring

def sorted_append(path_list, path):
    if len(path_list) == 0:
        path_list.append(path)
    i = len(path_list) - 1
    while i >= 0 and path.cost > path_list[i].cost:
        i -= 1
    path_list.insert(i+1, path)

def get_lowest_path(matrix, start_pos, end_pos):
    costs = [ [None for _ in range(len(matrix[0])) ] for _ in range(len(matrix))]
    paths = [ Path(start=start_pos) ]
    while paths[-1].nodes[-1] != end_pos:
        curr_path = paths.pop()
        i, j = curr_path.nodes[-1]
        for di, dj in ( (0,1), (1,0), (0,-1), (-1,0) ):
            if 0 <= i+di < len(matrix) and 0 <= j+dj < len(matrix[0]):
                new_path = curr_path.extend( (i+di, j+dj), matrix[i+di][j+dj] )
                if costs[i+di][j+dj] is None or new_path.cost < costs[i+di][j+dj]:
                    costs[i+di][j+dj] = new_path.cost
                    sorted_append(paths, new_path)
        # print()
        # for i in range(len(paths)):
        #     print(paths[i])
        # input()
    return paths.pop()

def p1(matrix):
    return get_lowest_path(matrix, (0,0), (len(matrix)-1, len(matrix[0])-1) ).cost

def p2(matrix):
    col_size = len(matrix[0])
    row_size = len(matrix)
    new_matrix = [ [0 for _ in range(col_size * 5) ] for _ in range(row_size * 5)]
    for i in range(row_size):
        for j in range(col_size):
            new_matrix[i][j] = matrix[i][j]
    for c in range(1,5):
        for i in range(row_size):
            for j in range(col_size):
                new_matrix[c*row_size+i][j] = (new_matrix[(c-1)*row_size+i][j] + 1) % 10
                if not new_matrix[c*row_size+i][j]:
                    new_matrix[c*row_size+i][j] = 1
    for k in range(1,5):
        for i in range(row_size * 5):
            for j in range(col_size):
                new_matrix[i][k*col_size+j] = (new_matrix[i][(k-1)*col_size+j] + 1) % 10
                if not new_matrix[i][k*col_size+j]:
                    new_matrix[i][k*col_size+j] = 1

    return get_lowest_path(new_matrix, (0,0), (len(new_matrix)-1, len(new_matrix[0])-1) ).cost

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day15.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input()
    if len(data_in) < 1:
        raise BadInputException()

    # parse input data
    matrix = [ [int(x) for x in line] for line in data_in]

    solution1 = p1(matrix)
    solution2 = p2(matrix)

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()