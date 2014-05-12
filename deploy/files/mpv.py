#!/usr/bin/env python3.4
import multiprocessing

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('mpv')
    path_to_mpv_dir = Path(config['path_to_root'], 'home', config['user_name'], '.config', 'mpv')

    with create_file(Path(path_to_mpv_dir, 'config')) as f:
        print("""##############################################################
# https://github.com/mpv-player/mpv/blob/master/DOCS/man/en/ #
##############################################################
ad-lavc-threads=2
vd-lavc-threads=8

cache=262144          # 256 mb
cache-default=262144  # 256 mb

reset-on-next-file=""

volume=50

sub-ass=no
osd-duration=3000
osd-font="Liberation Mono"
osd-font-size=12
osd-level=3 # volume + seek + timer + percentage + total time

osd-color=1.0/1.0/1.0
osd-back-color=0.0/0.0/0.0/0.25

osd-border-size=0
sub-text-blur=0

hwdec=auto

slang="ru"
alang="ru"

vo=opengl-hq

screenshot-jpeg-quality=100
screenshot-png-compression=9
""", file=f)

    with create_file(Path(path_to_mpv_dir, 'input.conf')) as f:
        print("""
F1 show_text "${filename}(${video-format})   [${width}x${height}@${fps} ${file-size}]"
F3 show_text "${estimated-frame-number} / ${estimated-frame-count}"
F3 show_text "video bitrate: ${video-bitrate}"
F4 show_text "cache total/used/free: ${cache-size} / ${cache-used} / ${cache-free} - ${cache}%"
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)