#! /usr/bin/python3 
# -*- coding: utf-8 -*-

import multiprocessing
import os

def get_cpu_count():
    return multiprocessing.cpu_count()

def get_sse_support():
    return " sse sse2 sse3 ssse3 " #+ " sse4 sse4.1 sse4_1 sse4.2 sse4_2 avx "

def get_etc_make_conf():
    comments = 'PORTDIR_OVERLAY="/usr/local/portage"\n\n'
    text = 'LINGUAS="ru"\nACCEPT_LICENSE="*"\n\n'
    devices = 'INPUT_DEVICES="evdev keyboard mouse virtualbox"\nVIDEO_CARDS="nvidia"\n\n'
    makeopts = 'MAKEOPTS="-j' + str(get_cpu_count()) + '"\n\n'
    jobs = 'EMERGE_DEFAULT_OPTS="--jobs=' + str(int(get_cpu_count() / 3)) + '"\n\n'
    sse = get_sse_support()
    use = 'USE="nls qt4 python theora gmp posix usb png ogg udev threads xvid webm x264 ogg flac opengl policykit consolekit X xorg vdpau unicode utf8 doc iconv icu m17n-lib python2_7 python3_3 ' + sse + '"\n\n'
    flags = 'CFLAGS="-march=native -mtune=corei7 -Ofast -flto -pipe -msse4.1 -msse4.2 -mpopcnt -fomit-frame-pointer"\n\n'

    all_text = text + makeopts + jobs + comments + use + flags

    with open('make.conf', 'w') as f:
        print(all_text, file=f)
    
