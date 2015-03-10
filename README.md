git_utils
=========

some helper scripts to do git operations on al the git repos in your ~workspace


alias for .bash_profile
=======================
```bash
alias com='~/workspace/git_utils/commitfast.sh;'
alias comm='python3 ~/workspace/git_utils/make_exclude_dirs.py&&/Users/rabshakeh/workspace/git_utils/commit.sh&&/Users/rabshakeh/workspace/git_utils/push.sh'
alias pull='python3 ~/workspace/git_utils/pull_all_git_folders.py -i'
alias pullall='python3 ~/workspace/git_utils/pull_all_git_folders.py'
alias push='~/workspace/git_utils/push.sh;'
alias compush='~/workspace/git_utils/commitfast.sh; ~/workspace/git_utils/push.sh; wait'
alias stats='~/workspace/git_utils/status.sh;'
alias gcom='git commit -am "-" > /dev/null; git status'
alias gcompush='git commit -am "-" > /dev/null; git push'
alias gitreset='git reset --hard origin/master'
alias gpull='git pull'
alias gpush='git push'
alias gstats='git status'
alias ggc='~/workspace/git_utils/gc.sh'
```

comm
====
Asks for a commit message and if it neeeds to clean
Scans the directories in ~workspace except the ones in ~workspace/github, it looks for the .git folder and parses out the url from .git/config
After scanning, it commits al the changes found 
If cleaning is selected it will do a 'git fsck' and a 'git gc' on all the folders (can take a while)

com
===
Commits all the folders found in the scanning phase with "-" for message.

pull
====
Pulls all folders, except ~/workspace/github

pullall
=======
Pulls all folders

push
====
Pushes all changes to server

compush
=======
Commits all changes with message "-" and then pushes the changes

stats
=====
Shows all changes in ~workspace except for ~workspace/github

ggc
===
Do a 'git gc' on all folders
