#!/usr/bin/env python3.4

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('X')
    path_to_home = Path(config['path_to_root'], 'home', config['user_name'])

    with create_file(Path(path_to_home, '.xinitrc')) as f:
        print("exec startkde", file=f)

    with create_file(Path(config['path_to_root'], 'etc/conf.d/xdm')) as f:
        print("""# We always try and start X on a static VT. The various DMs normally default
# to using VT7. If you wish to use the xdm init script, then you should ensure
# that the VT checked is the same VT your DM wants to use. We do this check to
# ensure that you haven't accidentally configured something to run on the VT
# in your /etc/inittab file so that you don't get a dead keyboard.
CHECKVT=7

# What display manager do you use ?  [ xdm | gdm | kdm | gpe | entrance ]
# NOTE: If this is set in /etc/rc.conf, that setting will override this one.
DISPLAYMANAGER="kdm"
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)