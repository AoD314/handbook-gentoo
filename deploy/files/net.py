#!/usr/bin/env python3.4

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('network')

    with create_file(Path(config['path_to_root'], 'etc/conf.d/net')) as f:
        print('config_eth0="dhcp"', file=f)
        print('hostname="neo"', file=f)

    with create_file(Path(config['path_to_root'], 'etc/resolv.conf')) as f:
        print('nameserver 192.168.0.1', file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)