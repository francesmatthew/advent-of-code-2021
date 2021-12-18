""""
File: day16.py
Authors: Matthew Frances, Nicholas Conn, Peter Scrandis
Date: 12-16-2021
Description: https://adventofcode.com/2021/day/16

Note: Python is really not good for this type of bitwise data handling.
    A solution in C would be much more elegant
"""
from AOCHandler import AOCHandler, BadInputException
import sys
import os

def hex_to_bin(data):
    bins = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "a": "1010",
        "b": "1011",
        "c": "1100",
        "d": "1101",
        "e": "1110",
        "f": "1111"
    }
    rstring = ""
    for char in data:
        rstring += bins[char.lower()]
    return rstring

def bin_to_int(data):
    rint = 0
    for char in data:
        rint *= 2
        rint += int(char)
    return rint

class Packet:
    SUM = 0
    PRODUCT = 1
    MINIMUM = 2
    MAXIMUM = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7
    OPERATION = {
        SUM: lambda a, b: a + b,
        PRODUCT: lambda a, b: a * b,
        MINIMUM: lambda a, b: a if a <= b else b,
        MAXIMUM: lambda a, b: a if a >= b else b,
        GREATER_THAN: lambda a, b: int(a > b),
        LESS_THAN: lambda a, b: int(a < b),
        EQUAL_TO: lambda a, b: int(a == b)
    }

    def __init__(self, bin_data):
        """
        Parse binary data into a packet
        """
        self.size = 0
        self.raw = bin_data
        self.version = bin_to_int(self.raw[0:3])
        self.ptype = bin_to_int(self.raw[3:6])
        if self.ptype == self.LITERAL:
            self.value = 0
            index = 6 # starting index for the next 5-bit binary data
            while True:
                # "ABBBB": For each group of 5 bits, "B" bits are the BCD of the literal value...
                # ...and the "A" bit is 0 when this is the last literal in this packet
                self.value *= 16
                self.value += bin_to_int(self.raw[index+1:index+5])
                if self.raw[index] == "0": break
                else: index += 5
            self.size = index + 5
        else:
            self.sub_packets = []
            self.ltype = bin_to_int(self.raw[6])
            if self.ltype:
                # 11-bit number of sub-packets
                self.payload_len = bin_to_int(self.raw[7:18])
                index = 18
                for _ in range(self.payload_len):
                    sub_packet = Packet(self.raw[index:])
                    self.sub_packets.append(sub_packet)
                    index += len(sub_packet)
                self.size = index
            else:
                # 15-bit number of bits
                self.payload_len = bin_to_int(self.raw[7:22])
                index = 22
                while (index - 22) < self.payload_len:
                    sub_packet = Packet(self.raw[index:])
                    self.sub_packets.append(sub_packet)
                    index += len(sub_packet)
                self.size = index

    def __len__(self):
        return self.size

    def __str__(self, depth:int = 0):
        rstring = ("    " * depth) + f"Length: {self.size} Version: {self.version}. Type: {self.ptype}."
        if self.ptype == self.LITERAL:
            rstring += f" Value: {self.value}"
        else:
            rstring += f" Payload Type: {self.ltype}. Payload Length: {self.payload_len}. Payload:"
            for packet in self.sub_packets:
                rstring += '\n' + packet.__str__(depth = depth + 1)
        return rstring

    def get_sum_versions(self):
        if self.ptype == self.LITERAL:
            return self.version
        else:
            return self.version + sum([p.get_sum_versions() for p in self.sub_packets])

    def get_value(self):
        if self.ptype == self.LITERAL:
            return self.value
        else:
            val = self.sub_packets[0].get_value()
            for i in range(1, len(self.sub_packets)):
                a = self.sub_packets[i].get_value()
                val = self.OPERATION[self.ptype](val, a)
        return val

def main():
    # get I/O identifier from command-line argument
    if len(sys.argv) < 2:
        print("Useage: python3 ./python/day16.py <I/O file identifier>")
        return
    aoc_handler = AOCHandler(sys.argv[1])

    data_in = aoc_handler.get_input()
    if len(data_in) < 1:
        raise BadInputException()

    # parse input data
    packet = Packet(hex_to_bin(data_in[0]))
    print(packet)

    solution1 = packet.get_sum_versions()
    solution2 = packet.get_value()

    aoc_handler.write_output(solution1, solution2, verbose=True)

if __name__ == '__main__':
    main()