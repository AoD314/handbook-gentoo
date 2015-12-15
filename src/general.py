
import subprocess
import sys

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
    print(cmd, end='')
    sys.stdout.flush()
    (status, output) = subprocess.getstatusoutput(cmd)
    print(' (status: ' + str(status) + ')')
    print(output)
    print('\n')


def configure_print(name):
    print('configure {:.>25s}'.format(name))


class Dir():
    def __init__(self, base_path):
        self.path = base_path

    def full(self, path):
        if len(path) > 0:
            path = path[1:] if path[0] == '/' else path
        return str(Path(self.path, path))
