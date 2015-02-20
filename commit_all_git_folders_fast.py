# coding=utf-8

# -*- coding: utf-8 -*-
""" git checking script """

import os
import sys
# noinspection PyPep8Naming
import cPickle as pickle
import subprocess


def main():
    """ check all folders and pull all from the server """
    excludes = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp))
    else:
        raise RuntimeError("Cannot find " + os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    msg = os.popen("date").read().strip()

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            print folder

        if os.path.basename(folder) not in excludes and 4==2:
            p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am",  msg], stdout=subprocess.PIPE, cwd=folder)
            output, se = p.communicate()

            if "nothing to commit" in output:
                sys.stdout.write(".")
                sys.stdout.flush()
            else:
                print
                print "\033[92mcommit "+os.path.basename(folder)+"\033[0m\n\033[93m"+output.strip()+"\033[0m"

    print excludes


if __name__ == "__main__":
    main()
