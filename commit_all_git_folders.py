#!/usr/bin/env python3
# coding=utf-8
"""
git checking script
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library

import datetime
import os
import pickle
import subprocess
import sys

from argparse import ArgumentParser
from consoleprinter import console
findcnt = 0


def find_git_repos(arg, directory, files):
    """
    @type arg: str, unicode
    @type directory: str, unicode
    @type files: str, unicode
    @return: None
    """
    global findcnt
    findcnt += 1

    if findcnt % 100 == 0:
        sys.stdout.write(".")
        sys.stdout.flush()

    git_dir = os.path.join(directory, ".git")
    hg_dir = os.path.join(directory, ".hg")

    if os.path.exists(git_dir):
        try:
            config = open(git_dir + "/config").read().split("url =")
            if len(config)>1:
                config = config[1].split("\n")[0].strip().split("//")[1].split("/")[0]
        except IndexError:
            config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip().split(":")[0].split("/")[0]
        except Exception as ex:
            config = str(ex)

        # print "gitdir:", directory, "("+config+")"
        sys.stdout.write("*")
        sys.stdout.flush()
        arg.append(directory)
    elif os.path.exists(hg_dir):
        try:
            config = open(hg_dir + "/hgrc").read().split("default =")[1].split("\n")[0].strip().split("//")[1].split("/")[0]
        except Exception as ex:
            config = str(ex)

        #console("gitdir:", directory, "("+config+")", color="magenta")
        sys.stdout.write("*")
        sys.stdout.flush()
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    timestamp = datetime.datetime.now().strftime("%A %d %B %Y (week;%W day;%j), %H:%M:%S").replace(";0", ":").replace(";", ":")
    parser = ArgumentParser()
    parser.add_argument("-m", "--message", dest="message", help="commit message", nargs='?')
    parser.add_argument("-c", "--check", dest="check", help="git gc", action="store_true", default=False)
    args, unknown = parser.parse_known_args()

    if args.message is None:
        args.message = str(os.path.basename(os.getcwd())) + ":" + str(timestamp)

    fcheck = args.check
    excludes = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        excludes.extend([os.path.join(os.path.expanduser("~") + "/workspace/.gitutilsexclude", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        excludes.extend([os.path.join(os.path.expanduser("~") + "/workspace", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])

    msg = args.message

    if msg and len(msg.strip()) == 0:
        msg = os.popen("date").read().strip()
        msg += " Commit and gc"

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        os.remove(dfp)

    dir_list = []
    excludes = []
    workspacefolder = os.path.join(os.path.expanduser("~"), "workspace")

    if os.path.exists(os.path.join(workspacefolder, ".gitutilsexclude")):
        excludes.extend([os.path.join(workspacefolder, x.strip()) for x in open(os.path.join(workspacefolder, ".gitutilsexclude")).read().split("\n") if x.strip()])

    wsfolders = [os.path.join(workspacefolder, folder) for folder in os.listdir(workspacefolder) if os.path.join(workspacefolder, folder) not in excludes]
    for wsfolder in wsfolders:
        for root, dirlist, file in os.walk(wsfolder):
            find_git_repos(dir_list, root, dirlist)

    dir_list = [project_name for project_name in dir_list if "workspace/github" not in project_name]
    dir_list2 = []
    for d in dir_list:
        if d not in excludes:
            dir_list2.append(d)
    print
    dir_list=dir_list2
    print("committing")

    pickle.dump(dir_list, open(dfp, "wb"))

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            sys.stdout.write(".")
            sys.stdout.flush()
            if os.path.exists(os.path.join(folder, ".git")):
                p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am", msg], stdout=subprocess.PIPE, cwd=folder)
                p.communicate()
                #p.wait()

    if not fcheck:
        print()
        print("\033[33mDone indexing, skipping check", len(dir_list), "items found\033[0m")
        print()
        return

    print()
    l = []

    for folder in dir_list:
        if os.path.exists(os.path.join(folder, ".git")):
            p = subprocess.Popen(["/usr/local/bin/git", "fsck"], cwd=folder)
            l.append(p)

            if len(l) > 8:
                [p.communicate() for p in l]
                l = []
    [p.communicate() for p in l]
    l = []

    for folder in dir_list:
        if os.path.exists(os.path.join(folder, ".git")):
            p = subprocess.Popen(["/usr/local/bin/git", "gc"], cwd=folder)
            l.append(p)

            if len(l) > 8:
                [p.communicate() for p in l]
                l = []
    [p.communicate() for p in l]
    print("\033[33mDone", len(dir_list), "items found\033[0m")



standard_library.install_aliases()

if __name__ == "__main__":
    main()
