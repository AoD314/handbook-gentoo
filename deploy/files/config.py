#!/usr/bin/env python3.4
import os

from pathlib import Path

from files import bash, vim, git, mpv, profile, fstab, locale, make, net, sysctl, X, sublime
from files import general
import subprocess
import shutil

applications_start = [
    'app-admin/syslog-ng',
    'sys-process/cronie',
    'virtual/ssh',
    'net-misc/dhcpcd',
    'sys-boot/grub',
    'sys-kernel/gentoo-sources',
    'sys-kernel/genkernel',
    'app-editors/vim',
    'app-portage/eix',
    'app-portage/cpuinfo2cpuflags',
    'x11-apps/setxkbmap',
    'app-portage/genlop',
    'app-portage/gentoolkit',
    'app-portage/mirrorselect',
    'app-portage/portage-utils',
    'app-shells/bash-completion',
    'net-analyzer/iftop',
    'sys-process/iotop',
    'sys-process/htop',
    'app-text/tree',
    'virtual/awk',
    'virtual/eject',
    'net-analyzer/nmap',
    'net-analyzer/traceroute',
    'net-analyzer/tcptraceroute',
    'net-firewall/iptables',
    'net-misc/dhcpcd',
    'net-misc/wget',
    'sys-apps/lm_sensors',
    'net-misc/ntp'
]

applications_base = [
    'dev-util/cmake',
    'dev-util/ninja',
    'dev-vcs/git',
    'dev-qt/qt-creator',
    'x11-misc/qxkb',
    'sys-devel/clang',
    'sys-devel/llvm',
    'sys-devel/gdb',
    'app-arch/p7zip',
    'app-arch/unrar',
    'app-misc/mc',
    'app-misc/tmux',
    'dev-util/ccache',
    'media-fonts/droid',
    'media-libs/flac',
    'media-libs/freeglut',
    'media-libs/glew',
    'media-libs/glu',
    'media-libs/libogg',
    'media-libs/libpng',
    'media-libs/libsdl2',
    'media-libs/libtheora',
    'media-libs/libvpx',
    'media-libs/libwebp',
    'media-libs/opus',
    'media-libs/sdl2-gfx',
    'media-libs/sdl2-ttf',
    'media-libs/tiff',
    'media-libs/x264',
    'media-libs/x265',
    'media-libs/xvid',
    'media-video/ffmpeg',
    'media-video/mediainfo',
    'media-video/mpv',
    'media-video/nvidia-settings',
    'net-print/cups',
    'virtual/ffmpeg',
    'virtual/jre',
    'virtual/jpeg',
    'virtual/glu',
    'virtual/latex-base',
    'virtual/opencl',
    'virtual/opengl',
    'www-client/links'
]

applications_X = [
    'media-libs/mesa',
    'dev-libs/wayland',
    'x11-base/xorg-drivers',
    'x11-base/xorg-server',
    'x11-base/xorg-x11',
    'x11-drivers/nvidia-drivers',
    'x11-drivers/xf86-input-mouse',
    'x11-drivers/xf86-input-evdev',
    'x11-drivers/xf86-input-keyboard'
]

applications_big = [
    'dev-cpp/tbb',
    'app-doc/doxygen',
    'dev-java/oracle-jre-bin',
    'dev-libs/gmp',
    'dev-python/matplotlib',
    'dev-python/numpy',
    'dev-python/pyopencl',
    'dev-texlive/texlive-xetex',
    'dev-util/nvidia-cuda-toolkit',
    'dev-util/valgrind',
    'media-gfx/blender',
    'media-gfx/gimp',
    'media-gfx/inkscape',
    'media-video/qt-recordmydesktop',
    'media-video/recordmydesktop',
    'net-fs/samba',
    'net-im/skype',
    'www-client/firefox',
    'www-client/chromium',
    'www-plugins/adobe-flash',
    'x11-apps/mesa-progs'
]

