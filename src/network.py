from general import create_file, run_command

import os


def configure():

    with create_file('/etc/conf.d/hostname') as f:
        print('hostname="zion"', file=f)

    with create_file('/etc/conf.d/net') as f:
        print('config_eth0="dhcp"', file=f)
        print('config_eth1="dhcp"', file=f)
        
    run_command("emerge -v1 net-misc/dhcpcd")

    os.chdir('/etc/init.d')
    os.system('ln -s net.lo net.eth0')
    os.system('rc-update add net.eth0 default')
