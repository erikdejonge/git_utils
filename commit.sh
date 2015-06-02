#!/bin/sh
/usr/local/bin/python3 /Users/rabshakeh/workspace/brainyquote/printbrainyquote.py -c -r -l 30 -d ~/workspace/brainyquote/quotes  > /Users/rabshakeh/cquote.txt
rm ~/workspace/git_utils/exclude_dirs
python3 ~/workspace/git_utils/make_exclude_dirs.py
python3 ~/workspace/git_utils/commit_all_git_folders.py



