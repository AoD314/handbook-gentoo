#!/usr/bin/env python3.4

import multiprocessing
from pathlib import Path
import subprocess
import math
from general import create_file, configure_print


def get_sse_support():
    r = ' '
    cpu_flags = subprocess.getoutput('cat /proc/cpuinfo | grep flags | uniq')
    inst = 'sse sse2 sse3 ssse3 sse4 sse4_1 sse4_2 avx avx2'.split(' ')
    for i in inst:
        if i in cpu_flags:
            r += i + ' '
    return r


def configure(config):
    configure_print('make.conf')
    path_to_root = config['path_to_root']
    print('see ' + str(Path(path_to_root, 'usr/share/portage/config/make.conf.example')) + ' for examples')

    with create_file(Path(path_to_root, 'etc/portage/make.conf')) as f:
        sse = get_sse_support().strip()
        last_sse = '-m' + sse.split(' ')[-1].replace('_', '.')
        print('\nUSE="nls qt4 qt5 theora gmp posix usb png ogg udev threads xvid webm x264 ogg flac opengl policykit consolekit vdpau utf8 c++11 wayland ipv6 -semantic-desktop ' + sse + '"', file=f)
        print('CHOST="x86_64-pc-linux-gnu"', file=f)
        print('CFLAGS="-O3 -pipe -march=native ' + last_sse + ' -mpopcnt -fomit-frame-pointer -funroll-loops -fschedule-insns -fsched-pressure"\nCXXFLAGS="${CFLAGS}"', file=f)
        print('LINGUAS="ru"\nACCEPT_LICENSE="*"\n', file=f)
        print('INPUT_DEVICES="evdev keyboard mouse virtualbox"\nVIDEO_CARDS="nvidia"\n', file=f)
        print('MAKEOPTS="-j' + str(multiprocessing.cpu_count() + 1) + '"', file=f)
        print('EMERGE_DEFAULT_OPTS="--jobs=' + str(int(math.sqrt(multiprocessing.cpu_count()))) + '"', file=f)
        print('\nPORTDIR_OVERLAY=/usr/local/portage', file=f)
        print('PORTDIR=/usr/portage', file=f)
        print('PORTAGE_TMPDIR=/tmp', file=f)
        print('\nsource "/var/lib/layman/make.conf"', file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)
