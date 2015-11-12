#!/usr/bin/env python3
import argparse

import re
import requests
import time


def download_file_from_internet(path_from_internet, path_to_disk):
    with open(path_to_disk, 'wb') as handle:
        t = time.time()

        response = requests.get(path_from_internet, stream=True)
        length = int(response.headers['Content-Length'])

        print(path_to_disk)
        print('    size: {}  ({:.3f} Mb)'.format(length, length / (1024.0 * 1024.0)))
        print('    data: {}'.format(response.headers['Last-Modified']))

        block_size = 1024 * 256  # 256 kb
        i = 0
        for block in response.iter_content(block_size):
            print("progress: {:7.2%}".format(i * block_size / length))
            i += 1
            handle.write(block)

        print("progress: 100.00%\n")
        sec = time.time() - t
        print("done. [time: {:.3f} sec    speed: {:.3f} Mb/sec]".format(sec, float(length / (1024.0 * 1024.)) / sec))


def command_line_parse():
    parser = argparse.ArgumentParser(description='installer gentoo linux')
    parser.add_argument('--download', choices=["all", "portage", "stage3"], help='download portage and stage3')
    return parser.parse_args()


def download_portage():
    portage = 'portage-latest.tar.bz2'
    path_to_portage = 'http://mirror.yandex.ru/gentoo-distfiles/snapshots/' + portage
    download_file_from_internet(path_to_portage, portage)


def download_stage3():
    path_to_stage3 = 'http://mirror.yandex.ru/gentoo-distfiles/releases/amd64/autobuilds/current-stage3-amd64/'
    response = requests.get(path_to_stage3)
    text = str(response.content)
    pattern = re.compile('<a href="stage3-amd64-(\d+).tar.bz2">')
    path_to_stage3 = path_to_stage3 + 'stage3-amd64-{}.tar.bz2'.format(pattern.findall(text)[0])
    download_file_from_internet(path_to_stage3, 'stage3-amd64-latest.tar.bz2')


def download_install_files(download: str) -> str:
    if download in ['all', 'portage']:
        download_portage()

    if download in ['all', 'stage3']:
        download_stage3()


def main():
    args = command_line_parse()
    download_install_files(args.download)
    print(args)


if __name__ == "__main__":
    main()
