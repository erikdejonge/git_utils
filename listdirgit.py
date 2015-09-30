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


def print_line(lines):
    """
    @type line: str
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
    ld = os.listdir(arguments.rootpath)
    ld.append(os.path.basename(arguments.rootpath))

    if arguments.gitcommand == "status":
        not_git = []

        for i in ld:
            if i != os.path.basename(arguments.rootpath):
                td = os.path.join(arguments.rootpath, i)
            else:
                td = os.path.join(os.path.dirname(arguments.rootpath), i)

            if os.path.isdir(td):
                gp = os.path.join(td, os.path.join(".git"))

                if not os.path.exists(os.path.join(gp)):
                    not_git.append(os.path.dirname(gp))
                else:
                    result = os.popen("cd " + td + "&&git status ").read()

                    if "modified" in result or "new file" in result or "untracked" in result:
                        print("\n\033[91mchanged: " + os.path.dirname(gp), "\033[0m")
                        print_line(result.strip())

        print("\033[33m{}\033[0m".format(timestamp))

        if len(not_git) > 0:
            print("\n\033[31mNot git:\033[0m")

        for p in not_git:
            print("\033[31m", p, "\033[0m")


if __name__ == "__main__":
    main()