applications_games = [
    'games-arcade/sdlroids',
    'games-fps/xonotic',
    'games-action/violetland'
]

applications_kde = [
    'kde-base/kdebase-runtime-meta',
    'kde-base/kdebase-startkde'
]


def configure_applications(config):
    print('clear ' + config['path_to_root'] + ' ...')
    subprocess.getstatusoutput('rm -rf ' + config['path_to_root'])
    print('unpacking stage3 ...')
    subprocess.getstatusoutput('tar xvjpf ' + config['path_to_stage3'] + ' -C ' + config['path_to_root'])
    print('unpacking portage ...')
    subprocess.getstatusoutput('tar xvjf  ' + config['path_to_portage'] + ' -C ' + str(Path(config['path_to_root'], 'usr')))

    profile.configure(config)
    fstab.configure(config)
    locale.configure(config)
    make.configure(config)
    net.configure(config)
    sysctl.configure(config)
    X.configure(config)
    bash.configure(config)
    sublime.configure(config)
    vim.configure(config)
    git.configure(config)
    mpv.configure(config)

    r = Path(config['path_to_root'], 'gentoo-install')
    if not r.exists():
        r.mkdir()
    shutil.copyfile('./config/system/.config', str(Path(r, '.config')))
    shutil.copytree('../package/package.keywords/', str(Path(config['path_to_root'], 'etc/portage/package.keywords/')))
    shutil.copytree('../package/package.unmask/', str(Path(config['path_to_root'], 'etc/portage/package.unmask/')))
    shutil.copytree('../package/package.use/', str(Path(config['path_to_root'], 'etc/portage/package.use/')))

    with general.create_file(Path(config['path_to_root'], 'var/lib/layman/make.conf')) as f:
        print('PORTDIR_OVERLAY="$PORTDIR_OVERLAY"', file=f)

    # generate shell install script
    with general.create_file(Path(config['path_to_root'], 'gentoo-chroot.sh')) as f:
        print('echo mounting ...', file=f)
        print('mount -t proc proc {}'.format(str(Path(config['path_to_root'], 'proc'))), file=f)
        print('mount --rbind /sys {}'.format(str(Path(config['path_to_root'], 'sys'))), file=f)
        print('mount --rbind /dev {}'.format(str(Path(config['path_to_root'], 'dev'))), file=f)
        print('echo chrooting ...', file=f)
        print('chroot {} /bin/bash'.format(config['path_to_root']), file=f)
        print('\n', file=f)

    with general.create_file(Path(config['path_to_root'], 'gentoo-install.sh')) as f:
        print('source /etc/profile', file=f)
        print('export PS1="(chroot) $PS1"', file=f)
        print('mkdir /usr/local/portage', file=f)
        print('\n', file=f)

        print('echo "SYNC ..."', file=f)
        print('emerge-webrsync', file=f)
        print('emerge --sync --quiet', file=f)
        print('\n', file=f)

        print('echo "Install gcc ..."', file=f)
        print('echo "emerge =sys-devel/gcc-4.8.2"', file=f)
        print('emerge =sys-devel/gcc-4.8.2', file=f)
        print('gcc-config -l', file=f)
        print('echo "Enter number of compiler:"', file=f)
        print('read cm', file=f)
        print('gcc-config ${cm}', file=f)
        print('echo "Rebuild qtcore(emerge dev-qt/qtcore)"', file=f)
        print('emerge dev-qt/qtcore', file=f)

        print('echo "Setting profile ..."', file=f)
        print('eselect profile list', file=f)
        print('echo "Enter number of profile:"', file=f)
        print('read pr', file=f)
        print('eselect profile set ${pr}', file=f)
        print('', file=f)

        print('echo "Install TimeZone ..."', file=f)
        print('echo "Europe/Moscow" > /etc/timezone', file=f)
        print('emerge --config sys-libs/timezone-data', file=f)
        print('', file=f)

        print('echo "Install locale ..."', file=f)
        print('locale-gen\n', file=f)
        print('eselect locale list', file=f)
        print('echo "Enter number of locale:"', file=f)
        print('read lc', file=f)
        print('eselect locale set ${lc}', file=f)
        print('env-update && source /etc/profile', file=f)

        print('echo "Install applications ..."', file=f)
        cmd = 'emerge -vuDN1 ' + ' '.join(applications_start)
        print('echo "{}"'.format(cmd), file=f)
        print(cmd, file=f)
        print('\n', file=f)

        print('echo "Update autorun ..."', file=f)
        print('rc-update add syslog-ng default', file=f)
        print('rc-update add cronie default', file=f)
        print('crontab /etc/crontab', file=f)
        print('rc-update add sshd default\n', file=f)
        print('rc-update add ntpd default\n', file=f)

        print('echo "Update /etc/mtab..."', file=f)
        print('grep -v rootfs /proc/mounts > /etc/mtab\n', file=f)

        print('echo "Network configure ... "\n', file=f)
        print('cd /etc/init.d', file=f)
        print('ln -s net.lo net.eth0', file=f)
        print('rc-update add net.eth0 default', file=f)
        print('\n', file=f)

        print('echo "Keyboard configure ... "\n', file=f)
        print('setxkbmap -layout "us,ru(winkeys)" -option grp:caps_toggle,grp_led:caps', file=f)

        print('echo "Kernel configure ... "\n', file=f)
        print('cp /gentoo-install/.config /usr/src/linux', file=f)
        print('genkernel --oldconfig --no-clean --no-mrproper', file=f)

        print('echo "Grug2 configure ... "\n', file=f)
        print('grub2-install ' + str(fstab.find_device_by_name(config['table'], '/')), file=f)
        print('grub2-mkconfig -o /boot/grub/grub.cfg', file=f)

        print('echo "Creating groups ..."', file=f)
        print('groupadd games', file=f)
        print('groupadd android', file=f)
        print('groupadd vboxusers', file=f)
        print('groupadd kvm', file=f)

        print('echo "Add user ..."', file=f)
        print('useradd -m -G wheel,audio,cdrom,video,usb,users,portage,games,android,vboxusers,kvm -s /bin/bash ' +
              config['user_name'] + '\n', file=f)
        print('echo "Enter new password for ' + config['user_name'] + '"', file=f)
        print('passwd ' + config['user_name'], file=f)
        print('echo "Enter new root password"', file=f)
        print('passwd', file=f)
        print('\n', file=f)

        print('echo "done!"', file=f)

    with general.create_file(Path(config['path_to_root'], 'gentoo-exit.sh')) as f:
        print("""
echo "exit && cd / && umount -l /mnt/gentoo/dev{/shm,/pts,} && umount -l /mnt/gentoo/proc"
""", file=f)

    with general.create_file(Path(config['path_to_root'], 'gentoo-install-my-tools.sh')) as f:
        cmd = 'emerge -f ' + ' '.join(applications_base) + ' '.join(applications_X) + ' '.join(applications_big) + ' '.join(applications_games) + ' '.join(applications_kde)
        print('echo "' + cmd + '"', file=f)
        print(cmd, file=f)
        cmd = 'emerge -1 ' + ' '.join(applications_base) + ' '.join(applications_X) + ' '.join(applications_big) + ' '.join(applications_games) + ' '.join(applications_kde)
        print('echo "' + cmd + '"', file=f)
        print(cmd, file=f)


    os.chmod(str(Path(config['path_to_root'], 'gentoo-install-my-tools.sh')), mode=755)
    os.chmod(str(Path(config['path_to_root'], 'gentoo-install.sh')), mode=755)
    os.chmod(str(Path(config['path_to_root'], 'gentoo-chroot.sh')), mode=755)
    os.chmod(str(Path(config['path_to_root'], 'gentoo-exit.sh')), mode=755)
