# coding=utf-8

# -*- coding: utf-8 -*-
""" git checking script """

import os
import cPickle

def main():
    """ check all folders and pull all from the server """

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = cPickle.load(open(dfp))
    else:
        raise RuntimeError("Cannot find " + os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    currdir = os.getcwd()

    for folder in dir_list:
        os.chdir(folder)
        status = os.popen("git gc").read()
        print status
        os.chdir(currdir)


if __name__ == "__main__":
    main()
