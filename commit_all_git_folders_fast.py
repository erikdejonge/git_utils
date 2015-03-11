# coding=utf-8
""" git checking script """
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()
from builtins import str

import os
import sys
import datetime
import pickle
import subprocess
from argparse import ArgumentParser


def main():
    """ check all folders and pull all from the server """
    timestamp = datetime.datetime.now().strftime("%A %d %B %Y (week;%W day;%j), %H:%M:%S").replace(";0", ":").replace(";", ":")
    parser = ArgumentParser()
    parser.add_argument("-m", "--message", dest="message", help="commit message", nargs='?')
    args, unknown = parser.parse_known_args()

    if args.message is None:
        args.message = str(os.path.basename(os.getcwd())) + "\n" + str(timestamp)

    excludes = []

    if os.path.exists(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs"):
        excludes = [x.strip() for x in open(os.path.expanduser("~") + "/workspace/git_utils/exclude_dirs").read().split("\n") if x.strip()]

    if os.path.exists(os.path.expanduser("~") + "/workspace/.gitutilsexclude"):
        excludes.extend([os.path.join(os.path.expanduser("~") + "/workspace", x.strip()) for x in open(os.path.expanduser("~") + "/workspace/.gitutilsexclude").read().split("\n") if x.strip()])

    dfp = os.path.expanduser(os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    if os.path.exists(dfp):
        ofp = open(dfp, "rb")

        dir_list = pickle.load(ofp)
    else:
        raise RuntimeError("Cannot find " + os.path.expanduser("~") + "/workspace/git_utils/gitdirlist.pickle")

    msg = args.message

    for folder in dir_list:
        if os.path.basename(folder) not in excludes:
            if os.path.exists(os.path.join(folder, ".git")):
                
                p = subprocess.Popen(["/usr/local/bin/git", "commit", "-am",  msg], stdout=subprocess.PIPE, cwd=folder)
                output, se = p.communicate()
                if output:
                    output = output.decode("utf-8")
                if se:
                    se = se.decode("utf-8")
                if "nothing to commit" in str(output):
                    sys.stdout.write(".")
                    sys.stdout.flush()
                else:
                    print()
                    print("\033[32mcommit "+os.path.basename(folder)+"\033[0m\n\033[37m"+output.strip()+"\033[0m")

    print()   


if __name__ == "__main__":
    main()
