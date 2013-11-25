# pylint: disable-msg=C0103
# pylint: enable-msg=C0103
# tempfile regex format
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

""" git checking script """

import os
import subprocess
import cPickle as pickle

def find_git_repos(arg, directory, files):
    """ find the git repositories """

    files = files
    git_dir = os.path.join(directory, ".git")
    if os.path.exists(git_dir):
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """

    msg = raw_input("message: ")

    dfp = "/Users/rabshakeh/workspace/gitdirlist.pickle"
    if os.path.exists(dfp):
        os.remove(dfp) 
    dir_list = []
    os.path.walk(".", find_git_repos, dir_list)
    currdir = os.popen("pwd").read().strip()
    dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
    pickle.dump(dir_list, open(dfp, "w"))

    procs = []
    for folder in dir_list:
        procs.append(subprocess.Popen(["/usr/local/bin/git", "commit", "-am", msg], cwd=folder))

    for p in procs:
        p.wait()

    procs = []
    for folder in dir_list:
        procs.append(subprocess.Popen(["/usr/local/bin/git", "gc"], cwd=folder))

    for p in procs:
        p.wait()

if __name__ == "__main__":
    main()
