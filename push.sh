#!/bin/sh

python3 ~/workspace/git_utils/push_all_git_folders.py

if [ -d ".git" ]; then
  echo "\033[0;90m"
  pwd
  git status
  echo "\033[0m"
fi
