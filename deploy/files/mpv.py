#!/usr/bin/env python3.4
import multiprocessing

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('mpv')
    path_to_mpv_dir = Path(config['path_to_root'], 'home', config['user_name'], '.mpv')

    with create_file(Path(path_to_mpv_dir, 'config')) as f:
        print("""##############################################################
# https://github.com/mpv-player/mpv/blob/master/DOCS/man/en/ #
##############################################################
ad-lavc-threads=""" + str(multiprocessing.cpu_count()) + """
cache=auto
cache-default=""" + str(256 * 1024) + """ #kb
cache-min=5
fs=yes
ass=no
osd-duration=5000
osd-font="Liberation Mono"
osd-font-size=16
osd-level=3
sub-text-blur=2
hwdec=auto
slang="ru"
alang="ru"
vo=opengl-hq
volstep=2
screenshot-jpeg-quality=100
screenshot-png-compression=9""", file=f)

    with create_file(Path(path_to_mpv_dir, 'input.conf')) as f:
        print('F1 show_text "${filename}(${video-format})   [${width}x${height}@${fps} ${file-size}]"', file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)