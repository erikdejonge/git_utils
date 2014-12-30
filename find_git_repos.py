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

        config = open(git_dir + "/config").read().split("url =")[1].split("\n")[0].strip()


        arg.append((os.path.basename(directory), config))

def main():
    dir_list = []
    os.path.walk("/home/rabshakeh/workspace/cryptobox", find_git_repos, dir_list)
    for i in dir_list:
        print i[1]

if __name__=="__main__":
    main()
