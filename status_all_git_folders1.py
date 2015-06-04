# coding=utf-8
"""
Lorum ipsum

Usage:
  status_all_git_folders1.py [options] <input>

Options:
  -h --help     Show this screen.

author  : rabshakeh (erik@a8.nl)
project : git_utils
created : 04-06-15 / 14:32
"""
from arguments import Arguments


def main():
    """
    main
    """
    arguments = Arguments(__doc__)
    print(arguments)


if __name__ == "__main__":
    main()
