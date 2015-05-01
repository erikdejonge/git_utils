#!/bin/sh

python3 ~/workspace/git_utils/push_all_git_folders.py

if [ -d ".git" ]; then
  echo -e "\033[0;90m"`git status`"\033[0m"

fi
