#!/usr/bin/env python3.4

from pathlib import Path
from general import create_file, configure_print


def configure(config):
    configure_print('locale')

    with create_file(Path(config['path_to_root'], 'etc/conf.d/net')) as f:
        print('config_eth0="dhcp"', file=f)
        print('hostname="neo"', file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)