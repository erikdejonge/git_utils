# pylint: disable-msg=C0103
# pylint: enable-msg=C0103
# tempfile regex format
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

""" git checking script """

import os
import sys
import cPickle as pickle
import subprocess


def main():
    """ check all folders and pull all from the server """
    excludes = []

    if os.path.exists("/Users/rabshakeh/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open("/Users/rabshakeh/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    dfp = "/Users/rabshakeh/workspace/git_utils/gitdirlist.pickle"
    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp))
    else:
        raise RuntimeError("Cannot find /Users/rabshakeh/workspace/git_utils/gitdirlist.pickle")
    msg = os.popen("date").read().strip()
    procs = []
    cnt = 0
    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am",  msg], cwd=folder)
            p.wait()
            output = ""
            if "nothing to commit" in output:
                sys.stdout.write(".")
                sys.stdout.flush()
            else:
                print
                print "\033[92mcommit "+os.path.basename(folder)+"\033[0m\n\033[93m"+output.strip()+"\033[0m"

    print



if __name__ == "__main__":
    main()
