import sys
import subprocess

from general import create_file, run_command

def configure():
    with create_file('/etc/timezone') as f:
        print('Europe/Moscow', file=f)

    run_command('emerge --config sys-libs/timezone-data')

