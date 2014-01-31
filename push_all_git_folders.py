# pylint: disable-msg=C0103
# pylint: enable-msg=C0103
# tempfile regex format
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

""" git checking script """

import os
import time
import sys
import cPickle
import subprocess


def find_git_repos(arg, directory, files):
    """ find the git repositories """

    files = files
    git_dir = os.path.join(directory, ".git")
    if os.path.exists(git_dir):
        if os.path.isdir(git_dir):
            arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    excludes = []

    if os.path.exists("/Users/rabshakeh/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open("/Users/rabshakeh/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    dfp = "/Users/rabshakeh/workspace/git_utils/gitdirlist.pickle"
    if os.path.exists(dfp):
        dir_list = cPickle.load(open(dfp))
    else:
        dir_list = []
        os.path.walk(".", find_git_repos, dir_list)
        currdir = os.popen("pwd").read().strip()
        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        cPickle.dump(dir_list, open(dfp, "w"))

    procs = []

    for folder in dir_list:
        last_sleep = 0
        if len([x for x in [x in folder for x in excludes] if x]) == 0:
            started = False
            while not started:
                try:
                    procs.append({"folder": folder, "proc": subprocess.Popen(["/usr/local/bin/git", "push"], stderr=subprocess.PIPE, cwd=folder)})
                    started = True
                except Exception, e:
                    print str(e)
                    time.sleep(1)
        if len(procs) % 5 == 0 and last_sleep!=len(procs):
            print "sleep", len(procs), last_sleep
            time.sleep(1)
            last_sleep = len(procs)
    for d in procs:
        p = d["proc"]
        p.wait()
        output = p.stderr.read()
        if "Everything up-to-date" in output:
            sys.stdout.write(".")
            sys.stdout.flush()
        else:
            print
            print d["folder"]
            print output
    print


if __name__ == "__main__":
    main()
