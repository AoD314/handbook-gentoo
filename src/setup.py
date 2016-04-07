#!/usr/bin/env python3

from download import download_stage3
from ask import get_answer
from general import Dir
from general import run_command

import os
import re
import subprocess
import shutil
import sys

import make
import timezone
import locale
import network
import profile
import repos
import sysctl


def unpack_stage3(path_to_install):
    path_to_stage3 = '/tmp/stage3-amd64-latest.tar.bz2'
    cmd = 'tar xvjpf ' + path_to_stage3

    os.chdir(path_to_install)

    print('cleaning ... ', end='')
    sys.stdout.flush()
    os.system('rm -rf *')
    print('done')

    print('installing ... ', end='')
    sys.stdout.flush()

    status, msg = subprocess.getstatusoutput(cmd)
    msg = msg.split('\n')
    filtered_msg = [l for l in msg if re.match('^tar', l)]
    if status != 0:
        print('\nerror: ', status)
        print('message:\n', '\n'.join(filtered_msg))
    else:
        print('done')

    path = Dir(path_to_install)
    shutil.copy2('/etc/resolv.conf', path.full('etc/resolv.conf'))


def update_portage():
    run_command('emerge-webrsync')
    run_command('emerge --sync --quiet')
    run_command('emerge eix')
    run_command('eix-sync -q -H')


def configure():
    config = {}

    user_name, email, login, password, root_password = get_answer(['user name', 'email', 'login', 'password', 'root password'])
    config['login'] = login
    config['password'] = password
    config['root_password'] = root_password
    config['username'] = user_name
    config['email'] = email
    config['path_to_install'] = get_answer(['path to gentoo install'])[0]

    # config['login'] = 'user'
    # config['password'] = '123'
    # config['root_password'] = '123'
    # config['username'] = 'User User'
    # config['email'] = 'user@e-mail.com'
    # config['path_to_install'] = '/mnt/gentoo'

    return config


def apply_config_files():
    make.configure()
    repos.configure()
    sysctl.configure()
    profile.configure()
    timezone.configure()
    network.configure()
    locale.configure()

    # install X11
    kde.configure()

    # install last
    run_command('emerge -1v sys-kernel/gentoo-sources sys-boot/grub')
    run_command('emerge -1v app-admin/syslog-ng sys-process/cronie app-editors/vim app-portage/genlop sys-process/htop')


def chroot(path_to_install):
    path = Dir(path_to_install)
    os.system('mount -t proc proc  {}\n'.format(path.full('/proc')))
    os.system('mount --rbind /sys  {}\n'.format(path.full('/sys')))
    os.system('mount --rbind /dev  {}\n'.format(path.full('/dev')))
    os.chroot(path_to_install)
    os.system('source /etc/profile')
    os.system('export PS1="(chroot) $PS1"')


def change_password(root_password):
    print('*' * 120)
    print("Please change root password !!!!!")
    print('*' * 120)
    passwd = subprocess.Popen(['passwd'], stdin=subprocess.PIPE, stdout=open('/dev/null', 'w').fileno(), stderr=subprocess.STDOUT)
    passwd.communicate(str(root_password).encode('utf-8'))
    print("result: " + str(passwd.returncode))


def main():
    config = configure()
    download_stage3()
    unpack_stage3(config['path_to_install'])
    chroot(config['path_to_install'])

    update_portage()
    apply_config_files()

    change_password(config['root_password'])


if __name__ == "__main__":
    main()
