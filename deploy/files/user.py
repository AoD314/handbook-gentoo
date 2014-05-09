#!/usr/bin/env python3.4

from pathlib import Path
from general import create_file, configure_print


def configure(config):
    configure_print('user')


if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)