""""
File: day10.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 12-10-2021
Description: https://adventofcode.com/2021/day/10
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os


BRACKETS = [ ('(',')'), ('[',']'), ('<','>'), ('{','}') ]
LEFT = ['(', '[', '<', '{']
RIGHT = [')',']','>','}']
P1_SCORE = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}
P2_SCORE = {
    '(':1,
    '[':2,
    '{':3,
    '<':4
}

class BadClosedException(Exception):
    def __init__(self, rbrak, msg=""):
        # rbrak is the closed bracket that was not expected
        self.rbrak = rbrak
        super().__init__(self, msg)

def p1(data):
    invalid = {}
    # operate on copy of data, list is modified during loop
    for line in data[:]:
        # maintain a stack of all opened brackets, in ordered...
        # ...last element in stack is most recently opened bracket...
        # ...closing brackets must match that last opened bracket
        opened_stack = []
        try:
            for char in line:
                if char in LEFT:
                    # push open bracket onto stack
                    opened_stack.append(char)
                elif char in RIGHT:
                    # pop last opened bracket off stack and...
                    # ...check if it matches this closing bracket
                    last_brak = opened_stack.pop()
                    for bracket_pair in BRACKETS:
                        if (char in bracket_pair) and (last_brak not in bracket_pair):
                            raise BadClosedException(char)
        except BadClosedException as e:
            # closing bracket did not match
            count = invalid.get(e.rbrak, 0)
            count += 1
            invalid[e.rbrak] = count
            # remove invalid line from data for part 2
            data.remove(line)

    # calculate score
    score = 0
    for rbrak, count in invalid.items():
        score += P1_SCORE[rbrak] * count
    return score

def p2(data):
    line_scores = [] # maintain scores for each line
    for line in data[:]:
        # solution is similar to part 1
        opened_stack = []
        for char in line:
            if char in LEFT:
                opened_stack.append(char)
            elif char in RIGHT:
                opened_stack.pop()
        line_score = 0
        # calculate this line score by finding the sequence of brackets required the currently...
        # ...opened brackets on the stack
        # iterate through list in reverse order (use list.pop())
        for _ in range(len(opened_stack)):
            char = opened_stack.pop()
            line_score *= 5
            line_score += P2_SCORE[char]
        line_scores.append(line_score)
    # calc final score
    line_scores.sort()
    middle_i = len(line_scores) // 2
    return line_scores[middle_i]

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day10.py <I/O file identifier>")
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