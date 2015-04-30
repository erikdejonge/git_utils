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

    f = open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs", "wt")
    st = set()
    for root, dirlist, file in os.walk(os.path.expanduser("~") + "/workspace/github"):
        if root.count("/") < 7:
            st.add(root.replace(os.path.expanduser("~") + "/workspace/github/", ""))
            for d in dirlist:
                st.add(d.replace(os.path.expanduser("~") + "/workspace/github/", ""))
    st2 = set()
    for i in st:
        if "documentation" not in i.lower():
            st2.add(i)
    for dn in st2:
        f.write(str(dn)+"\n")
    f.close()



if __name__ == "__main__":
    main()
