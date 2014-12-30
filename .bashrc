# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

export CLICOLOR=1
export LSCOLORS=ExFxCxDxBxegedabagacad


export PATH=/usr/local/sbin:/usr/local/bin:/usr/local/share/npm/bin:/usr/bin:/bin:/usr/sbin:/sbin:/home/rabshakeh/workspace/depot_tools
export LC_ALL=en_US.UTF-8
function _google() {
  open 'https://www.google.nl/search?site=&source=hp&q='$1+$2+$3+$4+$5
}
export PYRO_HMAC_KEY="sdhjfghvgchjgfuyeaguy"
export BOTO_PATH="/home/rabshakeh/.boto"

function _concatmp3() {
  echo "concatting mp3's and making audiobook" $1'.m4b'
  sleep 1
  find *|grep .mp3|while read f; do echo "file '$f'" >> mylist.txt; done
  wait
  ffmpeg -f concat -i mylist.txt -c copy $1".mp3"
  sleep 5
  wait
  ffmpeg -i $1".mp3" -threads 8 -metadata album=$1 -metadata title=$1 -vn $1'.m4a'
  sleep 5
  wait
  mv $1'.m4a' $1'.m4b'
  wait
  rm $1'.mp3'

  rm mylist.txt
}
function _mdcat() {
  markdown $1 | lynx -stdin
}
function _opendir() {
  python /home/rabshakeh/workspace/research/openfolder.py --fp=$1
}
#export DATASTORE_HOST="http://localhost:8080"
#export DATASTORE_DATASET="cryptobox2013"
#export DATASTORE_SERVICE_ACCOUNT="1077532276852@developer.gserviceaccount.com"
#export DATASTORE_PRIVATE_KEY_FILE="/home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/privatekey.pem"
#export OAUTH2_CLIENT_ID="32555940559.apps.googleusercontent.com"
#export OAUTH2_CLIENT_SECRET="ZmssLNjJy2998hD4CTg2ejr2"
alias app='cd /home/rabshakeh/workspace/cryptobox/cryptobox_app/source/commands/'
alias androidemu='"/Applications/Android Studio.app/sdk/tools/emulator" -avd android -netspeed full -netdelay none'
alias act='open /Applications/Utilities/Activity\ Monitor.app'
alias ca='cd /home/rabshakeh/workspace/cryptobox/crypto_data/'
alias cb='cd /home/rabshakeh/workspace/cryptobox/www_cryptobox_nl'
alias cbd='cd /home/rabshakeh/workspace/cryptobox/cryptobox_design'
alias cbbuildfrontend='/home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/build/build_frontend.sh'
alias cls='printf "\033c"'
alias com='/home/rabshakeh/workspace/git_utils/commitfast.sh;'
alias comm='cd /home/rabshakeh/workspace/git_utils; python make_exclude_dirs.py; /home/rabshakeh/workspace/git_utils/commit.sh; /home/rabshakeh/workspace/git_utils/push.sh'
alias commit='git commit -am '\''-'\'''
alias compush='/home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/deploy/rsyncdesign.sh&&tar -cf /home/rabshakeh/workspace/cryptobox/idea.tar /home/rabshakeh/workspace/cryptobox/.idea 2>&1 | grep -v "Removing leading"; mv /home/rabshakeh/workspace/cryptobox/idea.tar /home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/var; /home/rabshakeh/workspace/git_utils/commitfast.sh; /home/rabshakeh/workspace/git_utils/push.sh; wait'
alias concatmp3='_concatmp3'
alias cpa='/home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/run_cp_all.sh;'
alias cr='cd /home/rabshakeh/workspace/cryptobox/crypto_api'
alias createcb='cd /home/rabshakeh/workspace/cryptobox/www_cryptobox_nl;/home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/create/create_cryptobox.sh'
alias ct='cd /home/rabshakeh/workspace/cryptobox/cryptobox_containers'
alias ctr='cd /home/rabshakeh/workspace/cryptobox/crypto_tree'
alias cw='clear; /home/rabshakeh/workspace/cryptobox/crypto_taskworker/starter.py'
alias cwv='printf "\033c"; /home/rabshakeh/workspace/cryptobox/crypto_taskworker/starter.py -v -w 1'
alias cwkill='python /home/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill.py -n "x"'
alias cwvkill='python /home/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill.py -n "x"'
alias cwkillall='python /home/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill_all.py -n "x"'
alias cwvkillall='python /home/rabshakeh/workspace/cryptobox/crypto_taskworker/cmd_crypto_taskworker_kill_all.py -n "x"'
alias deletecb='cd /home/rabshakeh/workspace/cryptobox/www_cryptobox_nl;/home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/create/delete_cryptobox.sh;'
alias desk='cd /home/rabshakeh/Desktop'
alias down='cd; cd Downloads'
alias dump='/home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/create/make_local_copy_databases.sh'
alias flush='redis-cli flushall; celery purge -f'
alias gcom='git commit -am "-" > /dev/null; git status'
alias ghb="cd /home/rabshakeh/workspace/github"
alias google='_google'
alias gpull='git pull'
alias gpush='git push'
alias gcompush='git commit -am "-" > /dev/null&&git push'
alias gstats='git status'
alias j2c='js2coffee -X -i4 test.js > test.coffee'
alias kp='killall python; killall Python; redis-cli flushall;killall python; killall Python;'
alias locate='/home/rabshakeh/workspace/research/locate.py'
alias lnd='ssh lycianode.a8.nl'
alias ly2='ssh 192.168.14.7'
alias mdcat='_mdcat'
alias mov='cd /home/rabshakeh/Movies/Wondershare; python convertm4b.py'
alias n1='ssh node1-us.a8.nl'
alias n2='ssh node2-us.a8.nl'
alias nxrestart='nginx -s stop; nginx'
alias opendir='_opendir'
alias pull='python /home/rabshakeh/workspace/git_utils/pull_all_git_folders.py -i'
alias pullall='python /home/rabshakeh/workspace/git_utils/pull_all_git_folders.py'
alias pullcompush='/home/rabshakeh/workspace/git_utils/pull.sh; /home/rabshakeh/workspace/git_utils/commitfast.sh; /home/rabshakeh/workspace/git_utils/push.sh;'
alias push='/home/rabshakeh/workspace/git_utils/push.sh;'
alias setp3='unset PYTHONPATH;'
alias sf='cd /home/rabshakeh/workspace/sort_photo;python sort_photos.py'
alias res='cd /home/rabshakeh/workspace/research'
alias restart_safe='sudo nvram boot-args="-x";sudo shutdown -r now'
alias restart_normal='sudo nvram boot-args="";sudo shutdown -r now'
alias rmpyc="find . -type f -name '*.pyc' -exec rm {} \;"
alias rmdstore="find . -name \".DS_Store\" -depth -exec rm {} \;"
alias rredis='launchctl unload ~/Library/LaunchAgents/homebrew.mxcl.redis.plist; launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist'
alias scr='cd /home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts'
alias stats='/home/rabshakeh/workspace/git_utils/status.sh;'
alias startdata='rm nohup.out; nohup /home/rabshakeh/workspace/google/gcd-v1beta2-rev1-2.1.1/gcd.sh start /home/rabshakeh/workspace/google/cryptobox2013/ &'
alias temp='cd /home/rabshakeh/workspace/temp'
alias test='cd /home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/scripts/test'
alias todo='vi /etc/motd'
alias top='python /home/rabshakeh/workspace/research/top.py'
alias touchall='find . -name "*.coffee" -exec touch {} \;&&find . -name "*.less" -exec touch {} \;'
alias updatedb='sudo date; sudo /usr/libexec/locate.updatedb'
alias upgrade="sudo date; brew update; brew cask update; brew upgrade; brew cleanup -s --force; python /home/rabshakeh/workspace/research/list_python_packages.py > /home/rabshakeh/workspace/research/upgrade_python_packs.sh; /home/rabshakeh/workspace/research/upgrade_python_packs.sh; gcloud -q components update; brew doctor&&gem update bropages&&cd /home/rabshakeh; boot2docker stop; boot2docker upgrade; boot2docker start;"
alias verifydisk='diskutil verifyVolume /'
alias ws='cd /home/rabshakeh/workspace'
alias www='cd /home/rabshakeh/workspace/cryptobox/www_cryptobox_nl/source/coffee'
alias wwwserver='python -m SimpleHTTPServer 8000'

