# pylint: disable-msg=C0103
# pylint: enable-msg=C0103
# tempfile regex format
#
#!/usr/bin/python
# -*- coding: utf-8 -*-

""" git checking script """

import os


def find_git_repos(arg, directory, files):
    """ find the git repositories """

    files = files
    git_dir = os.path.join(directory, ".git")
    if os.path.exists(git_dir):
        arg.append(directory)


def main():
    """ check all folders and pull all from the server """

    dir_list = []
    os.path.walk(".", find_git_repos, dir_list)

    currdir = os.popen("pwd").read().strip()
    for folder in dir_list:
        os.chdir(folder)
        status = os.popen("git gc").read()
        print status
        os.chdir(currdir)

if __name__ == "__main__":
    main()
