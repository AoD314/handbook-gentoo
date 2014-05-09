#!/usr/bin/env python3.4

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('locale')

    with create_file(Path(config['path_to_root'], 'etc/locale.gen')) as f:
        print("""
en_US.UTF-8 UTF-8

ru_RU.UTF-8 UTF-8
""", file=f)

    with create_file(Path(config['path_to_root'], 'etc/environment')) as f:
        print("""
LANG="en_US.UTF-8"
""", file=f)

    with create_file(Path(config['path_to_root'], 'etc/conf.d/consolefont')) as f:
        print("""
consolefont="LatArCyrHeb-16"
""", file=f)

    with create_file(Path(config['path_to_root'], 'etc/conf.d/keymaps')) as f:
        print("""
keymap="us"
windowkeys="yes"
extended_keymaps=""
dumpkeys_charset=""
fix_euro="no"
""", file=f)

    with create_file(Path(config['path_to_root'], 'etc/conf.d/hwclock')) as f:
        print("""
clock="local"
""", file=f)





if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)