from general import create_file, run_command


def configure():

    with create_file('/etc/locale.gen') as f:
        print('ru_RU.UTF-8 UTF-8\nen_US.UTF-8 UTF-8', file=f)

    with create_file('/etc/environment') as f:
        print('LANG="en_US.UTF-8"', file=f)

    with create_file('/etc/conf.d/consolefont') as f:
        print('consolefont="LatArCyrHeb-14"', file=f)

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

    run_command('emerge -1v net-misc/ntp')

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

    run_command('rc-update add ntpd default')

    with create_file('/etc/profile.d/xdg_cache_home.sh') as f:
        print("""
export XDG_CACHE-HOME="/tmp/${USER}/.cache"
""", file=f)

    with create_file('/etc/env.d/02locale') as f:
        print("""
LANG="en_US.UTF-8"
LC_COLLATE="C"
""", file=f)

    run_command('locale-gen')
    run_command('env-update')
    run_command('source /etc/profile')
    run_command('emerge -1v x11-apps/setxkbmap')
    run_command('setxkbmap -layout "us,ru(winkeys)" -option grp:caps_toggle,grp_led:caps')
