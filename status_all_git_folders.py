# coding=utf-8
# -*- coding: utf-8 -*-
""" git checking script """
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

import os

# noinspection PyPep8Naming
import pickle as pickle


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


def print_status(status, prstatus):
    """
    @type status: str, unicode
    @type prstatus: str, unicode
    @return: None
    """
    for line in status.strip().split("\n"):
        if "untracked files present" in line:
            prstatus[0] = ""
            print("\033[90m" + line + "\033[0m")
        elif "deleted:" in line:
            print("\033[35m" + line + "\033[0m")
        elif prstatus[0] == "red" and not "git add <file>" in line:
            print("\033[31m" + line + "\033[0m")
        elif "Untracked files:" in line:
            prstatus[0] = "red"
            print("\033[37m" + line + "\033[0m")
        elif "modified:" in line:
            print("\033[32m" + line + "\033[0m")
        else:
            print("\033[90m" + line + "\033[0m")




def main():
    """ check all folders and pull all from the server """
    excludes = []
    prstatus = [""]

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        excludes.extend([os.path.join(os.path.expanduser("~") + "/workspace", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp, "rb"))
        currdir = os.popen("pwd").read().strip()
    else:
        dir_list = []

        for root, dirlist, file in os.walk("."):
            find_git_repos(dir_list, root, dirlist)

        currdir = os.popen("pwd").read().strip()
        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        pickle.dump(dir_list, open(dfp, "wb"))

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            os.chdir(folder)

            # os.system("git rm --cached -r .idea/")
            for branch in os.popen("git branch").read().split("\n"):
                if "*" in branch:
                    fl = os.path.basename(folder)

                    if len(fl) < 25:
                        fl += (" " * (25 - len(fl)))

                    if "master" not in branch:
                        if fl.strip() not in excludes and os.path.join(os.path.expanduser("~") + "/workspace", fl.strip()) not in excludes:
                            print(fl + "\t" + branch.replace("*", "").strip())

            status = os.popen("git status").read()

            if "modified" in status or "Untracked" in status or "new file" in status or "deleted" in status:
                prstatus[0] = ""
                print("\033[36mstatus:", folder, "\033[0m")

                if "new file" in status:
                    print_status(status, prstatus)

                if "deleted" in status:
                    print_status(status, prstatus)
                else:
                    print_status(status, prstatus)

            os.chdir(currdir)


if __name__ == "__main__":
    main()
