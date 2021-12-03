""""
File: day03.py
Authors: Matthew Frances, Nicholas Conn
Date: 12-03-2021
Description: https://adventofcode.com/2021/day/3
"""
from AOCHandler import AOCHandler
import sys
import os

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day03.py <I/O file identifier>")
        return
    # enter matt,nick,example to choose input
    aoc_handler = AOCHandler(sys.argv[1])
    # returns data as list of strings
    data_in = aoc_handler.get_input()
    if len(data_in) < 1:
        print("No data")
        return

    # To find gamma and epsilon values:
    # -Each bit in the gamma rate can be determined by finding
    # the most common bit in the corresponding position of all numbers
    # in the input
    # -Epsilon is the same process, except each bit is the least common bit
    # in the corresponding position...

    # find out the number of bits per entry
    num_bits = len(data_in[0])

    gamma_str = ""
    epsilon_str = ""

    for i in range(num_bits):
        common_bit = find_most_common_bit(data_in, i)
        gamma_str += str(common_bit)
        epsilon_str += str(common_bit ^ 1) # flip the bit

    gamma = bin_to_int(gamma_str)
    epsilon = bin_to_int(epsilon_str)

    # To find O2 and CO2 ratings:
    # -Keep only numbers selected by the bit criteria for the type of rating value
    # for which you are searching. Discard numbers which do not match the bit criteria.
    # -If you only have one number left, stop; this is the rating value for which you are searching.
    # -Otherwise, repeat the process, considering the next bit to the right.

    # list comprehension selects all elements that match the bit criteria
    # most common first digit is already determined, stored in gamma
    oxygen_data = [num for num in data_in if num[0] == gamma_str[0]]
    i = 1
    while( (len(oxygen_data) > 1) and (i < num_bits) ):
        select_bit = find_most_common_bit(oxygen_data, i)
        oxygen_data = [num for num in oxygen_data if int(num[i]) == select_bit]
        i += 1

    carbon_data = [num for num in data_in if num[0] != gamma_str[0]]
    i = 1
    while( (len(carbon_data) > 1) and (i < num_bits) ):
        select_bit = find_most_common_bit(carbon_data, i)
        carbon_data = [num for num in carbon_data if int(num[i]) != select_bit]
        i += 1

    # convert the remaining entry into decimal
    oxygen_rating = bin_to_int(oxygen_data[0])
    carbon_rating = bin_to_int(carbon_data[0])

    #writes to output directory, if verbose = True, print to console
    aoc_handler.write_output(epsilon*gamma, oxygen_rating*carbon_rating, verbose=True)


def find_most_common_bit(data_list, index):
    """
    data_list is a list of BCD strings
    index is an int of what bit position to search in each BCD string
    return data is an int of the most common bit at that index
    If 1's and 0's are equally common, return is 1
    """
    # determine if 1 or 0 is more common by comparing the...
    # ...count of entires with 1's in the given bit position to...
    # ...half of the total number of entries
    # ...ie. if 7 out of 12 entries have '1' as the first digit...
    # ...then 1 is more common than 0 as a first digit
    one_count = 0
    for line in data_list:
            if (line[index] == "1"):
                one_count += 1
    half_len = len(data_list) / 2.0
    return int(one_count >= half_len)


def bin_to_int(bin_str):
    """
    convert string of binary digits to integer
    """
    return_int = 0
    highest_two_power = len(bin_str) - 1
    for i in range(len(bin_str)):
        if bin_str[i] == "1":
            return_int += 2**(highest_two_power - i)

    return return_int


if __name__ == '__main__':
    main()
