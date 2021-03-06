#!/usr/bin/env python3.4

from general import create_file, run_command
from cpu import CPU


def configure():

    run_command('emerge -1v app-portage/cpuinfo2cpuflags')

    with create_file('/etc/portage/make.conf') as f:
        cpu = CPU()
        cmd = """
# see /usr/share/portage/config/make.conf.example

CPU_FLAGS_X86="{}"

PYTHON_TARGETS="python2_7 python3_5"
PYTHON_SINGLE_TARGET="python2_7"
USE_PYTHON="2.7"

ACCEPT_LICENSE="*"
CFLAGS="-O3 -pipe -march=native"
CXXFLAGS="${{CFLAGS}}"

#VIDEO_CARDS="nvidia"
INPUT_DEVICES="keyboard mouse" # virtualbox

CHOST="x86_64-pc-linux-gnu"

USE="threads policykit consolekit utf8 ipv6"

USE="${{USE}} qt4 -qt5 -gtk -gtk3 wayland egl gles gles2 opengl opencl"
USE="${{USE}} ffmpeg -libav -vlc "
USE="${{USE}} udev evdev -systemd "
USE="${{USE}} -java -ruby "
USE="${{USE}} -sqlite -mysql postgres "
USE="${{USE}} -pam -semantic-desktop "
USE="${{USE}} pulseaudio alsa "

ALSA_CARDS="ca0106 hda-intel"

PORTAGE_TMPDIR=/tmp

PORTDIR="/usr/portage"
DISTDIR="${{PORTDIR}}/distfiles"
PKGDIR="${{PORTDIR}}/packages"
#PORTDIR_OVERLAY="/usr/local/portage"

MAKEOPTS="-j{}"
EMERGE_DEFAULT_OPTS="--jobs=4 --keep-going=y "

#source /var/lib/layman/make.conf
""".format(cpu.get_flags(), cpu.get_num_cores() + 1)
        print(cmd, file=f)
