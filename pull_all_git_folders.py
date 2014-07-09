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

    procs = []
    cnt = 0
    for folder in dir_list:
        p = subprocess.Popen(["/usr/local/bin/git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
        procs.append({"folder": folder, "proc": p})

        print "\033[92mpull " + os.path.basename(folder) + "\033[0m"
        if cnt > 2:
            p.wait()
            cnt = 0
        else:
            cnt += 1


    for d in procs:
        p = d["proc"]
        p.wait()
        output = p.stdout.read()
        output = output.strip()
        #output += p.stderr.read()
        #output = output.strip()
        if "Already up-to-date" in output:
            print "\033[90m"+os.path.basename(d["folder"])+" up-to-date\033[0m"
        else:
            print "\033[93m" + os.path.basename(d["folder"]) + " updated *\n" + output.strip() + "\033[0m"


if __name__ == "__main__":
    main()
