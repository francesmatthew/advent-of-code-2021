"""
File: templateGenerator.py
Authors: Matthew Frances, Nicholas Conn
Date: 11-30-2021
Description: Create files for each puzzle according to a template
"""
import os
from sys import argv

TEMPLATE_DIR = ".template"
DAY_REPLACE_KEY = "{day}"
# the first element in each array should match the dir name under the template dir
PYTHON = ["python", "py"]
CPP = ["cpp", "c++"]

def replace_text(text, args):
    """
    Replace patterns in a string with given values
    params:
        text: string to be modified
        args: list of (key, value) tuples, where key is the pattern to match...
              in text and value is what replaces it
    return:
        text parameter after replacing each key with its corresponding value
    """
    for (key, value) in args:
        text = text.replace(key, value)
    return text

def copy_template_file(src_dir_name, dest_dir_name, src_file_name, *args):
    """
    Copy template files, filling in templated information where able
    Will match templated information in file name and file contents
    params:
        src_dir_name: string folder path where template file is
        dest_dir_name: string folder path where template file will be copied
        src_file_name: string name of file located in source directory
        args: any number of (key, value) tuples, where key is the pattern to match...
              in the file and value is what replaces it
    """
    dest_file_name = replace_text(src_file_name, args)
    src = f"{src_dir_name}/{src_file_name}"
    dest = f"{dest_dir_name}/{dest_file_name}"
    # check that the file doesn't exist already before overwriting
    if (os.path.exists(dest)):
        print(f"File {dest} already exists, aborting")
        return
    # read in the file data and fill in the information for the day
    with open(src, 'r') as template:
        file_data = template.read()
        file_data = replace_text(file_data, args)
        with open(dest, "w") as destination:
            destination.write(file_data)

def generate_new_day():
    """
    Copy template files for a given programming language on a given day
    Arguments are given by command-line argument
    """
    # get the day from argv
    if (len(argv) < 3):
        print("Useage: python3 templateGenerator.py <day> <language>")
        return
    # use f-strings to assure the day will be two digits with a leading 0
    day = f"{int(argv[1]):02d}"
    # resolve what language to copy
    lang = "none"
    for lang_const in (PYTHON, CPP):
        if (argv[2] in lang_const):
            lang = lang_const[0]
    if (lang == "none"):
        print(f"Invalid language {argv[2]}")
        return

    # create the target dir
    new_dir_name = f"day{day}"
    if not(os.path.exists(new_dir_name)):
        os.mkdir(new_dir_name)
    # create the new sub-directory according to the desired language
    new_dir_name = new_dir_name + '/' + lang
    if not(os.path.exists(new_dir_name)):
        os.mkdir(new_dir_name)

    # copy each file from the template directory into the target directory
    template_dir_name = TEMPLATE_DIR + '/' + lang
    for file_name in os.listdir(template_dir_name):
        copy_template_file(template_dir_name, new_dir_name, file_name, (DAY_REPLACE_KEY, day))


if __name__ == "__main__":
    generate_new_day()