# pylint: disable-msg=C0103
# pylint: enable-msg=C0103
# tempfile regex format
#
#!/usr/bin/python
# -*- coding: utf-8 -*-
""" git checking script """
import os
import sys
import subprocess
import cPickle as pickle


def find_git_repos(arg, directory, files):
    """
    @type arg: str
    @type directory: str
    @type files: list
    """
    files = files
    git_dir = os.path.join(directory, ".git")

    if os.path.exists(git_dir):
        arg.append(directory)


def main():
    """
    main
    """
    excludes = []
    """ check all folders and pull all from the server """
    dir_list = []
    os.path.walk(".", find_git_repos, dir_list)
    currdir = os.popen("pwd").read().strip()
    dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]

    procs = []

    for folder in dir_list:
        if len([x for x in [x in folder for x in excludes] if x]) == 0:
            p = subprocess.Popen(["/usr/local/bin/git", "pull"], stdout=subprocess.PIPE, cwd=folder)
            procs.append({"folder": folder, "proc": p})

    for d in procs:
        p = d["proc"]
        p.wait()
        output = p.stdout.read()

        if "Already up-to-date" in output:
            sys.stdout.write(".")
            sys.stdout.flush()
        else:
            print "pull_all_git_folders.py:60"
            print "pull_all_git_folders.py:61", d["folder"]
            print "pull_all_git_folders.py:62", output
    print "pull_all_git_folders.py:63"

if __name__ == "__main__":
    main()
