#!/usr/bin/env python3.4
import multiprocessing

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('mpv')
    path_to_mpv_dir = Path(config['path_to_root'], 'home', config['user_name'], '.config', 'mpv')

    with create_file(Path(path_to_mpv_dir, 'mpv.conf')) as f:
        print("""##############################################################
# https://github.com/mpv-player/mpv/blob/master/DOCS/man/en/ #
##############################################################
ad-lavc-threads=6
vd-lavc-threads=12

cache=524288          # 512 mb
cache-default=524288  # 512 mb

reset-on-next-file=""
volume=32
sub-ass=no
osd-duration=3000
osd-font="Liberation Mono"
osd-font-size=12
osd-level=3 # volume + seek + timer + percentage + total time
osd-color=1.0/1.0/1.0
osd-back-color=0.0/0.0/0.0/0.25
osd-border-size=0
sub-blur=0
hwdec=auto

slang="ru"
alang="ru"

screenshot-jpeg-quality=100
screenshot-png-compression=9
screenshot-format=png
screenshot-png-filter=5
profile=opengl-hq
""", file=f)

    with create_file(Path(path_to_mpv_dir, 'input.conf')) as f:
        print("""
F1 show_text "${filename}(${video-format}, ${audio-codec-name})   [${width}x${height}@${container-fps} ${file-size}]"
F2 show_text "${estimated-frame-number} / ${estimated-frame-count}"
F3 show_text "bitrate: \n${video-bitrate}\n${audio-bitrate}"
F4 show_text "cache total/used/free: ${cache-size} / ${cache-used} / ${cache-free} - ${cache-buffering-state}%"
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)
