#!/usr/bin/env python3.4

from pathlib import Path
from general import create_file, configure_print


def configure(config):
    configure_print('profile')

    with create_file(Path(config['path_to_root'], 'etc/profile')) as f:
        print("""
export HISTSIZE=8192
export HISTFILESIZE=$HISTSIZE
export HISTIGNORE="&:ls:[bf]g:exit:l:ll:cd ..:m:n:pwd:[ \t]*"
export HISTCONTROL=ignorespace:erasedups
export EIX_LIMIT_COMPACT=0
export EIX_LIMIT=0
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)