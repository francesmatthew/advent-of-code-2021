""""
File: day14.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 12-14-2021
Description: https://adventofcode.com/2021/day/14
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

def p1(poly_template, rules):
    polymer = list(poly_template)
    poly_dict = apply_rules(polymer, rules, 10)
    return calc_score(poly_dict, poly_template)

def p2(poly_template, rules):
    polymer = list(poly_template)
    poly_dict = apply_rules(polymer, rules, 40)
    return calc_score(poly_dict, poly_template)

def calc_score(polymer, poly_template):
    counts = count_chars(polymer, poly_template)
    max_count = None
    min_count = None
    # keep track of the greatest and smallest counts
    for count in counts.values():
        if max_count is None or count > max_count:
            max_count = count
        if min_count is None or count < min_count:
            min_count = count
    return max_count - min_count

def apply_rules(polymer, rules, ntimes):
    # match rules based on dictionary keys
    rule_dict = {}
    for lmatch, rmatch, middle in rules:
        rule_dict[ lmatch + rmatch ] = middle

    # store polymer as a count of pairs, rules operate on entire pairs
    poly_dict = { }
    for i in range(len(polymer) - 1):
        count = poly_dict.get(polymer[i] + polymer[i+1], 0)
        count += 1
        poly_dict[polymer[i] + polymer[i+1]] = count

    for n in range(ntimes):
        for pair, count in poly_dict.copy().items():
            if pair in rule_dict:
                poly_dict[pair] -= count
                lcount = poly_dict.get(pair[0] + rule_dict[pair], 0) + count
                rcount = poly_dict.get(rule_dict[pair] + pair[1], 0) + count
                poly_dict[pair[0] + rule_dict[pair]] = lcount
                poly_dict[rule_dict[pair] + pair[1]] = rcount
        # for i in range(len(polymer) - 1):
        #     new_polymer.append(polymer[i])
        #     if (polymer[i], polymer[i+1]) in rule_dict:
        #         # include the new character in between the two characters
        #         new_polymer.append(rule_dict[ (polymer[i], polymer[i+1]) ])
        # new_polymer.append(polymer.pop()) # keep the last element
        # polymer = new_polymer
    return poly_dict


def count_chars(poly_dict, poly_template):
    counts = {}
    for pair, pcount in poly_dict.items():
        for char in pair:
            ccount = counts.get(char, 0)
            ccount += pcount
            counts[char] = ccount
    # each item is double-counted except for the first and last elements
    counts[poly_template[0]] += 1
    counts[poly_template[-1]] += 1
    for char, count in counts.items():
        counts[char] = count // 2
    return counts

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day14.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input_raw()
    if len(data_in) < 1:
        raise BadInputException()

    # parse input data
    poly_template, rules_in = data_in.split("\n\n")
    rules_in = rules_in.split("\n")
    rules  = []
    for rule in rules_in:
        l,r  = rule.split(" -> ")
        rules.append( (l[0], l[1], r) )

    solution1 = p1(poly_template, rules)
    solution2 = p2(poly_template, rules)

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()