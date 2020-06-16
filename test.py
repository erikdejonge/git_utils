#!/usr/bin/env python3
# coding=utf-8
"""
Project git_utils

Usage:
  test.py [options]

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : git_utils
created : 16 Jun 2020 / 12:17
where   : Latitude: 51.825382
Longitude: 4.651071

Accuracy (m): 65.000000
Timestamp: 16/06/2020, 12:17:09 CEST
"""
import sys
import pickle
from arguments import Arguments
from consoleprinter import console

if sys.version_info.major < 3:
    console("Python 3 is required", color="red", plaintext="True")
    exit(1)


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    if arguments.help:
        print("prints contents of gitdirlist.pickle")
        return
    data = pickle.load(open('gitdirlist.pickle', "rb"))
    for i in data:
        print(i)

if __name__ == "__main__":
    main()
