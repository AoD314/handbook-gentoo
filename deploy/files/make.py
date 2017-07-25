#!/usr/bin/env python3.4

import multiprocessing
from pathlib import Path
import subprocess
import math
from files.general import configure_print, create_file


def get_sse_support():
    # FIXME: run app-portage/cpuinfo2cpuflags
    return 'CPU_FLAGS_X86="aes mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3"'

def get_python_support():
    return """
PYTHON_TARGETS="python2_7 python3_5 python3_6"
PYTHON_SINGLE_TARGET="python2_7"
USE_PYTHON="2.7"
PYTHON_ABIS="2.7 3.5 3.6"
"""


def configure(configuration):
    configure_print('make.conf')
    path_to_root = configuration['path_to_root']
    print('see ' + str(Path(path_to_root, 'usr/share/portage/config/make.conf.example')) + ' for examples')

    with create_file(Path(path_to_root, 'etc/portage/make.conf')) as f:
        sse = get_sse_support()
        py = get_python_support()
        cmd = sse + '\n\n' + '\n\n' + py + """
ACCEPT_LICENSE="*"
CFLAGS="-O3 -pipe -march=native"
CXXFLAGS="${CFLAGS}"

VIDEO_CARDS="nvidia"
INPUT_DEVICES="keyboard mouse" # virtualbox

CHOST="x86_64-pc-linux-gnu"

USE="threads policykit consolekit utf8 ipv6"

USE="${USE} qt4 -qt5 -gtk -gtk3 wayland egl gles gles2 opengl opencl"
USE="${USE} ffmpeg -libav -vlc "
USE="${USE} udev evdev -systemd "
USE="${USE} -java -ruby "
USE="${USE} -sqlite -mysql postgres "
USE="${USE} -pam -semantic-desktop "
USE="${USE} pulseaudio alsa "

ALSA_CARDS="ca0106 hda-intel"

PORTDIR="/usr/portage"
DISTDIR="${PORTDIR}/distfiles"
PKGDIR="${PORTDIR}/packages"

MAKEOPTS="-j{0}"
EMERGE_DEFAULT_OPTS="--jobs=2 --keep-going=y "
PORTAGE_TMPDIR=/tmp
#PORTDIR_OVERLAY="/usr/local/portage"

source /var/lib/layman/make.conf
""".format(multiprocessing.cpu_count())
        print(cmd, file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)
