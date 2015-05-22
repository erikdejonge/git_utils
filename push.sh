#!/bin/sh

python3 ~/workspace/git_utils/push_all_git_folders.py

if [ -e ".git/config" ]; then
  echo "status cwd:\033[0;33m"
  pwd
  echo "\033[0;90m "
  git status
  echo "\033[0m"
fi
