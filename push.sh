#!/bin/sh
#python3 ~/workspace/git_utils/push_all_git_folders.py

if [ -e ".git/config" ]; then
  resultstatus=`git status`
  if [[ $resultstatus == *"git add"* ]]
  then
      echo "\033[0;33mstatus cwd: `pwd`"
      echo "\033[0;90m$resultstatus\033[0m"
  fi
fi
