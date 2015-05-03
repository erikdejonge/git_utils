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
import sys

# noinspection PyPep8Naming
import pickle as pickle


def query_yes_no_quit(question, default="yes"):
    """
    @type question: str
    @type default: str
    @return: None
    """
    valid = {"yes": "yes", "y": "yes", "ye": "yes",
             "no": "no", "n": "no",
             "quit": "quit", "qui": "quit", "qu": "quit", "q": "quit"}

    if default is None:
        prompt = " [y/n/q] "
    elif default == "yes":
        prompt = " [Y/n/q] "
    elif default == "no":
        prompt = " [y/N/q] "
    elif default == "quit":
        prompt = " [y/n/Q] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()

        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes', 'no' or 'quit'.\n")


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
        if len(line.strip()) == 0:
            continue

        if "untracked files present" in line:
            prstatus[0] = ""
            print("\n\033[90m" + line + "\033[0m")
        elif "deleted:" in line:
            print("\033[31m" + line + "\033[0m")
        elif prstatus[0] == "red" and "git add <file>" in line:
            print("\033[37m" + line + "\033[0m\n")
        elif prstatus[0] == "red" and not "git add <file>" in line:
            print("\033[31m" + line + "\033[0m")
        elif "Untracked files:" in line:
            prstatus[0] = "red"
            print("\033[37m" + line + "\033[0m")
        elif "new file:" in line:
            print("\033[32m" + line + "\033[0m")
        elif "status:" in line:
            print("\033[90m" + line + "\033[0m")
        elif "modified:" in line:
            print("\033[91m" + line + "\033[0m")
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

    foundsomething = False
    first = True
    untrackedaction = set()

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            if os.path.exists(os.path.join(folder, ".git")):
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
                    foundsomething = True
                    prstatus[0] = ""

                    if "Untracked" in status:
                        print("\033[95m---\033[0m")
                    print("\033[33mstatus:", folder, "\033[0m")


                    if "Untracked files" in status:
                        print_status(status, prstatus)
                        untrackedaction.add(folder)

                    elif "new file" in status:
                        print_status(status, prstatus)
                    elif "deleted" in status:
                        print_status(status, prstatus)
                    else:
                        print_status(status, prstatus)

            os.chdir(currdir)

    untrackedaction = list(untrackedaction)
    untrackedaction.sort(key=lambda x: len(str(x).split("\n")))

    if len(untrackedaction) > 0:
        if "yes" is query_yes_no_quit("execute add files commands?"):
            for fp in untrackedaction:
                cmd = "cd " + fp + "; git add * 2> /dev/null"
                print("\033[91madding:", fp, "\033[0m")
                os.system(cmd)


if __name__ == "__main__":
    main()
