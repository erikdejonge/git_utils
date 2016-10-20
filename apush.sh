#!/bin/sh
function globalpython3 () {
    `cat ~/.globalpythonedj` $@
}

globalpython3 ~/workspace/git_utils/status_all_git_folders.py -f
globalpython3 ~/workspace/git_utils/commit_all_git_folders_fast.py
globalpython3 ~/workspace/git_utils/push_all_git_folders.py
globalpython3 ~/workspace/git_utils/status_all_git_folders.py
