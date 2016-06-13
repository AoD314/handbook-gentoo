#!/usr/bin/env python3

from ask import get_answer
from download import download_stage3
from general import Dir, run_command, print_log

import os
import re
import subprocess
import shutil
import sys

import fstab
import kde
import locale
import make
import network
import profile
import repos
import sysctl
import timezone


def unpack_stage3(path_to_install):
    path_to_stage3 = '/tmp/stage3-amd64-latest.tar.bz2'
    cmd = 'tar xvjpf ' + path_to_stage3

    print_log('chdir ' + path_to_install)
    os.chdir(path_to_install)

    print_log('cleaning ... ')
    print_log('[rm -rf *]')
    os.system('rm -rf *')
    print_log('done')

    print_log('installing ... ')

    status, msg = subprocess.getstatusoutput(cmd)
    print_log(msg)
    print_log('status ' + str(status))

    path = Dir(path_to_install)
    print_log('cp /etc/resolv.conf ' + path.full('etc/resolv.conf'))
    shutil.copy2('/etc/resolv.conf', path.full('etc/resolv.conf'))


def update_portage():
    run_command('emerge-webrsync')
    run_command('emerge --sync --quiet')
    run_command('emerge eix')
    run_command('eix-sync -q -H')


def configure():
    config = {}

    # user_name, email, login, password, root_password = get_answer(['user name', 'email', 'login', 'password', 'root password'])
    # config['login'] = login
    # config['password'] = password
    # config['root_password'] = root_password
    # config['username'] = user_name
    # config['email'] = email
    config['path_to_install'] = '/mnt/gentoo' #get_answer(['path to gentoo install'])[0]

    return config


def apply_config_files():
    make.configure()
    repos.configure()
    sysctl.configure()
    profile.configure()
    timezone.configure()
    network.configure()
    locale.configure()
    fstab.configure()

    # install X11
    kde.configure()

    # install last
    #run_command('emerge -1v sys-kernel/gentoo-sources sys-boot/grub')
    #run_command('emerge -1v app-admin/syslog-ng sys-process/cronie app-editors/vim app-portage/genlop sys-process/htop')


def chroot(path_to_install):
    path = Dir(path_to_install)
    os.system('mount -t proc proc  {}\n'.format(path.full('/proc')))
    os.system('mount --rbind /sys  {}\n'.format(path.full('/sys')))
    os.system('mount --rbind /dev  {}\n'.format(path.full('/dev')))
    os.chroot(path_to_install)
    os.system('source /etc/profile')
    os.system('export PS1="(chroot) $PS1"')


def change_password(root_password):
    print("changing password ... ")
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

    change_password('123')


if __name__ == "__main__":
    main()
