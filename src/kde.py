from general import create_file

import subprocess

def configure():
    with create_file('/etc/conf.d/xdm') as f:
        print('DISPLAYMANAGER="kdm"', file=f)

    print(subprocess.getoutput('emerge -1v x11-apps/xdm kde-apps/kdebase-meta'))
    print(subprocess.getoutput('rc-update add xdm default'))
