if [ -b "nohup.out" ]
then
  rm nohup.out
fi

nohup python /Users/rabshakeh/workspace/git_utils/commit_all_git_folders.py&&cat nohup.out &



