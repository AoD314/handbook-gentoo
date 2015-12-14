#!/usr/bin/env python3

from download import download_stage3
from ask import get_answer
from general import create_file, Dir

import os
import re
import subprocess
import shutil
import sys

import make, timezone, locale, network, profile, kde, repos, sysctl

def unpack_stage3(path_to_install):
    path_to_stage3 = '/tmp/stage3-amd64-latest.tar.bz2'
    cmd = 'tar xvjpf /tmp/stage3-amd64-latest.tar.bz2'

    os.chdir(path_to_install)
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
    subprocess.getstatusoutput('emerge-webrsync')
    subprocess.getstatusoutput('emerge --sync --quiet')

def configure():
    config = {}

    user_name, email, login, password, root_password = get_answer(['user name', 'email', 'login', 'password', 'root password'])

    config['login'] = login
    config['password'] = password
    config['root_password'] = root_password
    config['username'] = user_name
    config['email'] = email
    config['path_to_install'] = get_answer(['path to gentoo install'])[0]

    return config

def apply_config_files():
    make.configure()
    repos.configure()
    sysctl.configure()
    profile.configure()
    timezone.configure()
    network.configure()
    locale.configure()

    # install kde
    kde.configure()


def chroot(path_to_install):
    path = Dir(path_to_install)

    os.system('mount -t proc proc  {}\n'.format(path.full('/proc')))
    os.system('mount --rbind /sys  {}\n'.format(path.full('/sys')))
    os.system('mount --make-rslave {}\n'.format(path.full('/sys')))
    os.system('mount --rbind /dev  {}\n'.format(path.full('/dev')))
    os.system('mount --make-rslave {}'.format(path.full('/dev')))

    os.chroot(path_to_install)

    os.system('source /etc/profile')
    os.system('export PS1="(chroot) $PS1"')


def change_password(root_password):
    passwd = subprocess.Popen(['passwd'], stdin=subprocess.PIPE,
                          stdout=open('/dev/null', 'w').fileno(),
                          stderr=subprocess.STDOUT)
    passwd.communicate(root_password.encode('utf-8'))
    print("result: " + passwd.returncode)

def main():
    config = configure()
    download_stage3()
    unpack_stage3(config['path_to_install'])
    chroot(config['path_to_install'])

    update_portage()
    apply_config_files()

    change_password(config['root_password'])

    os.system('umount -l /mnt/gentoo/dev{/shm,/pts,} && umount /mnt/gentoo{/boot,/sys,/proc,}')

    print('install finished !!!')

if __name__ == "__main__":
    main()
