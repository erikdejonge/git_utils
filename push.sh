#!/bin/sh

python3 ~/workspace/git_utils/push_all_git_folders.py

if [ -d ".git" ]; then
  git status
fi
