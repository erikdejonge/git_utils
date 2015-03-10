# coding=utf-8

# -*- coding: utf-8 -*-
""" git checking script """
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

import sys
import os
findcnt = 0


# noinspection PyUnusedLocal
def find_git_repos(arg, directory, files):
    """ find the git repositories
    :param arg:
    :param directory:
    :param files:
    """
    global findcnt
    findcnt += 1

    if findcnt % 100 == 0:
        sys.stdout.write(".")
        sys.stdout.flush()

    git_dir = os.path.join(directory, ".git")

    if os.path.exists(git_dir):
        config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip()
        arg.append((os.path.basename(directory), config))


def main():
    """
    main
    """
    dir_list = []
    os.path.walk(os.path.expanduser("~") + "/workspace", find_git_repos, dir_list)

    for i in dir_list:
        print(i[1])


if __name__ == "__main__":
    main()
