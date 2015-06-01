# coding=utf-8
"""
do not include the projects from the github directory for push
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

import os
import sys


def main():
    """
    main
    """
    gen_list = write_file = True
    githubfolder = os.path.expanduser("~") + "/workspace/github"
    set_projects = set()

    if gen_list:
        lastroot = ""

        for root, dirlist, file in os.walk(githubfolder):
            if root.count("/") < 7:
                set_projects.add(root.replace(os.path.expanduser("~") + "/workspace/github/", ""))

                for d in dirlist:
                    set_projects.add(d.replace(os.path.expanduser("~") + "/workspace/github/", ""))
    else:
        set_projects = [projectname.strip() for projectname in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if projectname.strip()]

    forks = set()

    for root, dirlist, files in os.walk(os.path.expanduser("~") + "/workspace"):
        if not root.startswith(githubfolder) and root.endswith(".git"):
            # for afile in files:
            #    print(afile)
            project_dir = root.strip("/.git/")
            project_base_folder = os.path.basename(os.path.dirname(project_dir))
            if project_base_folder=="forks":
                project_name = os.path.basename(project_dir)

                for project_name_iter in set_projects:
                    if project_name in project_name_iter:
                        forks.add(project_name_iter)

    for fork in forks:
        set_projects.remove(fork)

    if write_file:
        afile = open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs", "wt")

        for projectname in set_projects:
            afile.write(str(projectname) + "\n")

        afile.close()


if __name__ == "__main__":
    main()
