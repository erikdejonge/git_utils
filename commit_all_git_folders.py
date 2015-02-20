# coding=utf-8
# -*- coding: utf-8 -*-
""" git checking script """

import sys
import os
import subprocess

#noinspection PyPep8Naming

import cPickle as pickle

findcnt = 0


#noinspection PyUnusedLocal


def find_git_repos(arg, directory, files):
    """ find the git repositories
    :param arg:
    :param directory:
    :param files:
    """
    global findcnt
    findcnt += 1

    if findcnt % 100 == 0:
        sys.stdout.write(".")
        sys.stdout.flush()

    git_dir = os.path.join(directory, ".git")

    if os.path.exists(git_dir):
        try:
            config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip().split("//")[1].split("/")[0]
        except IndexError:
            config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip().split(":")[0].split("/")[0]
        except Exception, ex:
            config = str(ex)

        # print "gitdir:", directory, "("+config+")"
        sys.stdout.write("*")
        sys.stdout.flush()
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    fcheck = raw_input("fcheck? (y/n): ")
    fcheck = fcheck.strip() == "y"
    excludes = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    msg = raw_input("checkin message: ")

    if msg and len(msg.strip()) == 0:
        msg = os.popen("date").read().strip()
        msg += " commit and gc"

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        os.remove(dfp)

    dir_list = []
    os.path.walk(os.path.expanduser("~") + "/workspace", find_git_repos, dir_list)
    print "committing"
    pickle.dump(dir_list, open(dfp, "w"))

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            sys.stdout.write(".")
            sys.stdout.flush()
            p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am", msg], stdout=subprocess.PIPE, cwd=folder)
            p.communicate()

    if not fcheck:
        print
        print
        print "\033[33mDone, skipping check", len(dir_list), "items found\033[0m"
        return

    print
    l = []

    for folder in dir_list:
        p = subprocess.Popen(["/usr/local/bin/git", "fsck"], cwd=folder)
        l.append(p)

        if len(l) > 8:
            [p.communicate() for p in l]
            l = []
    [p.communicate() for p in l]
    l = []

    for folder in dir_list:
        p = subprocess.Popen(["/usr/local/bin/git", "gc"], cwd=folder)
        l.append(p)

        if len(l) > 8:
            [p.communicate() for p in l]
            l = []
    [p.communicate() for p in l]
    print "\033[33mDone", len(dir_list), "items found\033[0m"


if __name__ == "__main__":
    main()
