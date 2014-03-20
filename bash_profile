export CLICOLOR=1
export LSCOLORS=ExFxCxDxBxegedabagacad


export PATH=/usr/local/bin:/usr/local/share/npm/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/rabshakeh/workspace/depot_tools
export LC_ALL=en_US.UTF-8
function _google() { 
  open 'https://www.google.nl/search?site=&source=hp&q='$1+$2+$3+$4+$5
}
export PYRO_HMAC_KEY="sdhjfghvgchjgfuyeaguy"
export PYTHONPATH=${PYTHONPATH}:$HOME/gsutil/third_party/boto:$HOME/gsutil;
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

alias app='cd /Users/rabshakeh/workspace/cryptobox/cryptobox_app/source/commands/'
alias ca='cd /Users/rabshakeh/workspace/cryptobox/crypto_data/'
alias cb='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/'
alias com='/Users/rabshakeh/workspace/git_utils/commitfast.sh;'
alias comm='cd /Users/rabshakeh/workspace/git_utils; python make_exclude_dirs.py; /Users/rabshakeh/workspace/git_utils/commit.sh;'
alias commit='git commit -am '\''-'\'''
alias compush='/Users/rabshakeh/workspace/git_utils/commitfast.sh; /Users/rabshakeh/workspace/git_utils/push.sh'
alias cpa='/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/run_cp_all.sh;'
alias cr='cd /Users/rabshakeh/workspace/cryptobox/crypto_api'
alias createcb='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl;/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/create/create_cryptobox.sh;'
alias ct='cd /Users/rabshakeh/workspace/cryptobox/crypto_taskworker'
alias ctr='cd /Users/rabshakeh/workspace/cryptobox/crypto_tree'
alias cw='/Users/rabshakeh/workspace/cryptobox/crypto_taskworker/starter.py'
alias cwv='/Users/rabshakeh/workspace/cryptobox/crypto_taskworker/starter.py -v'
alias cwkill='python /Users/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill.py -n "x"'
alias cwkillall='python /Users/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill_all.py -n "x"'
alias down='cd; cd Downloads'
alias dump='/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/create/make_local_copy_databases.sh'
alias flush='echo '\''flush_all'\'' | nc localhost 11211'
alias gcom='git commit -am "-" > /dev/null; git status'
alias google='_google'
alias gpull='git pull'
alias gpush='git push'
alias gstats='git status'
alias j2c='js2coffee -X -i4 test.js > test.coffee'
alias kp='killall python; killall Python'
alias mov='cd /Users/rabshakeh/Movies/Wondershare; python convertm4b.py'
alias n1='ssh node1-us.a8.nl'
alias pull='/Users/rabshakeh/workspace/git_utils/pull.sh;'
alias pullcompush='/Users/rabshakeh/workspace/git_utils/pull.sh; /Users/rabshakeh/workspace/git_utils/commitfast.sh; /Users/rabshakeh/workspace/git_utils/push.sh;'
alias push='/Users/rabshakeh/workspace/git_utils/push.sh;'
alias res='cd /Users/rabshakeh/workspace/research'
alias restart_couch='/usr/bin/sudo launchctl stop org.apache.couchdb'
alias rredis='launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.redis.plist; launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist'
alias scr='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts'
alias stats='/Users/rabshakeh/workspace/git_utils/status.sh;'
alias startdata='nohup /Users/rabshakeh/workspace/google/gcd-v1beta2-rev1-2.1.1/gcd.sh start /Users/rabshakeh/workspace/google/cryptobox2013/ &'
alias test='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/test'
alias todo='vi /etc/motd'
alias updatedb='sudo date; sudo /usr/libexec/locate.updatedb &'
alias upgrade='sudo ls > /dev/null; brew update; brew upgrade; brew doctor; brew cleanup -s --force; sudo gem update bropages; sudo /Users/rabshakeh/upgradepython.sh'
alias ws='cd /Users/rabshakeh/workspace'

