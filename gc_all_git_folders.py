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
import pickle

def main():
    """ check all folders and pull all from the server """

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp, "rb"))
    else:
        raise RuntimeError("Cannot find " + os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    currdir = os.getcwd()

    for folder in dir_list:
        if not os.path.exists(os.path.join(folder, ".git")):
            print(".git folder removed?", os.path.join(folder, ".git"))
            for folder in dir_list:
                print(folder)
            raise SystemError()

        os.chdir(folder)
        status = os.popen("git repack -a -d").read()
        #status = os.popen("git gc --aggressive --prune").read()

        print(status)
        os.chdir(currdir)


if __name__ == "__main__":
    main()
