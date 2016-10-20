
#!/bin/sh
function globalpython3 () {
    if [ -f $HOME/.globalpythonedj ]; then
        `cat ~/.globalpythonedj` $@
    else
        python3 $@
    fi
}

globalpython3 ~/workspace/git_utils/status_all_git_folders.py
