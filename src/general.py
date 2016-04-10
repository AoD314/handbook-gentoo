
from datetime import datetime
from pathlib import Path
import os
import sys
import subprocess


def create_dir(dir_name):
    name = Path(dir_name)
    if name.is_file():
        raise (str(name) + ' is file')
    if not name.exists():
        name.mkdir(parents=True)
        print('create directory ' + str(name))


def create_file(file_name):
    name = Path(file_name)
    create_dir(name.parent)
    if name.exists():
        name.unlink()
    print('create file ' + str(name))
    return open(str(name), 'w')


def run_command(cmd):
    print_log(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print_log(line)
    print_log('status '+ str(p.wait()))
    

def print_log(msg):
    print(msg)
    sys.stdout.flush()
    with open('/tmp/gentoo_install.log', 'a') as f:
        f.write(str(datetime.now()) + ": " + str(msg))


class Dir():
    def __init__(self, base_path):
        self.path = base_path

    def full(self, path):
        if len(path) > 0:
            path = path[1:] if path[0] == '/' else path
        return str(Path(self.path, path))
