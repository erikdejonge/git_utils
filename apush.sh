#!/bin/sh
function globalpython3 () {
    if [ -f $HOME/.globalpythonedj ]; then
        `cat ~/.globalpythonedj` $@
    else
        python3 $@
    fi
}

globalpython3 ~/workspace/git_utils/status_all_git_folders.py -f
globalpython3 ~/workspace/git_utils/commit_all_git_folders_fast.py
globalpython3 ~/workspace/git_utils/push_all_git_folders.py
globalpython3 ~/workspace/git_utils/status_all_git_folders.py
