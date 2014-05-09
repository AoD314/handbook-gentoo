#!/usr/bin/env python3.4

from pathlib import Path
from general import create_file, configure_print
import subprocess


def find_device_by_name(table, name):
    for r in table:
        if r['name'] == name:
            return r['device']
    raise 'device not found !'


def get_uuid(name):
    text = subprocess.getoutput('ls -l /dev/disk/by-uuid/').split('\n')
    for t in text:
        if name[-4:] in t:
            return t[-50:-14]
    raise 'uuid not found!'

def configure(config):
    configure_print('fstab')

    table = config['table']

    with create_file(Path(config['path_to_root'], 'etc/fstab')) as f:
        print("""# /etc/fstab: static file system information.
#
# See the manpage fstab(5) for more information.
#

""", file=f)

        print('#{:<49s} {:<15s} {:<6s} {:<42s} {}\n'.format('<fs>', '<mountpoint>', '<type>', '<opts>', '<dump/pass>'), file=f)

        device = find_device_by_name(table, '/')
        print('UUID={:<45s} {:<15s} {:<6s} {:<42s} 0     1'.format(get_uuid(device), '/',    'ext4',  'defaults,relatime,discard'), file=f)

        for t in table:
            if t['name'] == '/': continue
            params = 'noatime'
            if t['name'] == '/home': params += ',defaults'
            print('UUID={:<45s} {:<15s} {:<6s} {:<42s} 0     0'.format(get_uuid(t['device']), t['name'], 'ext4', params), file=f)

        print('{:<50s} {:<15s} {:<6s} {:<42s} 0     0'.format('/dev/cdrom', '/mnt/cdrom',    'auto',  'noauto,user,ro,utf8'), file=f)
        print('{:<50s} {:<15s} {:<6s} {:<42s} 0     0'.format('tmpfs','/tmp', 'tmpfs', 'noatime,nodiratime,nodev,nosuid,size=8G'), file=f)


if __name__ == '__main__':
    table = [
        {'name': '/',            'device': '/dev/sda5'},
        {'name': '/home',        'device': '/dev/sda2'},
        {'name': '/torrent',     'device': '/dev/sdc2'},
        {'name': '/work',        'device': '/dev/sdd2'},
        {'name': '/video',       'device': '/dev/sda5'},
        {'name': '/music_video', 'device': '/dev/sdb2'}
    ]
    config = {'path_to_root': '/tmp', 'table': table}
    configure(config)