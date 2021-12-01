"""
File: AOCHandler.py
Authors: Matthew Frances, Nicholas Conn
Date: 11-30-2021
Description: Handle program input and output on the filesystem
"""
import os

class AOCHandler:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def get_input(self):
        # Return a list string from the input file, newline-delimited
        with open(self.input_file, 'r') as input:
            raw_input = input.read()
            raw_input = raw_input.replace('\r', '') # remove all carriage returns
            return raw_input.split('\n',-1)

    def write_output(self, solution):
        # Write the string `solution` to the output file
        with open(self.output_file, 'w') as output:
            output.write(solution)
            return
