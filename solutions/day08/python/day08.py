""""
File: day08.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-08-2021
Description: https://adventofcode.com/2021/day/8
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

A='a'
B='b'
C='c'
D='d'
E='e'
F='f'
G='g'
ALL_SYMBOLS = [A,B,C,D,E,F,G]
DISPLAY_SEGMENTS = {
    0: ["a", "b", "c", "e", "f", "g"],
    1: ["c", "f"],
    2: ["a", "c", "d", "e", "g"],
    3: ["a", "c", "d", "f", "g"],
    4: ["b", "c", "d", "f"],
    5: ["a", "b", "d", "f", "g"],
    6: ["a", "b", "d", "e", "f", "g"],
    7: ["a", "c", "f"],
    8: ["a", "b", "c", "d", "e", "f", "g"],
    9: ["a", "b", "c", "d", "f", "g"]
}
def p1(entries):
    UNIQUE_SEGMENTS = [1,4,7,8]
    num_unique_seg = 0
    for entry in entries:
        for segments in entry[1]:
            for unique_num in UNIQUE_SEGMENTS:
                if len(segments) == len(DISPLAY_SEGMENTS[unique_num]):
                    num_unique_seg += 1
    return num_unique_seg

def p2(entries):
    intersect = lambda lsta, lstb : set(lsta).intersection(lstb)

    sum_output = 0
    for entry in entries:
        UNIQUE_SEGMENTS = [1,4,7,8]
        output = 0
        # keep track of how certain digits are decoded
        decode_segments = {}
        for i in range(10):
            decode_segments[i] = []
        # determine mappings from number not in output
        for digit_segments in entry[0]:
            # first, decode the number if it has a unique number of segments
            for unique_num in UNIQUE_SEGMENTS:
                if len(digit_segments) == len(DISPLAY_SEGMENTS[unique_num]):
                    decoded_digit = unique_num
                    decode_segments[decoded_digit] = digit_segments

        for digit_segments in entry[1]:
            # first, decode the number if it has a unique number of segments
            decoded_digit = None
            for unique_num in UNIQUE_SEGMENTS:
                if len(digit_segments) == len(DISPLAY_SEGMENTS[unique_num]):
                    decoded_digit = unique_num
                    decode_segments[decoded_digit] = digit_segments
            # then, decode numbers that have a non-unique number of segments
            if decoded_digit is None:
                decoded_digit = 0 # TODO: figure out how to deduce these combinations of segments
                if len(digit_segments) == 6:
                    # number is 0, 6, or 9
                    pass
                elif len(digit_segments) == 5:
                    # number is 2, 3, or 5
                    pass
            # append this digit to the output
            output *= 10
            output += decoded_digit
        sum_output += output

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day08.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    # parse input
    entries = aoc_handler.get_input()
    if len(entries) < 1:
        raise BadInputException()
    entries = [entry.split(" | ") for entry in entries]
    for entry in entries:
        entry[0] = entry[0].split(" ")
        entry[1] = entry[1].split(" ")

    solution1 = p1(entries)
    solution2 = p2(entries)

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()