#!/usr/bin/python
# -*- coding: utf-8 -*-
""" git checking script """
import os
import sys
import subprocess
import time
import cPickle


def find_git_repos(arg, directory, files):
    """
    @type arg: str
    @type directory: str
    @type files: str
    """

    disp = directory.replace("/Users/rabshakeh/workspace/", "")[:100]

    if len(disp) < 100:
        disp += " " * (100 - len(disp))

    sys.stdout.write(disp+"\r")
    sys.stdout.flush()
    git_dir = os.path.join(directory, ".git")

    if os.path.exists(git_dir):
        arg.append(directory)


def main():
    """
    main
    """
    if os.path.exists("/Users/rabshakeh/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open("/Users/rabshakeh/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]
    dfp = "/Users/rabshakeh/workspace/git_utils/gitdirlist.pickle"

    if os.path.exists(dfp):
        dir_list = cPickle.load(open(dfp))
    else:
        dir_list = []
        os.path.walk(".", find_git_repos, dir_list)
        currdir = os.popen("pwd").read().strip()

        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        cPickle.dump(dir_list, open(dfp, "w"))
    procs = []
    last_sleep = 0

    for folder in dir_list:
        if len([x for x in [x in folder for x in excludes] if x]) == 0:
            p = subprocess.Popen(["/usr/local/bin/git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
            procs.append({"folder": folder, "proc": p})
            if len(procs) % 15 == 0 and last_sleep != len(procs):
                #print "sleep", len(procs), last_sleep
                time.sleep(1)
                last_sleep = len(procs)
            #print folder, p.wait()
    for d in procs:
        p = d["proc"]
        sys.stdout.write(d["folder"])
        sys.stdout.flush()
        p.wait()
        output = p.stdout.read()
        output += p.stderr.read()

        if "Already up-to-date" in output:
            sys.stdout.write(".. ok\n")
            sys.stdout.flush()
        else:
            sys.stdout.write("\n"+output+"\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
