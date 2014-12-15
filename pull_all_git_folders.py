#!/usr/bin/python
# -*- coding: utf-8 -*-
""" git checking script """

import os
import sys
import subprocess
import time
import cPickle
from optparse import OptionParser

findcnt = 0


def main():
    """
    main
    """
    parser = OptionParser()
    parser.add_option("-i", "--ignoregithub", help="Ignore paths with github in it", action="store_true")
    (options, args) = parser.parse_args()
    dfp = "/Users/rabshakeh/workspace/git_utils/gitdirlist.pickle"

    if os.path.exists(dfp):
        dir_list = cPickle.load(open(dfp))
    else:
        raise RuntimeError("Cannot find /Users/rabshakeh/workspace/git_utils/gitdirlist.pickle")

    procs = []

    for folder in dir_list:
        if options.ignoregithub is True and "github" in folder:
            pass
        else:
            print "pull_all_git_folders.py:35", "pull", folder
            p = subprocess.Popen(["/usr/local/bin/git", "pull"], cwd=folder)
            procs.append(p)

        if len(procs) > 20:
            for p in procs:
                p.communicate()
            procs = []

    for p in procs:
        p.communicate()


if __name__ == "__main__":
    main()
