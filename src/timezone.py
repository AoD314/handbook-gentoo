import sys
import subprocess

from general import Dir, create_file

def configure():
    print('configure timezone ... ', end='')
    sys.stdout.flush()
    
    with create_file('/etc/timezone') as f:
        print('Europe/Moscow', file=f)
    print(subprocess.getstatusoutput('emerge --config sys-libs/timezone-data'))

