#!/usr/bin/env python3
# coding=utf-8
"""
Checks all gitfolders and optionally add new items

Usage:
  status_all_git_folders.py [options]

Options:
  -h --help     Show this screen.
  -n --newonly  Print only new items
  -l --list     Only list, no add actions
  -f --force    Do not ask for addition of files

author  : rabshakeh (erik@a8.nl)
project : git_utils
created : 04-06-15 / 14:32
"""
from __future__ import division, print_function, absolute_import, unicode_literals
from future import standard_library

import os
import pickle

from arguments import Arguments
from consoleprinter import query_yes_no


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.force = False
        self.newonly = False
        self.help = False
        self.list = False
        super().__init__(doc)


def check_branches(arg, currdir, dir_list, excludes, prstatus):
    """
    @type arg: IArguments
    @type currdir: str
    @type dir_list: list
    @type excludes: list
    @type prstatus: str
    @return: set
    """
    untrackedaction = set()

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            if os.path.exists(os.path.join(folder, ".git")):
                os.chdir(folder)
                print("folder", folder)
                # os.system("git rm --cached -r .idea/")
                for branch in os.popen("git branch").read().split("\n"):
                    if "*" in branch:
                        foldername = os.path.basename(folder)

                        if len(foldername) < 25:
                            foldername += (" " * (25 - len(foldername)))

                        if "master" not in branch:
                            if foldername.strip() not in excludes and os.path.join(os.path.expanduser("~") + "/workspace", foldername.strip()) not in excludes:
                                print("\033[31m--- attention: repos not checked out as master\n** " + folder + " \033[34m" + branch.replace("*", "").strip() + "\033[31m**\n---\033[0m")

                status = os.popen("git status").read()
                report(arg, folder, prstatus, status, untrackedaction)

            os.chdir(currdir)
        else:
            print("--", folder)
            print(excludes)

    return untrackedaction


def find_git_repos(arg, directory, files):
    """ find the git repositories
    :param arg:
    :param directory:
    :param files:
    """
    # noinspection PyUnusedLocal
    files = files
    git_dir = os.path.join(directory, ".git")

    if os.path.exists(git_dir):
        arg.append(directory)


def handle_new_items(arg, untrackedaction):
    """
    @type arg: IArguments
    @type untrackedaction: str
    @return: None
    """
    untrackedaction = list(untrackedaction)
    untrackedaction.sort(key=lambda x: len(str(x).split("\n")))

    if len(untrackedaction) > 0:
        if not arg.newonly and arg.list is False:
            if query_yes_no("execute add files commands?", force=arg.force):
                for filepointer in untrackedaction:
                    cmd = "cd " + filepointer + "; git add * 2> /dev/null"
                    print("\033[91madding:", filepointer, "\033[0m")
                    os.system(cmd)

        else:
            print("\n\033[34mNew files in folders:\033[0m")
            for filepointer in untrackedaction:
                print("\033[31m" + filepointer + "\033[0m")


def print_line(line, prstatus):
    """
    @type line: str
    @type prstatus: list
    @return: None
    """
    if "untracked files present" in line:
        prstatus[0] = ""
        print("\n\033[37m" + line + "\033[0m")
    elif "deleted:" in line or (prstatus[0] == "red" and not "git add <file>" in line):
        print("\033[31m" + line + "\033[0m")
    elif prstatus[0] == "red" and "git add <file>" in line:
        print("\033[37m" + line + "\033[0m\n")
    elif "Untracked files:" in line:
        prstatus[0] = "red"
        print("\033[37m" + line + "\033[0m")
    elif "new file:" in line:
        print("\033[32m" + line + "\033[0m")
    elif "modified:" in line:
        print("\033[91m" + line + "\033[0m")
    else:
        print("\033[37m" + line + "\033[0m")


def print_status(arg, status, prstatus):
    """
    @type arg: IArguments
    @type status: str, unicode
    @type prstatus: str, unicode
    @return: None
    """
    for line in status.strip().split("\n"):
        if len(line.strip()) == 0:
            continue

        if arg.newonly is False:
            print_line(line, prstatus)


def report(arg, folder, prstatus, status, untrackedaction):
    """
    @type arg: IArguments
    @type folder: str
    @type prstatus: list
    @type status: list
    @type untrackedaction: str
    @return: None
    """
    if not arg.newonly and "modified" in status or "Untracked" in status or "new file" in status or "deleted" in status:
        prstatus[0] = ""

        if "Untracked" in status:
            if arg.newonly is False:
                print("\033[95m---\033[0m")

        if arg.newonly is False:
            print("\033[33mstatus:", folder, "\033[0m")

        if "Untracked files" in status:
            print_status(arg, status, prstatus)
            untrackedaction.add(folder)
        elif "new file" in status:
            print_status(arg, status, prstatus)
        elif "deleted" in status:
            print_status(arg, status, prstatus)
        else:
            print_status(arg, status, prstatus)


def main():
    """
    main
    """
    arg = IArguments(__doc__)
    excludes = []
    prstatus = [""]

    # if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
    #     excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]
    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        excludes.extend([os.path.join(os.path.expanduser("~") + "/workspace", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp, "rb"))
        currdir = os.popen("pwd").read().strip()
    else:
        dir_list = []

        for root, dirlist, _ in os.walk("."):
            find_git_repos(dir_list, root, dirlist)

        currdir = os.popen("pwd").read().strip()
        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        pickle.dump(dir_list, open(dfp, "wb"))

    dir_list = [project_name for project_name in dir_list if "workspace/github" not in project_name]

    untrackedaction = check_branches(arg, currdir, dir_list, excludes, prstatus)
    handle_new_items(arg, untrackedaction)

standard_library.install_aliases()


if __name__ == "__main__":
    main()
