#!/bin/sh

python3 ~/workspace/git_utils/status_all_git_folders.py -f
python3 ~/workspace/git_utils/commit_all_git_folders_fast.py
python3 ~/workspace/git_utils/push_all_git_folders.py

