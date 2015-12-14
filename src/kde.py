from general import create_file

import os

def configure():
    with create_file('/etc/conf.d/xdm') as f:
        print('DISPLAYMANAGER="kdm"', file=f)

    os.system('emerge -1v kde-apps/kdebase-meta')
    os.system('rc-update add xdm default')
