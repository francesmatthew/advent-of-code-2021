""""
File: day10.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-10-2021
Description: https://adventofcode.com/2021/day/10
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

OBRACKETS = ['[','{','(','<']
CBRACKETS = [']','}',')','>']

def p1(data):
    errors = 0
    errors2 = []
    for line in data:
        string = []
        for i in line:
            if i in OBRACKETS:
                string.append(i)
            elif i in CBRACKETS:
                if i == ')':
                    if string[-1] == '(':
                        string.pop()   
                    else:
                        errors += 3
                        string = []
                        break
                elif i == ']':
                    if string[-1] == '[':
                        string.pop()
                    else:
                        errors += 57
                        string = []
                        break
                elif i == '}':
                    if string[-1] == '{':
                        string.pop()
                    else:
                        errors += 1197
                        string = []
                        break
                elif i == '>':
                    if string[-1] == '<':
                        string.pop()
                    else:
                        errors += 25137
                        string = []
                        break
        if string:
            errors2.append(p2(string))
    errors2 = sorted(errors2)
    print(errors2)
    print(errors2[(len(errors2) // 2)])
    return(errors)
    pass

def p2(data):
    total = 0;
    while data:
        total *= 5
        if data[-1] == '(':
            total += 1
        elif data[-1] == '[':
            total += 2
        elif data[-1] == '{':
            total += 3
        elif data[-1] == '<':
            total += 4
        data.pop()
    return(total)
    pass

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day10.py <I/O file identifier>")
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