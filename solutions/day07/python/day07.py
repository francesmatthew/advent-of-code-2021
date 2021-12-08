""""
File: day07.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-07-2021
Description: https://adventofcode.com/2021/day/07
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os
import statistics


def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day07.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input()
    if len(data_in) < 1:
        raise BadInputException()

    data = [int(d) for d in "".join(aoc_handler.get_input()).split(",")]
    median = abs(statistics.median(data))
    print(f"Linear Fuel Usuage: {P1(data,median)}")
    print(f"Exponential Fuel Usuage: {P2(data)}")


def P1(Data: list, med: int):
    return sum([abs(med - int(i)) for i in Data])


def P2(Data: list):
    best = None
    #iterate through all possible gas usuage combos
    for i in range(min(Data), max(Data)):
        #total gas usuage for this index
        total = 0
        #all the crabs in the data
        for subs in Data:
            #gas usage  per index
            gas_usage = abs(subs - i)
            #common summation rule
            #
            total += gas_usage * (gas_usage + 1) // 2
        if not best or total < best:
            best = total
    return best


if __name__ == "__main__":
    main()
