#!/bin/sh
stats=$(python3 ~/workspace/git_utils/status_all_git_folders.py -n) &
~/workspace/git_utils/commitfast.sh;
~/workspace/git_utils/push.sh;
wait
echo $stats