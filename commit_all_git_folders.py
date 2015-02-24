# coding=utf-8
""" git checking script """

import sys
import os
import subprocess
import cPickle
import datetime
from argparse import ArgumentParser

findcnt = 0


# noinspection PyUnusedLocal


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

    if os.path.exists(git_dir):
        try:
            config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip().split("//")[1].split("/")[0]
        except IndexError:
            config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip().split(":")[0].split("/")[0]
        except Exception, ex:
            config = str(ex)

        # print "gitdir:", directory, "("+config+")"
        sys.stdout.write("*")
        sys.stdout.flush()
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    timestamp = datetime.datetime.now().strftime("%A %d %B %Y (week:%w day;%j), %H:%M:%S").replace(";0", ":").replace(";", ":")
    parser = ArgumentParser(description="Vagrant controller, argument 'all' is whole cluster")
    parser.add_argument("-m", "--message", dest="message", help="commit message", nargs='?')
    parser.add_argument("-c", "--check", dest="check", help="git gc", action="store_true", default=False)
    args, unknown = parser.parse_known_args()
    print args, unknown, True
    if args.message is None:
        args.message = str(os.path.basename(os.getcwd())) + "\n" + str(timestamp)

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
    os.path.walk(os.path.expanduser("~") + "/workspace", find_git_repos, dir_list)
    print "committing"
    cPickle.dump(dir_list, open(dfp, "w"))

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            sys.stdout.write(".")
            sys.stdout.flush()
            p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am", msg], stdout=subprocess.PIPE, cwd=folder)
            p.communicate()

    if not fcheck:
        print
        print "\033[33mDone indexing, skipping check", len(dir_list), "items found\033[0m"
        print
        return

    print
    l = []

    for folder in dir_list:
        p = subprocess.Popen(["/usr/local/bin/git", "fsck"], cwd=folder)
        l.append(p)

        if len(l) > 8:
            [p.communicate() for p in l]
            l = []
    [p.communicate() for p in l]
    l = []

    for folder in dir_list:
        p = subprocess.Popen(["/usr/local/bin/git", "gc"], cwd=folder)
        l.append(p)

        if len(l) > 8:
            [p.communicate() for p in l]
            l = []
    [p.communicate() for p in l]
    print "\033[33mDone", len(dir_list), "items found\033[0m"


if __name__ == "__main__":
    main()
