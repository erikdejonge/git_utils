#!/usr/bin/python
# -*- coding: utf-8 -*-
""" git checking script """
import os
import sys
import subprocess
import time
import cPickle
findcnt = 0


def find_git_repos(arg, directory, files):
    """ find the git repositories """
    global findcnt
    findcnt += 1

    if findcnt % 100 == 0:
        sys.stdout.write(".")
        sys.stdout.flush()

    git_dir = os.path.join(directory, ".git")

    if os.path.exists(git_dir):

        print "gitdir:", directory
        arg.append(directory)


def main():
    """
    main
    """



    dir_list = []
    os.path.walk("/Users/rabshakeh/workspace", find_git_repos, dir_list)
    print

    currdir = os.popen("pwd").read().strip()
    dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]

    procs = []


    for folder in dir_list:
        p = subprocess.Popen(["/usr/local/bin/git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
        procs.append({"folder": folder, "proc": p})
        print "\033[92mpull " + os.path.basename(folder) + "\033[0m"
        p.wait()

    for d in procs:
        p = d["proc"]
        p.wait()
        output = p.stdout.read()
        output += p.stderr.read()

        if "Already up-to-date" in output:
            pass
        else:
            print "\033[93m" + output.strip() + "\033[0m"

if __name__ == "__main__":
    main()
