# pylint: disable-msg=C0103
# pylint: enable-msg=C0103
# tempfile regex format
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

""" git checking script """

import os
import cPickle as pickle

def find_git_repos(arg, directory, files):
    """ find the git repositories """

    files = files
    git_dir = os.path.join(directory, ".git")
    if os.path.exists(git_dir):
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """


    excludes = []

    if os.path.exists("/Users/rabshakeh/workspace/excludes_push"):
        excludes = open("/Users/rabshakeh/workspace/excludes_push").read().split("\n")

    dfp = "/Users/rabshakeh/workspace/gitdirlist.pickle"
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
            #os.system("git rm --cached -r .idea/")
            status = os.popen("git status").read()
            if "modified" in status or "Untracked" in status:
                print "In -->", folder
                print status
            os.chdir(currdir)

if __name__ == "__main__":
    main()
