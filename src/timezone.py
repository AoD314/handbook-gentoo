import sys
import subprocess

from general import Dir, create_file

def configure():
    with create_file('/etc/timezone') as f:
        print('Europe/Moscow', file=f)
    print(subprocess.getoutput('emerge --config sys-libs/timezone-data'))

