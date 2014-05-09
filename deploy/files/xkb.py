#!/usr/bin/env python3.4




## /etc/X11/xorg.conf
# """
#  Section "InputDevice"
#       Identifier  "Keyboard0"
#       Driver      "kbd"
#       Option      "XkbModel" "pc105"
#       Option      "XkbLayout" "us,ru"
#       Option      "XkbVariant" ",winkeys"
#       Option      "XkbOptions" "grp:caps_toggle,grp_led:caps"
#  EndSection
#
#
##################################################################
#
#
# /etc/X11/xorg.conf.d/10-keyboard.conf
# Section "InputClass"
#         Identifier "system-keyboard"
#         MatchIsKeyboard "on"
#         Option "XkbLayout" "cz,us"
#         Option "XkbModel" "pc104"
#         Option "XkbVariant" ",dvorak"
#         Option "XkbOptions" "grp:alt_shift_toggle"
# EndSection
#
# """

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('sublime')

    with create_file(Path(config['path_to_root'], 'home', config['user_name'] ,'.config/qxkb.cfgs')) as f:
        print("""
[Style]
path=/usr/share/qxkb/theme/default

[KeyLayout]
model=pc104
layout="us,ru"
variant=" ,"
status=2
showflag=true
showsingle=false
switching=0
useConvert=false
shotcutConvert=
option=grp:caps_toggle
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)