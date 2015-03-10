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


def check_result(folder, p):
    """
    @type folder: str, unicode
    @type p: str, unicode
    @return: None
    """
    out, err = p.communicate()
    if 0 == p.returncode:
        if "Already up-to-date." != out.strip():
            print("\033[32m", out, "\033[0m")
    out += err
    if 0 != p.returncode:
        print("\033[31mError in: " + folder + "\033[0m")
        print("\033[37m" + out + "\033[0m")


def main():
    """
    main
    """
    parser = OptionParser()
    parser.add_option("-i", "--ignoregithub", help="Ignore paths with github in it", action="store_true")
    (options, args) = parser.parse_args()
    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp))
    else:
        raise RuntimeError("Cannot find " + os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    resetgits = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        resetgits = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        resetgits.extend([os.path.join(os.path.expanduser("~") + "/workspace", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])

    procs = []
    ws = os.path.expanduser("~") + "/workspace/"

    for folder in dir_list:
        if folder in resetgits:
            print("\033[37mReset:", folder, "\033[0m")
            p = subprocess.Popen(["/usr/local/bin/git", "reset", "--hard", "origin/master"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
            out, err = p.communicate()
            out += err
            if 0 != p.returncode:
                print("\033[31m", out, "\033[0m")

        if options.ignoregithub is True and "github" in folder:
            pass
        else:
            if os.path.exists(folder):
                print("\033[36mPull:", folder.replace(ws, ""), "\033[0m")

                p = subprocess.Popen(["/usr/local/bin/git", "pull"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
                procs.append((folder, p))
            else:
                print("\033[35mmissing:", os.path.basename(folder), "\033[0m")

        if len(procs) > 1:
            for folder, p in procs:
                check_result(folder, p)

            procs = []

    for folder, p in procs:
        check_result(folder, p)

    print("\033[32mok\033[0m")


if __name__ == "__main__":
    main()
