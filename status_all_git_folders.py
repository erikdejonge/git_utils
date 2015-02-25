# coding=utf-8

# -*- coding: utf-8 -*-
""" git checking script """

import os
# noinspection PyPep8Naming
import cPickle as pickle


def find_git_repos(arg, directory, files):
    """ find the git repositories
    :param arg:
    :param directory:
    :param files:
    """
    # noinspection PyUnusedLocal
    files = files
    git_dir = os.path.join(directory, ".git")

    if os.path.exists(git_dir):
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """
    excludes = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        excludes.extend([os.path.join(os.path.expanduser("~") + "/workspace", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        dir_list = pickle.load(open(dfp))
        currdir = os.popen("pwd").read().strip()
    else:
        dir_list = []
        os.path.walk(".", find_git_repos, dir_list)
        currdir = os.popen("pwd").read().strip()
        dir_list = [os.path.join(currdir, x.lstrip("./")) for x in dir_list]
        pickle.dump(dir_list, open(dfp, "w"))

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            os.chdir(folder)

            # os.system("git rm --cached -r .idea/")
            for branch in os.popen("git branch").read().split("\n"):
                if "*" in branch:
                    fl = os.path.basename(folder)

                    if len(fl) < 25:
                        fl += (" " * (25 - len(fl)))

                    if "master" not in branch:
                        if fl.strip() not in excludes and os.path.join(os.path.expanduser("~") + "/workspace", fl.strip()) not in excludes:
                            print fl + "\t" + branch.replace("*", "").strip()

            status = os.popen("git status").read()

            if "modified" in status or "Untracked" in status or "new file" in status or "deleted" in status:
                print "\033[96mstatus:", folder, "\033[0m"

                if "new file" in status:
                    print "\033[32m" + status.strip() + "\033[0m\n"

                if "deleted" in status:
                    print "\033[91m" + status.strip() + "\033[0m\n"
                else:
                    print "\033[33m" + status.strip() + "\033[0m\n"

            os.chdir(currdir)


if __name__ == "__main__":
    main()
