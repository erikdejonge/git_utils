# coding=utf-8
# -*- coding: utf-8 -*-
""" git checking script """
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

import os
import sys
import pickle
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


def print_status(status, prstatus):
    """
    @type status: str, unicode

    @type prstatus: str, unicode

    @return: None
    """
    for line in status.strip().split("\n"):
        if len(line.strip()) == 0:
            continue

        if "untracked files present" in line:
            prstatus[0] = ""
            print("\n\033[90m" + line + "\033[0m")
        elif "deleted:" in line:
            print("\033[31m" + line + "\033[0m")
        elif "rejected]" in line:
            print("\033[31m" + line + "\033[0m")
        elif "error: failed to push some refs" in line:
            print("\033[37m" + line + "\033[0m")
        elif prstatus[0] == "red" and "git add <file>" in line:
            print("\033[37m" + line + "\033[0m\n")
        elif prstatus[0] == "red" and not "git add <file>" in line:
            print("\033[34m" + line + "\033[0m")
        elif "Untracked files:" in line:
            prstatus[0] = "red"
            print("\033[37m" + line + "\033[0m")
        elif "new file:" in line:
            print("\033[34m" + line + "\033[0m")
        elif "status:" in line:
            print("\033[90m" + line + "\033[0m")
        elif "modified:" in line:
            print("\033[32m" + line + "\033[0m")
        else:
            print("\033[90m" + line + "\033[0m")


def communicate_with(procs):
    """
    """
    try:
        p = procs.pop()
    except IndexError:
        p = None

    if p is not None:
        output, se = p[1].communicate()
        output = output.decode("utf-8")

        if se:
            se = se.decode("utf-8")

        if 0 != p[1].returncode:
            prstatus = [""]

            print_status(se, prstatus)

            #print("\033[37m" + str(se.strip()) + str(output.strip()) + "\033[0m")
        else:
            output = se.strip()
            print("\033[37m" + os.path.basename(p[0]) + " pushed *\n" + output.strip() + "\033[0m")


def main():
    """ check all folders and pull all from the server """
    excludes = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        for item in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n"):
            item = item.strip()

            if item:
                for si in item.split("/"):
                    excludes.append(si)

                excludes.append(os.path.join(os.path.expanduser("~") + "/workspace", item.strip()))

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp, "rb"))
    else:
        dir_list = []
        for root, dirlist, file in os.walk("."):
            find_git_repos(dir_list, root, dirlist)

        currdir = os.popen("pwd").read().strip()
        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        pickle.dump(dir_list, open(dfp, "wb"))

    cnt = 0
    procs = []
    prstatus = [""]
    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            if os.path.exists(os.path.join(folder, ".git")):
                sys.stdout.flush()
                p = subprocess.Popen(["/usr/local/bin/git", "status"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, cwd=folder)
                output, se = p.communicate()

                if output:
                    output = output.decode("utf-8")

                if se:
                    se = se.decode("utf-8")

                try:
                    if "Your branch is ahead" in output or "have diverged" in output:
                        print("\033[95mpush " + os.path.basename(folder) + "\033[0m")
                        p2 = subprocess.Popen(["/usr/local/bin/git", "push"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, cwd=folder)
                        procs.append((folder, p2))

                        if len(procs) > 4 or (len(procs) == len(dir_list)):
                            communicate_with(procs)
                        else:
                            cnt += 1
                    else:
                        if "nothing to commit" not in output:
                            print_status(output, prstatus)
                except BaseException as e:
                    print("\033[37m",e,"\033[0m")
                    print("\033[37m",folder,"\033[0m")


    communicate_with(procs)
if __name__ == "__main__":
    main()
