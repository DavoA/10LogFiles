#!usr/bin/python3
"""
I used os and datetime modules
"""
import os
from datetime import datetime

def creating_files():
    """
    This is for creating files
    """
    for i in range(10):
        now = datetime.now()
        tmp = (str(now.year), str(now.month), str(now.day), str(now.hour), str(now.minute), str(now.second), str(now.microsecond))
        fname = "_".join(tmp)
        if now.microsecond % 2 == 0:
            stat = "Pass"
        else:
            stat = "Fail"
        with open(fname + ".log", "w") as f:
            f.write(fname + " --> Status: " + stat)

def main():
    """
    This is the main
    """
    directory = "tests"
    os.mkdir(directory)
    os.chdir(directory)
    creating_files()
main()
