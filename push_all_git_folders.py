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
    cnt = 0
    procs = []
    for folder in dir_list:
        if len([x for x in [x in folder for x in excludes] if x]) == 0:
            sys.stdout.flush()
            p = subprocess.Popen(["/usr/local/bin/git", "status"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, cwd=folder)
            p.wait()

            if "Your branch is ahead" in p.stdout.read():
                print "\033[95mpush "+os.path.basename(folder)+"\033[0m"

                p2 = subprocess.Popen(["/usr/local/bin/git", "push"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, cwd=folder)
                procs.append((folder, p2))
                if cnt > 5:
                    p2.wait()
                    cnt = 0
                else:
                    cnt += 1

    for p in procs:
        p[1].wait()
        output = p[1].stdout.read()
        output = output.strip()
        print "\033[93m" + os.path.basename(d["folder"]) + " pushed *\n" + output.strip() + "\033[0m"

if __name__ == "__main__":
    main()
