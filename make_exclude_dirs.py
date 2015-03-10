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


def main():
    """
    main
    """
    s = os.popen("ls " + os.path.expanduser("~") + "/workspace/github").read()
    l = s.strip().split("\n")
    f = open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs", "w")
    ws = os.popen("ls " + os.path.expanduser("~") + "/workspace").read()
    wl = ws.strip().split("\n")

    for i in l:
        if i not in wl:
            f.write(i)
            f.write("\n")




if __name__ == "__main__":
    main()
