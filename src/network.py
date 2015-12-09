from general import create_file

import subprocess
import os

def configure(path_to_root):

    with create_file('/etc/conf.d/hostname') as f:
        print('hostname="zion"', file=f)

    with create_file('/etc/conf.d/net') as f:
        print('config_eth0="dhcp"', file=f)
        print('config_eth1="dhcp"', file=f)

    os.chdir('/etc/init.d')
    os.system('ln -s net.lo net.eth0')
    os.system('rc-update add net.eth0 default')
