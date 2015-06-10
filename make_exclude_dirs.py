#!/usr/bin/env python3
# coding=utf-8
"""
do not include the projects from the github directory for push
"""
from __future__ import division, print_function, absolute_import, unicode_literals
from future import standard_library

import os
import sys


def print_stdout(chara, cnt=0, moddiv=1):
    """
    @type chara: str
    @return: None
    """
    cnt += 1

    if cnt % moddiv == 0:
        sys.stdout.write(chara)
        sys.stdout.flush()

    return cnt


def main():
    """
    main
    """
    forks = set()
    write_file = True
    projects_set = set()
    excludes = []
    workspacefolder = os.path.join(os.path.expanduser("~"), "workspace")

    if os.path.exists(os.path.join(workspacefolder, ".gitutilsexclude")):
        excludes.extend([os.path.join(workspacefolder, x.strip()) for x in open(os.path.join(workspacefolder, ".gitutilsexclude")).read().split("\n") if x.strip()])

    wsfolders = [os.path.join(workspacefolder, folder) for folder in os.listdir(workspacefolder) if os.path.join(workspacefolder, folder) not in excludes]
    for wsfolder in wsfolders:
        for root, dirlist, files in os.walk(wsfolder):
            if root.endswith(".git"):
                print_stdout(".")
                project_dir = root.strip("/.git/")
                project_base_folder = os.path.basename(os.path.dirname(project_dir))
                if project_base_folder == "forks":
                    project_name = os.path.basename(project_dir)

                    for project_name_iter in projects_set:
                        if project_name in project_name_iter:
                            forks.add(project_name_iter)

    for fork in forks:
        projects_set.remove(fork)

    if write_file:
        afile = open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs", "wt")

        for projectname in projects_set:
            afile.write(str(projectname) + "\n")

        afile.close()
    print()

standard_library.install_aliases()


if __name__ == "__main__":
    main()
