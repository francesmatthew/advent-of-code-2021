""""
File: day01.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-01-2021
Description: https://adventofcode.com/2021/day/1
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from AOCHandler import AOCHandler

def main():
    aoc_handler = AOCHandler("input.txt", "output.txt")
    input = aoc_handler.get_input_int()

    # count the number of times the current entry is greater than the previous entry
    single_increase = 0
    for i in range(1, len(input)):
        if (input[i] > input[i-1]):
            single_increase += 1

    # "consider sums of a three-measurement sliding window" i.e.:
    # 199  A      
    # 200  A B    
    # 208  A B C  
    # 210    B C D
    # 200  E   C D
    # 207  E F   D
    # 240  E F G  
    # 269    F G H
    # 260      G H
    # 263        H
    # count the number of times the current sliding window is greater than the previous sliding window
    triplet_increase = 0
    for i in range(3, len(input)):
        current_triplet = input[i] + input[i-1] + input[i-2]
        prev_triplet = input[i-1] + input[i-2] + input[i-3]
        if (current_triplet > prev_triplet):
            triplet_increase += 1

    aoc_handler.write_output(single_increase, triplet_increase, verbose=True)


if __name__ == '__main__':
    main()