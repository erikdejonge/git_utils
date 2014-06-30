#!/bin/sh
bash -c "cd /Users/rabshakeh/workspace/cryptobox/crypto_data&&git add databases/*;"
python /Users/rabshakeh/workspace/git_utils/commit_all_git_folders_fast.py
nohup tar -cf /Users/rabshakeh/workspace/cryptobox/idea.tar /Users/rabshakeh/workspace/cryptobox/.idea >/dev/null 2>&1
wait
