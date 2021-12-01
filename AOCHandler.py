"""
File: AOCHandler.py
Authors: Matthew Frances, Nicholas Conn
Date: 11-30-2021
Description: Handle program input and output on the filesystem
"""

class AOCHandler:
    BAD_INPUT_LINES = ['']

    def __init__(self, input_file_name, output_file_name):
        """
        Initalize Advent of Code Handler with input and output filenames
        """
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def get_input(self):
        """
        Return a list string from the input file, newline-delimited
        """
        with open(self.input_file_name, 'r') as input_file:
            input = input_file.read()
            input = input.replace('\r', '') # remove all carriage returns
            input = input.split('\n', -1)
        # remove empty strings (caused by trailing newline chars)
        # must iterate from last-to-first when removing elements in-place
        for index in range( (len(input)-1), -1, -1):
            if input[index] in self.BAD_INPUT_LINES:
                del input[index]
        return input

    def get_input_int(self):
        """
        Specialization of get_input() that returns a list of ints from the input file,
        newline-delimited
        This function may raise errors if input cannot be represented as an int
        """
        input_list = self.get_input()
        for i in range(len(input_list)):
            input_list[i] = int(input_list[i])
        return input_list

    def write_output(self, *args, **kwargs):
        """
        Write one or more arguments to the output file, one line per argument
        Arguments must support conversion to string
        kwargs:
            verbose: (boolean) also print arguments to terminal
        """
        # default value for verbosity
        if 'verbose' not in kwargs:
            kwargs['verbose'] = False

        with open(self.output_file_name, 'w') as output:
            for arg in args:
                arg = str(arg)
                output.write(arg + '\n')
                if kwargs['verbose']:
                    print(arg)
            return