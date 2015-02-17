#!/bin/sh
rm ~/workspace/git_utils/exclude_dirs
python ~/workspace/git_utils/make_exclude_dirs.py
python ~/workspace/git_utils/commit_all_git_folders.py



