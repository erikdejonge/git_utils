# coding=utf-8

# -*- coding: utf-8 -*-
""" git checking script """

import os
import sys
# noinspection PyPep8Naming
import cPickle as pickle
import subprocess


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


def main():
    """ check all folders and pull all from the server """
    excludes = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp))
    else:
        dir_list = []
        os.path.walk(".", find_git_repos, dir_list)
        currdir = os.popen("pwd").read().strip()
        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        pickle.dump(dir_list, open(dfp, "w"))

    msg = os.popen("date").read().strip()
    # noinspection PyUnusedLocal
    procs = []

    for folder in dir_list:
        if len([x for x in [x in folder for x in excludes] if x]) == 0:
            print folder
            p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am",  msg], stdout=subprocess.PIPE, cwd=folder)
            output, stderrout = p.communicate()

            if "nothing to commit" in output:
                sys.stdout.write(".")
                sys.stdout.flush()
            else:
                sys.stdout.write("\n")
                print output

    print


if __name__ == "__main__":
    main()
