    # pylint: disable-msg=C0103
# pylint: enable-msg=C0103
# tempfile regex format
#!/usr/bin/python
# -*- coding: utf-8 -*-
""" git checking script """

import sys
import os
import subprocess
import cPickle as pickle

findcnt = 0


def find_git_repos(arg, directory, files):
    """ find the git repositories """
    global findcnt
    findcnt += 1

    if findcnt % 100 == 0:
        sys.stdout.write(".")
        sys.stdout.flush()

    git_dir = os.path.join(directory, ".git")

    if os.path.exists(git_dir):
        try:
            config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip().split("//")[1].split("/")[0]
        except IndexError:
            config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip().split(":")[0].split("/")[0]
        except Exception, ex:
            config = str(ex)
        print
        print "gitdir:", directory, "("+config+")"
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    fcheck = raw_input("fcheck? (y/n): ")
    fcheck = fcheck.strip() == "y"

    if os.path.exists("/Users/rabshakeh/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open("/Users/rabshakeh/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    msg = raw_input("checkin message: ")

    if msg and len(msg.strip())==0:
        msg = os.popen("date").read().strip()
        msg += " commit and gc"

    dfp = "/Users/rabshakeh/workspace/git_utils/gitdirlist.pickle"

    if os.path.exists(dfp):
        os.remove(dfp)

    dir_list = []
    os.path.walk("/Users/rabshakeh/workspace", find_git_repos, dir_list)


    #dir_list = [os.path.join("/Users/rabshakeh/workspace", x.lstrip("./")) for x in dir_list]
    print "committing"
    pickle.dump(dir_list, open(dfp, "w"))
    procs = []

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            sys.stdout.write(".")
            sys.stdout.flush()
            p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am", msg], stdout=subprocess.PIPE, cwd=folder)
            p.wait()

    if not fcheck:
        print
        print "skipping check"
        return
    print

    for folder in dir_list:
        p = subprocess.Popen(["/usr/local/bin/git", "fsck"], cwd=folder)
        p.wait()


    for folder in dir_list:
        p = subprocess.Popen(["/usr/local/bin/git", "gc"], cwd=folder)
        p.wait()

    print "done"


if __name__ == "__main__":
    main()
