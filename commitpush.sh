#!/bin/sh
status=$(python3 ~/workspace/git_utils/status_all_git_folders.py) &
~/workspace/git_utils/commitfast.sh;
~/workspace/git_utils/push.sh;
wait
echo
echo -e $status