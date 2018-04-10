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
import subprocess
import pickle

from optparse import OptionParser
findcnt = 0
from sh import which

def check_result(folder, p):
    """
    @type folder: str, unicode
    @type p: str, unicode
    @return: None
    """
    out, err = p.communicate(timeout=30)

    if out:
        out = out.decode("utf-8")

    if err:
        err = err.decode("utf-8")
    else:
        err = ""

    if 0 == p.returncode:
        if "Already up-to-date." not in out.strip() and "no changes found" not in out.strip():
            print("\033[32m", out, "\033[0m")
    try:
        out += err

        # raise
        if 0 != p.returncode:
            print("\033[31mError in: " + folder + "\033[0m")
            print("\033[37m" + out + "\033[0m")
    except TypeError:
        print(err)


def main():
    """
    main
    """
    gitcmd = which('git')


    parser = OptionParser()
    parser.add_option("-i", "--ignoregithub", help="Ignore paths with github in it", action="store_true")
    parser.add_option("-f", "--folder", help="Startfolder", default='-')
    (options, args) = parser.parse_args()
    options.folder = options.folder.lstrip('-')

    if not options.folder:
        dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

        if os.path.exists(dfp):
            dir_list = pickle.load(open(dfp, "rb"))
        else:
            raise RuntimeError("Cannot find " + os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")
    else:
        from find_git_repos import find_git_repos
        dir_list = []

        for root, dirlist, file in os.walk(os.path.join(os.getcwd(), options.folder)):
            find_git_repos(dir_list, root, dirlist)

        dir_list = list(set([os.path.join(os.getcwd(), x[0]) for x in dir_list]))

    resetgits = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        resetgits = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        resetgits.extend([os.path.join(os.path.expanduser("~") + "/workspace", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])

    procs = []
    ws = os.path.expanduser("~") + "/workspace/"

    for folder in dir_list:
        if folder in resetgits:
            print("\033[33mReset:", folder.replace(ws, ""), "\033[0m")
            p = subprocess.Popen([gitcmd, "reset", "--hard", "origin/master"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
            out, err = p.communicate()

            if out:
                out = out.decode("utf-8")
            else:
                out = ""

            if err:
                err = err.decode("utf-8")
            else:
                err = ""

            out += err
            if 0 != p.returncode:
                print("\033[31m", out, "\033[0m")

        if options.ignoregithub is True and "github" in folder:
            pass
        else:
            if os.path.exists(folder):
                if os.path.exists(os.path.join(folder, "merge.sh")):
                    print("\033[96mMerge: " + folder.replace(ws, "") + "\033[0m")
                    pwd = os.getcwd()
                    os.chdir(folder)
                    os.system("./merge.sh")
                    os.chdir(pwd)
                elif os.path.exists(os.path.join(folder, ".git")):
                    print("\033[33mPull:", folder.replace(ws, ""), "\033[0m")
                    p = subprocess.Popen([gitcmd, "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
                    procs.append((folder, p))
                elif os.path.exists(os.path.join(folder, ".hg")):
                    print("\033[33mMercurial: " + folder.replace(ws, "") + "\033[0m")
                    p = subprocess.Popen(["/usr/local/bin/hg", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
                    p.wait()
                    check_result(folder, p)
            else:
                print("\033[95mmissing:", os.path.basename(folder), "\033[0m")

        if len(procs) > 1:
            for folder, p in procs:
                check_result(folder, p)

            procs = []

    for folder, p in procs:
        check_result(folder, p)

    print("\033[32mok\033[0m")


if __name__ == "__main__":
    main()
