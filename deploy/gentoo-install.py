#!/usr/bin/env python3.4

from files.config import configure_applications

table = [
    {'name': '/',            'device': '/dev/sde1'},
    {'name': '/home',        'device': '/dev/sdc2'},
    {'name': '/torrent',     'device': '/dev/sdd2'},
    {'name': '/work',        'device': '/dev/sda2'},
    {'name': '/video',       'device': '/dev/sdc5'},
    {'name': '/music_video', 'device': '/dev/sdb2'}
]

config = {
    'path_to_root': '/mnt/gentoo',
    'user_name': 'aod314',
    'device': '/dev/sde',
    'path_to_portage': '/tmp/portage-latest.tar.bz2',
    'path_to_stage3': '/tmp/stage3-amd64-latest.tar.bz2',
    'table': table
}

print('ONLY PRINT:')
print('    download: ' + config['path_to_portage'] + ', ' + config['path_to_stage3'] + ' from http://mirror.yandex.ru/')

print('    format disk: \n        # mkfs.ext4 /dev/sdaX')
print('    for SSD disable journal \n        # tune2fs -o journal_data_writeback /dev/sdaX')
print('\n\n')

print('configure applications')
configure_applications(config)
