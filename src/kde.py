from general import create_file, run_command


def configure():
    run_command('emerge -1v x11-apps/xdm')
    run_command('rc-update add xdm default')

    with create_file('/etc/conf.d/xdm') as f:
        print('DISPLAYMANAGER="kdm"', file=f)

    run_command('emerge -1v kde-apps/kdebase-meta')
