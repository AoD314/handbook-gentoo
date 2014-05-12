#!/usr/bin/env python3.4
import multiprocessing

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('bash')
    user_name = config['user_name']
    path_to_home = Path(config['path_to_root'], 'home', user_name)

    with create_file(Path(path_to_home, '.bashrc')) as f:
        print("""

PS1='\[\e[1;32m\]\u \[\e[0;31m\] [\[\e[1;34m\]\w \[\e[1;32m\]$(__git_ps1 "(%s)")\[\e[0;31m\]] \[\e[1;37m\]{\t}\n\$ '

shopt -s histappend
PROMPT_COMMAND='history -a'
shopt -s cdspell
shopt -s dirspell

#export ANDROID_NDK=/opt/android-ndk/
#export ANDROID_STANDALONE_TOOLCHAIN=/opt/android-ndk/toolchains/
#LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/lib64

PATH=$PATH:/opt/sublime-text2/

alias gr="grep -niIHR"
alias htop="htop -d 2"

alias l="ls -lh"
alias lS="ls -lSh"
alias ll="ls -lah"
alias bigs="ls -Shal | head -n 25"
alias news="ls -lsaht | head -n 25"
alias hotm="ps -A -o rssize:10,time:9,%cpu:5,cmd | sort -nr | head | awk '{ printf \"%7.1f M  --- %s\n\", \$1/1024, \$4}{};'"
alias hotc="ps -A -o rssize:10,time:9,%cpu:5,cmd --sort -%cpu | head -n 13 | awk '{ printf \"%6.1f%% --- %s\n\", \$3, \$4}{};' | tail -n 12"

alias m="make -j5"
alias n="ninja"
alias sl="sublime_text"

alias hddfree="du -h --max-depth=1 | sort -h"

source ~/.git-completion.bash

bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'
""".format(user_name, str(256 * 1024 * 1024), str(multiprocessing.cpu_count() + 1)), file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)