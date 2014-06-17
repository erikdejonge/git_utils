export LDFLAGS='-L/usr/local/opt/openssl/lib'
export CPPFLAGS='-I/usr/local/opt/openssl/include'
# build pycrypto
# sudo ln -s /usr/local/Cellar/gmp/5.1.3/lib/libgmp.dylib /usr/lib/libgmp.dylib
# ARCHFLAGS=-Wno-error CFLAGS=-I/usr/local/Cellar/gmp/5.1.3/include sudo -E pip install pycrypto
# ARCHFLAGS=-Wno-error CFLAGS=-I/usr/include sudo -E pip install pycrypto
export HOMEBREW_BUILD_FROM_SOURCE=1

export CLICOLOR=1
export LSCOLORS=ExFxCxDxBxegedabagacad


export PATH=/usr/local/sbin:/usr/local/bin:/usr/local/share/npm/bin:/usr/bin:/bin:/usr/sbin:/sbin:/cygdrive/d/workarea/depot_tools
export LC_ALL=en_US.UTF-8
function _google() {
  open 'https://www.google.nl/search?site=&source=hp&q='$1+$2+$3+$4+$5
}
export PYRO_HMAC_KEY="sdhjfghvgchjgfuyeaguy"
ulimit -n 10000
export BOTO_PATH="/Users/rabshakeh/.boto"

export DATASTORE_HOST="http://localhost:8080"
export DATASTORE_DATASET="cryptobox2013"
#export DATASTORE_SERVICE_ACCOUNT="1077532276852@developer.gserviceaccount.com"
#export DATASTORE_PRIVATE_KEY_FILE="/cygdrive/d/workarea/cryptobox/www_cryptobox_nl/c839e87ac6666dac54456db3d86a82f68c18dfc1-privatekey.p12"
alias app='cd /cygdrive/d/workarea/cryptobox/cryptobox_app/source/commands/'
alias ca='cd /cygdrive/d/workarea/cryptobox/crypto_data/'
alias cb='cd /cygdrive/d/workarea/cryptobox/www_cryptobox_nl'
alias cbbuildfrontend='/cygdrive/d/workarea/cryptobox/www_cryptobox_nl/scripts/build/build_frontend.sh'
alias cls='printf "\033c"'
alias com='/cygdrive/d/workarea/git_utils/commitfast.sh;'
alias comm='cd /cygdrive/d/workarea/git_utils; python make_exclude_dirs.py; /cygdrive/d/workarea/git_utils/commit.sh;'
alias commit='git commit -am '\''-'\'''
alias compush='tar -cf /cygdrive/d/workarea/cryptobox/idea.tar /cygdrive/d/workarea/cryptobox/.idea 2>&1 | grep -v "Removing leading"; mv /cygdrive/d/workarea/cryptobox/idea.tar /cygdrive/d/workarea/cryptobox/www_cryptobox_nl/scripts/var; /cygdrive/d/workarea/git_utils/commitfast.sh; /cygdrive/d/workarea/git_utils/push.sh'
alias cpa='/cygdrive/d/workarea/cryptobox/www_cryptobox_nl/scripts/run_cp_all.sh;'
alias cr='cd /cygdrive/d/workarea/cryptobox/crypto_api'
alias createcb='cd /cygdrive/d/workarea/cryptobox/crypto_data/; python delete_database.py -f; cd /cygdrive/d/workarea/cryptobox/www_cryptobox_nl;/cygdrive/d/workarea/cryptobox/www_cryptobox_nl/scripts/create/create_cryptobox.sh'
alias ct='cd /cygdrive/d/workarea/cryptobox/crypto_taskworker'
alias ctr='cd /cygdrive/d/workarea/cryptobox/crypto_tree'
alias cw='clear; /cygdrive/d/workarea/cryptobox/crypto_taskworker/starter.py'
alias cwv='printf "\033c"; /cygdrive/d/workarea/cryptobox/crypto_taskworker/starter.py -v -w 1'
alias cwkill='python /cygdrive/d/workarea/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill.py -n "x"'
alias cwvkill='python /cygdrive/d/workarea/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill.py -n "x"'
alias cwkillall='python /cygdrive/d/workarea/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill_all.py -n "x"'
alias cwvkillall='python /cygdrive/d/workarea/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill_all.py -n "x"'
alias deletecb='cd /cygdrive/d/workarea/cryptobox/www_cryptobox_nl;/cygdrive/d/workarea/cryptobox/www_cryptobox_nl/scripts/create/delete_cryptobox.sh;'
alias desk='cd /Users/rabshakeh/Desktop'
alias down='cd; cd Downloads'
alias dump='/cygdrive/d/workarea/cryptobox/www_cryptobox_nl/scripts/create/make_local_copy_databases.sh'
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
alias pull='/cygdrive/d/workarea/git_utils/pull.sh;'
alias pullcompush='/cygdrive/d/workarea/git_utils/pull.sh; /cygdrive/d/workarea/git_utils/commitfast.sh; /cygdrive/d/workarea/git_utils/push.sh;'
alias push='/cygdrive/d/workarea/git_utils/push.sh;'
alias res='ssh 188.226.155.145'
alias restart_safe='sudo nvram boot-args="-x";sudo shutdown -r now'
alias restart_normal='sudo nvram boot-args="";sudo shutdown -r now'
alias rmpyc="find . -type f -name '*.pyc' -exec rm {} \;"
alias rmdstore="find . -name \".DS_Store\" -depth -exec rm {} \;"
alias rredis='launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.redis.plist; launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist'
alias scr='cd /cygdrive/d/workarea/cryptobox/www_cryptobox_nl/scripts'
alias stats='/cygdrive/d/workarea/git_utils/status.sh;'
alias startdata='nohup /cygdrive/d/workarea/google/gcd-v1beta2-rev1-2.1.1/gcd.sh start /cygdrive/d/workarea/google/cryptobox2013/ &'
alias test='cd /cygdrive/d/workarea/cryptobox/www_cryptobox_nl/scripts/test'
alias todo='vi /etc/motd'
alias touchall='find . -name "*.coffee" -exec touch {} \;'
alias updatedb='sudo date; sudo /usr/libexec/locate.updatedb &'
alias upgrade="sudo date; brew update; brew upgrade; brew doctor; brew cleanup -s --force; sudo gem update bropages; sudo python /cygdrive/d/workarea/research/upgrade_python_packs.py; gcloud -q components update;"
alias verifydisk='diskutil verifyVolume /'
alias ws='cd /cygdrive/d/workarea'
alias www='cd /cygdrive/d/workarea/cryptobox/www_cryptobox_nl/source/coffee'

export PATH=/usr/local/sbin:$PATH

# The next line updates PATH for the Google Cloud SDK.
source /Users/rabshakeh/google-cloud-sdk/path.bash.inc

# The next line enables bash completion for gcloud.
source /Users/rabshakeh/google-cloud-sdk/completion.bash.inc


export PYTHONPATH=${PYTHONPATH}:/cygdrive/d/workarea/cryptobox:/cygdrive/d/workarea/cryptobox/www_cryptobox_nl:/usr/local/lib/python2.7/site-packages/gcs_oauth2_boto_plugin
export PYTHONPATH=`brew --prefix`/lib/python2.7/site-packages:$PYTHONPATH
