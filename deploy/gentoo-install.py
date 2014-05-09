#!/usr/bin/env python3.4

from pathlib import Path


config = {
    'path_to_root': '/tmp/gentoo',
    'user_name': 'aod314',
    'password': '123',
    'arch': 'x64',
    'device': '/dev/sda',
    'path_to_portage': '/tmp/portage-latest.tar.bz2',
    'path_to_stage3': '/tmp/stage3-amd64-latest.tar.bz2'
}

table = [
    {'name': '/',            'device': '/dev/sde1'},
    {'name': '/home',        'device': '/dev/sda2'},
    {'name': '/torrent',     'device': '/dev/sdc2'},
    {'name': '/work',        'device': '/dev/sdd2'},
    {'name': '/video',       'device': '/dev/sda5'},
    {'name': '/music_video', 'device': '/dev/sdb2'}
]

commands = []

print('ONLY PRINT:')
print('    download: ' + config['path_to_portage'] + ', ' + config['path_to_stage3'] + ' from http://mirror.yandex.ru/')

print('    format disk: \n        # mkfs.ext4 /dev/sdaX')
print('    for SSD disable journal \n        # tune2fs -o journal_data_writeback /dev/sdaX')
print('\n\n')

commands.append('mount ' + find_device_by_name(table, '/') + ' ' + config['path_to_root'])
commands.append('tar xvjpf ' + config['path_to_stage3'] + ' -C ' + config['path_to_root'])
commands.append('tar xvjf  ' + config['path_to_portage'] + ' -C ' + str(Path(config['path_to_root'], 'usr')))

print('configure applications')
print('\n\n')

for c in commands:
    print('\t' + c)