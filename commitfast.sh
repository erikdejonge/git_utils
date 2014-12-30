#!/bin/sh
python /home/rabshakeh/workspace/git_utils/commit_all_git_folders_fast.py
nohup tar -cf /home/rabshakeh/workspace/cryptobox/idea.tar /home/rabshakeh/workspace/cryptobox/.idea >/dev/null 2>&1
wait
