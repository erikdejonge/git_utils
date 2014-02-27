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

def find_git_repos(arg, directory, files):
    """ find the git repositories """

    files = files
    git_dir = os.path.join(directory, ".git")
    if os.path.exists(git_dir):
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    excludes = []

    if os.path.exists("/Users/rabshakeh/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open("/Users/rabshakeh/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    dfp = "/Users/rabshakeh/workspace/git_utils/gitdirlist.pickle"
    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp))
    else:
        dir_list = []
        os.path.walk(".", find_git_repos, dir_list)
        currdir = os.popen("pwd").read().strip()
        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        pickle.dump(dir_list, open(dfp, "w"))

    msg = os.popen("date").read().strip()
    procs = []
    for folder in dir_list:

        if len([x for x in [x in folder for x in excludes] if x]) == 0:
            p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am",  msg], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
            procs.append({"folder":folder, "proc":p})

    to_push = []
    for d in procs:
        p = d["proc"]
        p.wait()
        output = p.stdout.read()
        if "nothing to commit" in output:
            pass
        else:

            print "commited:", d["folder"]
            to_push.append(d["folder"])

    print
    procs = []
    for folder in to_push:
        if len([x for x in [x in folder for x in excludes] if x]) == 0:

            p = subprocess.Popen(["/usr/local/bin/git", "push"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=folder)
            procs.append({"folder": folder, "proc": p})
            if len(procs) % 15 == 0 and last_sleep != len(procs):
                #print "sleep", len(procs), last_sleep
                time.sleep(1)
                last_sleep = len(procs)

            #print folder, p.wait()

    for d in procs:
        p = d["proc"]
        p.wait()

        output = p.stderr.read()

        if "Already up-to-date" in output:
            pass
        else:
            print "pushed:", d["folder"]
            #print output


if __name__ == "__main__":
    main()
