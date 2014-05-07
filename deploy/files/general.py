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


def configure_print(name):
    print('configure {:.>25s}'.format(name))
