#!/bin/sh
python ~/workspace/git_utils/commit_all_git_folders_fast.py -m $1
nohup tar -cf ~/workspace/cryptobox/idea.tar ~/workspace/cryptobox/.idea >/dev/null 2>&1
wait
