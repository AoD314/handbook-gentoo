
import subprocess
import sys
import os

from pathlib import Path

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
    #os.system(cmd)
    print(cmd)
    print('_' * 120)
    #(status, output) = subprocess.getstatusoutput(cmd)
    #print(output)

    proc = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE)
    line = ' '
    while True:
        line = proc.stdout.readline()
        if not line: break

        line = line.decode('utf-8').strip()
        print(line)

    status = proc.returncode

    print('\n----> (status: ' + str(status) + ')')
    print('\n\n')


def configure_print(name):
    print('configure {:.>25s}'.format(name))


class Dir():
    def __init__(self, base_path):
        self.path = base_path

    def full(self, path):
        if len(path) > 0:
            path = path[1:] if path[0] == '/' else path
        return str(Path(self.path, path))
