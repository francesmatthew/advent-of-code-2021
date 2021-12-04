"""
File: AOCHandler.py
Authors: Matthew Frances, Nicholas Conn
Date: 11-30-2021
Description: Handle program input and output on the filesystem
"""

class BadInputException(Exception):
    def __init__(self, message="Bad AOC Input"):
        super().__init__(message)

class AOCHandler:
    BAD_INPUT_LINES = ['']
    INPUT_FILE_FORMAT = "inputs/<id>-input.txt"
    OUTPUT_FILE_FORMAT = "outputs/<id>-output.txt"

    def __init__(self, identifier):
        """
        Initalize Advent of Code Handler with input and output filenames
        """
        self.input_file_name = self.INPUT_FILE_FORMAT.replace("<id>", identifier)
        self.output_file_name = self.OUTPUT_FILE_FORMAT.replace("<id>", identifier)

    def get_input(self):
        """
        Return a list string from the input file, newline-delimited
        """
        with open(self.input_file_name, 'r') as input_file:
            data_in = input_file.read()
            data_in = data_in.replace('\r', '')  # remove all carriage returns
            data_in = data_in.split('\n', -1)
        # remove empty strings (caused by trailing newline chars)
        return [i for i in data_in if i not in self.BAD_INPUT_LINES]

    def get_input_raw(self):
        """
        Return a string dump of the entire input file contents
        """
        with open(self.input_file_name, 'r') as input_file:
            data_in = input_file.read()
            data_in = data_in.rstrip() # remove trailing newline
        return data_in

    def get_input_int(self):
        """
        Specialization of get_input() that returns a list of ints from the input file,
        newline-delimited
        This function may raise errors if input cannot be represented as an int
        """
        return [int(i) for i in self.get_input()]

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

        with open(self.output_file_name, 'w') as data_out:
            for arg in args:
                arg = str(arg)
                data_out.write(arg + '\n')
                if kwargs['verbose']:
                    print(arg)
            return
