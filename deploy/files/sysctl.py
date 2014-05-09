#!/usr/bin/env python3.4

from pathlib import Path
from general import create_file, configure_print


def configure(config):
    configure_print('sysctl.conf')

    with create_file(Path(config['path_to_root'], 'etc/sysctl.conf')) as f:
        print("""
net.ipv4.ip_forward = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.rp_filter = 1

vm.dirty_background_ratio = 50
vm.dirty_ratio = 85
vm.overcommit_memory = 1
vm.overcommit_ratio = 100
vm.swappiness=0
vm.vfs_cache_pressure = 1000
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)