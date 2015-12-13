from general import create_file

import subprocess

def configure(path_to_root):

    with create_file('/etc/locale.gen') as f:
        print('ru_RU.UTF-8 UTF-8\nen_US.UTF-8 UTF-8', file=f)

    with create_file('/etc/environment') as f:
        print('LANG="en_US.UTF-8"', file=f)

    with create_file('/etc/conf.d/consolefont') as f:
        print('consolefont="LatArCyrHeb-16"', file=f)

    with create_file('/etc/conf.d/keymaps') as f:
        print("""
keymap="us"
windowkeys="yes"
extended_keymaps=""
dumpkeys_charset=""
fix_euro="no"
""", file=f)

    with create_file('/etc/conf.d/hwclock') as f:
        print('clock="local"', file=f)

    with create_file('/etc/conf.d/keymaps') as f:
        print('clock="local"', file=f)

    with create_file('/etc/ntp.conf') as f:
        print("""
# Common pool for random people
#server pool.ntp.org

server ntp1.stratum2.ru
server ntp2.stratum2.ru
server ntp3.stratum2.ru

server ntp1.stratum1.ru
server ntp2.stratum1.ru
server ntp3.stratum1.ru

# Pools for Gentoo users
server 0.gentoo.pool.ntp.org
server 1.gentoo.pool.ntp.org
server 2.gentoo.pool.ntp.org
server 3.gentoo.pool.ntp.org

driftfile       /var/lib/ntp/ntp.drift

restrict default nomodify nopeer noquery limited kod
restrict 127.0.0.1
restrict [::1]
""", file=f)

    with create_file('/etc/env.d/02locale') as f:
        print("""
LANG="en_US.UTF-8"
LC_COLLATE="C"
""", file=f)

    subprocess.getstatusoutput('locale-gen')
    subprocess.getstatusoutput('env-update && source /etc/profile')

    print('Keyboard configure ... ', end='')
    subprocess.getstatusoutput('setxkbmap -layout "us,ru(winkeys)" -option grp:caps_toggle,grp_led:caps')
    print(' ')


