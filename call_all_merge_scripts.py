#!/usr/bin/env python3
# coding=utf-8
"""
Project forks

Usage:
  call_all_merge_scripts.py [options] <filepath>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : forks
created : 31 Jul 2016 / 14:17
where   : Latitude: 51.825310
          longitude: 4.650966
          https://www.google.nl/maps/place/51.825310,4.650966
"""
import sys
import os

from arguments import Arguments
from consoleprinter import console
from cmdssh import cmd_exec

if sys.version_info.major < 3:
    console("Python 3 is required", color="red", plaintext="True")
    exit(1)


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc):
        """
        __init__
        """
        self.help = False
        self.input = ""
        super().__init__(doc)


def main():
    """
    main
    """
    cwd = os.getcwd()
    arguments = IArguments(__doc__)

    for fp in os.listdir(arguments.filepath):
        if os.path.isdir(fp):
            fp = os.path.join(arguments.filepath, fp)
            fpm = os.path.join(fp, 'merge.sh')

            if os.path.exists(fpm):
                os.chdir(fp)
                console(fp)
                os.system("git pull; git commit -am '-'; git push")
                code, res = cmd_exec(fpm)

                if code == 128:
                    console(fp)
                    print("rm -Rf", fp)
                    return

                if code != 0:
                    os.chdir(fp)
                    return
            else:
                console("merge.sh path does not exist")
                console(fp)
                print("rm -Rf", fp)
                return

            os.chdir(cwd)


if __name__ == "__main__":
    main()
