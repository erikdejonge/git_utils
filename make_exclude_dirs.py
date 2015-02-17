# coding=utf-8
"""
do not include the projects from the github directory for push
"""

import os


def main():
    """
    main
    """
    s = os.popen("ls " + os.path.expanduser("~") + "/workspace/github").read()
    l = s.strip().split("\n")
    f = open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs", "w")

    for i in l:
        f.write(i)
        f.write("\n")


if __name__ == "__main__":
    main()
