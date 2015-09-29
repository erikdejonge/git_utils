# coding=utf-8
"""
Print git status for folder <input> and all it's subfolders

Usage:
  listdirstatus [options] <gitcommand> <rootpath>

Options:
  -h --help     Show this screen.
  -r --recurse  Recurse the subfolders

Commands: status -> git status
          commit -> git commit -m [timestamp]

author  : rabshakeh (erik@a8.nl)
project : git_utils
created : 28-09-15 / 11:47
"""
import sys
import datetime
from arguments import Arguments
from consoleprinter import console

if sys.version_info.major < 3:
    console("\033[31mpython3 is required\033[0m")
    exit(1)


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.gitcommand = ""
        self.rootpath = ""

        super().__init__(doc)


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    print(str(arguments))
    timestamp = datetime.datetime.now().strftime("%A %d %B %Y (week;%W day;%j), %H:%M:%S").replace(";0", ":").replace(";", ":")
    print(timestamp)

if __name__ == "__main__":
    main()
