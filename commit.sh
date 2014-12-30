#!/bin/sh
rm /home/rabshakeh/workspace/git_utils/exclude_dirs
python /home/rabshakeh/workspace/git_utils/make_exclude_dirs.py
python /home/rabshakeh/workspace/git_utils/commit_all_git_folders.py



