#!/usr/bin/python
# -*- coding: utf-8 -*-
""" git checking script """

import os
import sys
import subprocess
import time
import cPickle

findcnt = 0


def main():
    """
    main
    """
    dfp = "/Users/rabshakeh/workspace/git_utils/gitdirlist.pickle"

    if os.path.exists(dfp):
        dir_list = cPickle.load(open(dfp))
    else:
        raise RuntimeError("Cannot find /Users/rabshakeh/workspace/git_utils/gitdirlist.pickle")

    for folder in dir_list:
        print "pull_all_git_folders.py:26", folder
        p = subprocess.Popen(["/usr/local/bin/git", "pull"], cwd=folder)
        p.wait()


if __name__ == "__main__":
    main()
