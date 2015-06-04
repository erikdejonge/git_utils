#!/bin/sh
$(python3 ~/workspace/git_utils/status_all_git_folders.py -n > ~/.stats.txt) &
~/workspace/git_utils/commitfast.sh;
~/workspace/git_utils/push.sh;
wait
cat ~/.stats.txt
rm  ~/.stats.txt