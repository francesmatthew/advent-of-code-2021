"""
File: templateGenerator.py
Authors: Matthew Frances, Nicholas Conn
Date: 11-30-2021
Description: Create python files for each puzzle according to a template
"""
import os
from sys import argv

TEMPLATE_FILE = "template.txt"

def generate_new_file():
    # get the day from argv
    if (len(argv) < 2):
        print("Useage: python3 templateGenerator.py <day>")
        return
    # use f-strings to assure the day will be two digits with a leading 0
    day = f"{int(argv[1]):02d}"

    # create the directory
    new_dir_name = f"day{day}"
    if not(os.path.exists(new_dir_name)):
        os.mkdir(new_dir_name)
    # read in the template data and fill in the information for the day
    with open(TEMPLATE_FILE, 'r') as template:
        file_data = template.read()
        file_data = file_data.replace("{day}", day)
        # check that the file doesn't exist already before overwriting
        new_file_name = f"day{day}/day{day}.py"
        if (os.path.exists(new_file_name)):
            print(f"File {new_file_name} already exists, aborting")
            return
        with open(new_file_name, "w") as destination:
            destination.write(file_data)


if __name__ == "__main__":
    generate_new_file()