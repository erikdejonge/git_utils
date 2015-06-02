#!/bin/sh
/usr/local/bin/python3 /Users/rabshakeh/workspace/brainyquote/printbrainyquote.py -c -r -l 30 -d ~/workspace/brainyquote/quotes  > /Users/rabshakeh/cquote.txt
wait

python3 ~/workspace/git_utils/commit_all_git_folders_fast.py -m $1


