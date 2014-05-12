#!/usr/bin/env python3.4

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('locale')

    with create_file(Path(config['path_to_root'], 'etc/locale.gen')) as f:
        print("""
ru_RU.UTF-8 UTF-8
en_US.UTF-8 UTF-8
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
clock="UTC"
clock_args=""
""", file=f)

    with create_file(Path(config['path_to_root'], 'etc/ntp.conf')) as f:
        print("""
# Common pool for random people
#server pool.ntp.org

server ntp1.stratum2.ru
server ntp2.stratum2.ru
server ntp3.stratum2.ru

server ntp1.stratum1.ru
server ntp2.stratum1.ru
server ntp3.stratum1.ru

# Pools for Gentoo users
server 0.gentoo.pool.ntp.org
server 1.gentoo.pool.ntp.org
server 2.gentoo.pool.ntp.org
server 3.gentoo.pool.ntp.org


driftfile       /var/lib/ntp/ntp.drift

restrict default nomodify nopeer noquery limited kod
restrict 127.0.0.1
restrict [::1]
""", file=f)





if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)