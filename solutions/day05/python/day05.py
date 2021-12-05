""""
File: day05.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-05-2021
Description: https://adventofcode.com/2021/day/05
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

class VentLine:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.diagonal = (x1 != x2) and (y1 != y2)

    def get_points(self):
        # determine if the x and y coordinates count up or down
        x_inc = 1
        y_inc = 1
        if self.x1 > self.x2:
            x_inc = -1
        if self.y1 > self.y2:
            y_inc = -1

        # draw lines differently if lines are horizontal/vertical or diagonal
        points = []
        if not self.diagonal:
            points
            for x in range(self.x1, self.x2+x_inc, x_inc):
                for y in range(self.y1, self.y2+y_inc, y_inc):
                    points.append( (x,y) )
        else:
            # starting points
            x = self.x1
            y = self.y1

            # draw points until the end point is reached
            points = []
            while ((x - self.x2 - x_inc) and (y - self.y2 - y_inc)):
                points.append( (x,y) )
                x += x_inc
                y += y_inc

        return points

    def __str__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"


def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day05.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])
    data_in = aoc_handler.get_input()

    if len(data_in) < 1:
        raise BadInputException()

    # parse each line in the input to a VentLine
    vent_lines = []
    for line in data_in:
        points = line.split("->")
        points = [point.strip().split(",") for point in points]
        x1,y1,x2,y2 = [int(num) for point in points for num in point]
        vent_lines.append(VentLine(x1, y1, x2, y2))


    # count the number of lines located at each point on the ocean floor
    all_points = {}
    for vent_line in vent_lines:
        for point in vent_line.get_points():
            current_count = all_points.get(point, 0)
            current_count += 1
            all_points[point] = current_count

    # get the number of points that have 2 or more lines through them
    danger_points = 0
    DANGER_THRESHOLD = 2
    for point, count in all_points.items():
        if count >= DANGER_THRESHOLD:
            danger_points += 1

    aoc_handler.write_output(danger_points, verbose=True)

if __name__ == '__main__':
    main()