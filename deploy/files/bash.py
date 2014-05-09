#!/usr/bin/env python3.4
import multiprocessing

from pathlib import Path
from general import create_dir, create_file, configure_print


def configure(config):
    configure_print('bash')
    user_name = config['user_name']
    path_to_home = Path(config['path_to_root'], 'home', user_name)

    with create_file(Path(path_to_home, '.bashrc')) as f:
        print("""

PS1='\\[\\e[1;32m\\]\\u \\[\\e[0;31m\\] [\\[\\e[1;34m\\]\\w \\[\\e[0;31m\\]] \\[\\e[1;37m\\]{\\t}\\n\\$ ' """ + """

export CHROMIUM_USER_FLAGS="--disk-cache-dir=/tmp/chromium-cache-{} --scroll-pixels=250 --memory-model=high --disk-cache-size={}"

shopt -s histappend
PROMPT_COMMAND='history -a'
shopt -s cdspell
shopt -s dirspell

#export ANDROID_NDK=/opt/android-ndk/
#export ANDROID_STANDALONE_TOOLCHAIN=/opt/android-ndk/toolchains/
#LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/cuda/lib64

PATH=$PATH:/opt/sublime-text2/

alias l="ls -lh"
alias ll="ls -lah"
alias news="ls -lsaht | head -n 25"

alias m="make"
alias n="ninja"
alias sl="/opt/sublime-text2/sublime_text"
alias mm="make -j{}"
alias hddfree="du -h --max-depth=1 | sort -h"
alias ..="cd .."
alias ...="cd ../.."

source ~/.git-completion.bash

bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'""".format(user_name, str(256 * 1024 * 1024), str(multiprocessing.cpu_count() + 1)), file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)