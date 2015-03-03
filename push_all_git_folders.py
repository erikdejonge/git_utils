# coding=utf-8
# -*- coding: utf-8 -*-
""" git checking script """

import os
import sys
import cPickle
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
        if os.path.isdir(git_dir):
            arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    excludes = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        excludes.extend([os.path.join(os.path.expanduser("~") + "/workspace", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])
    print excludes
    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = cPickle.load(open(dfp))
    else:
        dir_list = []
        os.path.walk(".", find_git_repos, dir_list)
        currdir = os.popen("pwd").read().strip()
        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        cPickle.dump(dir_list, open(dfp, "w"))

    cnt = 0
    procs = []

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            sys.stdout.flush()
            p = subprocess.Popen(["/usr/local/bin/git", "status"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, cwd=folder)
            output, se = p.communicate()

            if "Your branch is ahead" in output:
                print "\033[35mpush "+os.path.basename(folder)+"\033[0m"
                p2 = subprocess.Popen(["/usr/local/bin/git", "push"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, cwd=folder)
                procs.append((folder, p2))

                if cnt > 8:
                    p2.communicate()
                    cnt = 0
                else:
                    cnt += 1

    for p in procs:

        output, se = p[1].communicate()

        if 0 != p[1].returncode:
            print "\033[31mError in: " + p[0] + "\033[0m"
            print "\033[37m" + se.strip() + output.strip() + "\033[0m"
        else:
            output = se.strip()
            print "\033[37m" + os.path.basename(p[0]) + " pushed *\n" + output.strip() + "\033[0m"


if __name__ == "__main__":
    main()
