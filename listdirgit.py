#!/usr/bin/env python3
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
import os
import sys
import datetime

from arguments import Arguments
from consoleprinter import console, query_yes_no

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


def print_line(lines):
    """
    @type lines: str
    @return: None
    """
    for line in lines.split("\n"):
        if "untracked files present" in line:
            print("\n\033[37m" + line + "\033[0m")
        elif "deleted:" in line:
            print("\033[31m" + line + "\033[0m")
        elif "git add <file>" in line:
            print("\033[37m" + line + "\033[0m\n")
        elif "Untracked files:" in line:
            print("\033[37m" + line + "\033[0m")
        elif "new file:" in line:
            print("\033[32m" + line + "\033[0m")
        elif "modified:" in line:
            print("\033[91m" + line + "\033[0m")
        else:
            print("\033[37m" + line + "\033[0m")


def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    timestamp = datetime.datetime.now().strftime("%A %d %B %Y (week;%W day;%j), %H:%M:%S").replace(";0", ":").replace(";", ":")

    if not os.path.isdir(arguments.rootpath):
        console(arguments.rootpath, " is not a folder", color="red")
        return

    gitdirs = []
    lg = os.walk(arguments.rootpath)
    for i in lg:

        if i[0].lower().endswith(".git"):
            gitdirs.append(i[0])

    if arguments.gitcommand == "status":
        for gd in gitdirs:
            result = os.popen("cd " + os.path.dirname(gd) + "&&git status ").read()

            if "modified" in result or "new file" in result or "untracked" in result:
                print("\n\033[91mchanged: " + os.path.dirname(gd), "\033[0m")
                print_line(str(result).strip())

    elif arguments.gitcommand == "gitreset":
        if query_yes_no("are you sure?"):
            for gd in gitdirs:
                print(gd)
                os.system("cd " + os.path.dirname(gd) + "&&git reset --hard origin/master; git clean -f")
    elif arguments.gitcommand == "gconf":

            for gd in gitdirs:
                os.system("cd " + os.path.dirname(gd) + "&&git status")
    elif arguments.gitcommand == "pull":

            for gd in gitdirs:
                os.system("cd " + os.path.dirname(gd) + "&&git pull")

    print("\033[33m{}\033[0m".format(timestamp))


if __name__ == "__main__":
    main()
