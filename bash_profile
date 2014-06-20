export LDFLAGS='-L/usr/local/opt/openssl/lib'
export CPPFLAGS='-I/usr/local/opt/openssl/include'
# build pycrypto
# sudo ln -s /usr/local/Cellar/gmp/5.1.3/lib/libgmp.dylib /usr/lib/libgmp.dylib
# ARCHFLAGS=-Wno-error CFLAGS=-I/usr/local/Cellar/gmp/5.1.3/include sudo -E pip install pycrypto
# ARCHFLAGS=-Wno-error CFLAGS=-I/usr/include sudo -E pip install pycrypto
export HOMEBREW_BUILD_FROM_SOURCE=1

export CLICOLOR=1
export LSCOLORS=ExFxCxDxBxegedabagacad


export PATH=/usr/local/sbin:/usr/local/bin:/usr/local/share/npm/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/rabshakeh/workspace/depot_tools
export LC_ALL=en_US.UTF-8
function _google() { 
  open 'https://www.google.nl/search?site=&source=hp&q='$1+$2+$3+$4+$5
}
export PYRO_HMAC_KEY="sdhjfghvgchjgfuyeaguy"
ulimit -n 10000
export BOTO_PATH="/Users/rabshakeh/.boto"

#export DATASTORE_HOST="http://localhost:8080"
#export DATASTORE_DATASET="cryptobox2013"
#export DATASTORE_SERVICE_ACCOUNT="1077532276852@developer.gserviceaccount.com"
#export DATASTORE_PRIVATE_KEY_FILE="/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/privatekey.pem"
#export OAUTH2_CLIENT_ID="32555940559.apps.googleusercontent.com"
#export OAUTH2_CLIENT_SECRET="ZmssLNjJy2998hD4CTg2ejr2"
alias app='cd /Users/rabshakeh/workspace/cryptobox/cryptobox_app/source/commands/'
alias ca='cd /Users/rabshakeh/workspace/cryptobox/crypto_data/'
alias cb='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl'
alias cbbuildfrontend='/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/build/build_frontend.sh'
alias cls='printf "\033c"'
alias com='/Users/rabshakeh/workspace/git_utils/commitfast.sh;'
alias comm='cd /Users/rabshakeh/workspace/git_utils; python make_exclude_dirs.py; /Users/rabshakeh/workspace/git_utils/commit.sh;'
alias commit='git commit -am '\''-'\'''
alias compush='tar -cf /Users/rabshakeh/workspace/cryptobox/idea.tar /Users/rabshakeh/workspace/cryptobox/.idea 2>&1 | grep -v "Removing leading"; mv /Users/rabshakeh/workspace/cryptobox/idea.tar /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/var; /Users/rabshakeh/workspace/git_utils/commitfast.sh; /Users/rabshakeh/workspace/git_utils/push.sh'
alias cpa='/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/run_cp_all.sh;'
alias cr='cd /Users/rabshakeh/workspace/cryptobox/crypto_api'
alias createcb='cd /Users/rabshakeh/workspace/cryptobox/crypto_data/;cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl;/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/create/create_cryptobox.sh'
alias ct='cd /Users/rabshakeh/workspace/cryptobox/crypto_taskworker'
alias ctr='cd /Users/rabshakeh/workspace/cryptobox/crypto_tree'
alias cw='clear; /Users/rabshakeh/workspace/cryptobox/crypto_taskworker/starter.py'
alias cwv='printf "\033c"; /Users/rabshakeh/workspace/cryptobox/crypto_taskworker/starter.py -v -w 1'
alias cwkill='python /Users/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill.py -n "x"'
alias cwvkill='python /Users/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill.py -n "x"'
alias cwkillall='python /Users/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill_all.py -n "x"'
alias cwvkillall='python /Users/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill_all.py -n "x"'
alias deletecb='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl;/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/create/delete_cryptobox.sh;'
alias desk='cd /Users/rabshakeh/Desktop'
alias down='cd; cd Downloads'
alias dump='/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/create/make_local_copy_databases.sh'
alias flush='redis-cli flushall; celery purge -f'
alias gcom='git commit -am "-" > /dev/null; git status'
alias google='_google'
alias gpull='git pull'
alias gpush='git push'
alias gstats='git status'
alias j2c='js2coffee -X -i4 test.js > test.coffee'
alias kp='killall python; killall Python; redis-cli flushall'
alias locate='/usr/bin/mdfind'
alias ly2='ssh 192.168.14.7'
alias mov='cd /Users/rabshakeh/Movies/Wondershare; python convertm4b.py'
alias n1='ssh node1-us.a8.nl'
alias pull='/Users/rabshakeh/workspace/git_utils/pull.sh;'
alias pullcompush='/Users/rabshakeh/workspace/git_utils/pull.sh; /Users/rabshakeh/workspace/git_utils/commitfast.sh; /Users/rabshakeh/workspace/git_utils/push.sh;'
alias push='/Users/rabshakeh/workspace/git_utils/push.sh;'
alias res='cd /Users/rabshakeh/workspace/research'
alias restart_safe='sudo nvram boot-args="-x";sudo shutdown -r now'
alias restart_normal='sudo nvram boot-args="";sudo shutdown -r now'
alias rmpyc="find . -type f -name '*.pyc' -exec rm {} \;"
alias rmdstore="find . -name \".DS_Store\" -depth -exec rm {} \;"
alias rredis='launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.redis.plist; launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist'
alias scr='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts'
alias stats='/Users/rabshakeh/workspace/git_utils/status.sh;'
alias startdata='nohup /Users/rabshakeh/workspace/google/gcd-v1beta2-rev1-2.1.1/gcd.sh start /Users/rabshakeh/workspace/google/cryptobox2013/ &'
alias test='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/test'
alias todo='vi /etc/motd'
alias touchall='find . -name "*.coffee" -exec touch {} \;'
alias updatedb='sudo date; sudo /usr/libexec/locate.updatedb &'
alias upgrade="sudo date; brew update; brew upgrade; brew doctor; brew cleanup -s --force; sudo gem update bropages; sudo python /Users/rabshakeh/workspace/research/upgrade_python_packs.py; gcloud -q components update;"
alias verifydisk='diskutil verifyVolume /'
alias ws='cd /Users/rabshakeh/workspace'
alias www='cd /Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl/source/coffee'

export PATH=/usr/local/sbin:$PATH

# The next line updates PATH for the Google Cloud SDK.
source /Users/rabshakeh/google-cloud-sdk/path.bash.inc

# The next line enables bash completion for gcloud.
source /Users/rabshakeh/google-cloud-sdk/completion.bash.inc


export PYTHONPATH=${PYTHONPATH}:/Users/rabshakeh/google-cloud-sdk/platform/gsutil/third_party/gcs-oauth2-boto-plugin:/Users/rabshakeh/workspace/cryptobox:/Users/rabshakeh/workspace/cryptobox/www_cryptobox_nl:/usr/local/lib/python2.7/site-packages:/Users/rabshakeh/google-cloud-sdk/platform/gsutil/third_party/gcs-oauth2-boto-plugin:/Users/rabshakeh/google-cloud-sdk/platform/gsutil/third_party/gcs-oauth2-boto-plugin/gcs_oauth2_boto_plugin;
