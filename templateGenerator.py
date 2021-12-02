"""
File: templateGenerator.py
Authors: Matthew Frances, Nicholas Conn
Date: 11-30-2021
Description: Create files for each puzzle according to a template
"""
import os
import sys
from distutils.dir_util import copy_tree


LANGUAGE = "python"
PATH = "./solutions/day"
KEY = "{day}"

if not sys.argv[1]:
    print("try running with 'python3 ./templateGenerator.py <day>")
    sys.exit()
else:
    CURRENT_DAY = f"{int(sys.argv[1]):02d}"


def generate_directory():
    #Check if valid templates exist
    if(os.path.exists("./.templates")):
        #copy template to solutions folder

        if not os.path.exists(f"./solutions/day{CURRENT_DAY}"):
            copy_tree("./.templates", "./solutions")
            #rename templated day to current day
            os.rename(PATH+"{day}", f"{PATH}{CURRENT_DAY}")
            PY_PATH = PATH+f"{CURRENT_DAY}{LANGUAGE}\day"
            os.rename(f"./solutions/day{CURRENT_DAY}/python/day{{day}}.py",f"./solutions/day{CURRENT_DAY}/python/day{CURRENT_DAY}.py")
            #open file in directory, and replace '{day}' with current day
            with open(f"./solutions/day{CURRENT_DAY}/python/day{CURRENT_DAY}.py") as r:
                #read into string
                template = r.read()
                #replace with current day
                template = template.replace(KEY, str(CURRENT_DAY))
                #clear and rewrite with proper date
                with open(f"./solutions/day{CURRENT_DAY}/python/day{CURRENT_DAY}.py", 'w') as f:
                    f.write(template)
        else:
            print("Cannot overwrite previous day")
            return
    else:
        print("No template file found")
        return


if __name__ == '__main__':
    generate_directory()
