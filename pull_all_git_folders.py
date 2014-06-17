#!/usr/bin/python
# -*- coding: utf-8 -*-
""" git checking script """

import os
import subprocess
import cPickle
findcnt = 0


def main():
    """
    main
    """
    dfp = "/cygdrive/d/workarea/git_utils/gitdirlist.pickle"

    if os.path.exists(dfp):
        dir_list = cPickle.load(open(dfp))
    else:
        raise RuntimeError("Cannot find /cygdrive/d/workarea/git_utils/gitdirlist.pickle")

    for folder in dir_list:
        print "\033[0mpull " + os.path.basename(folder) + "\033[0m", '\033[m'
        p = subprocess.Popen(["/usr/bin/git", "pull"], stdout=subprocess.PIPE, cwd=folder)
        p.wait()
        output = p.stdout.read()
        output = output.strip()

        if "Already up-to-date" in output:
            print "\033[96m" + os.path.basename(folder) + " up-to-date\033[0m"
        else:
            print "\033[93m" + output.strip() + "\033[0m"


if __name__ == "__main__":
    main()
