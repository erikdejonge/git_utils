export CLICOLOR=1
export LSCOLORS=ExFxCxDxBxegedabagacad


export PATH=/usr/local/bin:/usr/local/share/npm/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/rabshakeh/workspace/depot_tools
export LC_ALL=en_US.UTF-8
alias flush="echo 'flush_all' | nc localhost 11211"
alias kp='sudo killall python;sudo killall Python'
alias restart_couch='/usr/bin/sudo launchctl stop org.apache.couchdb'
alias start_couch='/usr/bin/sudo launchctl load -w /Library/LaunchDaemons/org.apache.couchdb.plist'
alias stop_couch='/usr/bin/sudo launchctl unload /Library/LaunchDaemons/org.apache.couchdb.plist'
alias cb='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/'
alias ws='cd /Users/rabshakeh/workspace'
alias ca='cd /Users/rabshakeh/workspace/cryptobox/couchdb_api/'
alias cr='cd /Users/rabshakeh/workspace/cryptobox/crypto_api'
alias ct='cd /Users/rabshakeh/workspace/cryptobox/crypto_tree'
alias com='/Users/rabshakeh/workspace/git_utils/commitfast.sh;'
alias cpa='/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/run_cp_all.sh;'
alias n1='ssh node1-eu.a8.nl'
alias d1='ssh data1-eu.a8.nl'
alias gcom='git commit -am "-" > /dev/null; git status'
alias gstats='git status'
alias gpush='git commit -am "-"; git push'
alias gpull='git pull'
alias upgrade="sudo ls; brew update; brew upgrade; brew doctor; brew cleanup -s --force; sudo gem update bropages; sudo /Users/rabshakeh/upgradepython.sh"
alias compush='/Users/rabshakeh/workspace/git_utils/commitfast.sh;  /Users/rabshakeh/workspace/git_utils/push.sh;'
alias pullcompush='/Users/rabshakeh/workspace/git_utils/pull.sh; /Users/rabshakeh/workspace/git_utils/commitfast.sh; /Users/rabshakeh/workspace/git_utils/push.sh;'
alias pull='/Users/rabshakeh/workspace/git_utils/pull.sh;'
alias push='/Users/rabshakeh/workspace/git_utils/push.sh;'
alias stats='/Users/rabshakeh/workspace/git_utils/status.sh;'
export PYRO_HMAC_KEY="sdhjfghvgchjgfuyeaguy"
export PYTHONPATH=${PYTHONPATH}:$HOME/gsutil/third_party/boto:$HOME/gsutil;
alias app='cd /Users/rabshakeh/workspace/cryptobox/cryptobox_app/source/commands/'
alias commit="git commit -am '-'"
ulimit -n 10000
export BOTO_PATH="/Users/rabshakeh/.boto"

# The next line updates PATH for the Google Cloud SDK.
export PATH=/Users/rabshakeh/google-cloud-sdk/bin:$PATH

# The next line enables bash completion for gcloud.
source /Users/rabshakeh/google-cloud-sdk/arg_rc

export DATASTORE_HOST="http://localhost:8080"
export DATASTORE_DATASET="cryptobox2013"
#export DATASTORE_SERVICE_ACCOUNT="1077532276852@developer.gserviceaccount.com"
#export DATASTORE_PRIVATE_KEY_FILE="/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/c839e87ac6666dac54456db3d86a82f68c18dfc1-privatekey.p12"

