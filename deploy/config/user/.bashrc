
export HISTFILESIZE=614000
export HISTSIZE=314000
export HISTIGNORE="&:ls:pwd:l:ll:..:cd:cd ..:n"
export HISTCONTROL="ignoredups"

export CHROMIUM_USER_FLAGS="--disk-cache-dir=/tmp --disk-cache-size=50000000"


shopt -s histappend
PROMPT_COMMAND='history -a'
shopt -s cdspell


PATH=$PATH:/opt/bin:/opt/sublime-text2/

export ANDROID_NDK=/opt/android-ndk/
export ANDROID_STANDALONE_TOOLCHAIN=/opt/android-ndk/toolchains/

#PATH=$PATH:/opt/cuda/bin:/opt/intel/Compiler/11.1/072/bin/intel64
#LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/lib64:/opt/intel/Compiler/11.1/072/lib/intel64

alias l="ls -lh"
alias ll="ls -lah"
alias lm="ls -lah | more "
alias news="ls -lsaht | head -n 25"

alias m="make"
alias n="ninja"
alias sl="/opt/sublime-text2/sublime_text"
alias mm="make -j12"

alias hddfree="du -h --max-depth=1 | sort -h"

alias ..="cd .."
alias ...="cd ../.."

shopt -s cdspell
shopt -s cmdhist

source ~/.git-completion.bash

HISTIGNORE="&:pwd:ls:ls -l:ls -la:ll:cd:cd \-:cd /:cd .."

. /etc/profile

PS1='\[\e[1;32m\]\u \[\e[0;31m\] [\[\e[1;34m\]\w \[\e[0;31m\]] \[\e[1;37m\]{\t}\n\$ '

PATH="/usr/lib/ccache/bin/:${PATH}"
export PATH=${PATH}


# ~/.bashrc
# bind '"\e[A": history-search-backward'
# bind '"\e[B": history-search-forward'
