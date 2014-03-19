# pylint: disable-msg=C0103
# pylint: enable-msg=C0103
# tempfile regex format
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

""" git checking script """
import sys
import os
import subprocess
import cPickle as pickle
lastdirvisited = ""

def find_git_repos(arg, directory, files):
    """ find the git repositories """
    global lastdirvisited
    files = files
    ds = directory.split("/")
    if len(ds)>3:
        printpath = ds[len(ds)-4]+"/"+ds[len(ds)-3]+"/"+ds[len(ds)-2]+"/"+ds[len(ds)-1]
        if ds[len(ds)-4]!=printpath:
            print ds[len(ds)-4]+"/"+ds[len(ds)-3]+"/"+ds[len(ds)-2]+"/"+ds[len(ds)-1]
            lastdirvisited = ds[len(ds)-4]
    git_dir = os.path.join(directory, ".git")
    if os.path.exists(git_dir):
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    fcheck = raw_input("fcheck? (y/n): ")
    fcheck = fcheck.strip() == "y"

    if os.path.exists("/Users/rabshakeh/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open("/Users/rabshakeh/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    msg = os.popen("date").read().strip()
    msg += " commit and gc"

    dfp = "/Users/rabshakeh/workspace/git_utils/gitdirlist.pickle"
    if os.path.exists(dfp):
        os.remove(dfp)
    dir_list = []
    os.path.walk("/Users/rabshakeh/workspace", find_git_repos, dir_list)
    print
    #dir_list = [os.path.join("/Users/rabshakeh/workspace", x.lstrip("./")) for x in dir_list]


    pickle.dump(dir_list, open(dfp, "w"))

    procs = []
    for folder in dir_list:
        if len([x for x in [x in folder for x in excludes] if x]) == 0:
            print folder
            p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am", msg], stdout=subprocess.PIPE, cwd=folder)
            p.wait()
    if not fcheck:
        print "skipping check"
        return
    print
    procs = []
    for folder in dir_list:
        procs.append(subprocess.Popen(["/usr/local/bin/git", "fsck"], cwd=folder))

    for p in procs:
        p.wait()

    procs = []
    for folder in dir_list:
        procs.append(subprocess.Popen(["/usr/local/bin/git", "gc"], cwd=folder))

    for p in procs:
        p.wait()



if __name__ == "__main__":
    main()
