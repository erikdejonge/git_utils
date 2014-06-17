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

    if os.path.exists("/cygdrive/d/workarea/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open("/cygdrive/d/workarea/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    dfp = "/cygdrive/d/workarea/git_utils/gitdirlist.pickle"
    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp))
    else:
        raise RuntimeError("Cannot find /cygdrive/d/workarea/git_utils/gitdirlist.pickle")
    msg = os.popen("date").read().strip()
    procs = []

    for folder in dir_list:
        if len([x for x in [x in folder for x in excludes] if x]) == 0:
            print folder
            p = subprocess.Popen(["/usr/bin/git", "commit", "-am",  msg], stdout=subprocess.PIPE, cwd=folder)
            procs.append({"folder":folder, "proc":p})
            p.wait()
            output = p.stdout.read()
            if "nothing to commit" in output:
                sys.stdout.write(".")
                sys.stdout.flush()
            else:
                print
                print "\033[92mcommit "+os.path.basename(folder)+"\033[0m\n\033[93m"+output.strip()+"\033[0m"
    print



if __name__ == "__main__":
    main()
