#!/usr/bin/env python3.4

from pathlib import Path

import bash, vim, git, mpv, profile, fstab, locale, make, net, sysctl, X

from general import create_file

applications_start = [
    'app-admin/syslog-ng',
    'sys-process/cronie',
    'virtual/ssh',
    'net-misc/dhcpcd',
    'sys-boot/grub',
    '=sys-kernel/gentoo-sources-3.14.3',
    'app-editors/vim',
    'app-portage/eix',
    'app-portage/genlop',
    'app-portage/gentoolkit',
    'app-portage/layman',
    'app-portage/mirrorselect',
    'app-portage/portage-utils',
    'app-shells/bash-completion',
    'app-text/tree',
    'net-analyzer/iftop',
    'sys-process/iotop',
    'sys-process/htop',
    'virtual/awk',
    'virtual/eject',
    'net-analyzer/nmap',
    'net-analyzer/traceroute',
    'net-analyzer/tcptraceroute',
    'net-firewall/iptables',
    'net-misc/dhcpcd',
    'net-misc/wget',
    'sys-apps/lm_sensors'
]

applications_base = [
    'dev-util/cmake',
    'dev-util/ninja',
    'dev-vcs/git',
    'dev-qt/qt-creator',
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
    profile.configure(config)
    fstab.configure(config)
    locale.configure(config)
    make.configure(config)
    net.configure(config)
    sysctl.configure(config)
    X.configure(config)
    bash.configure(config)
    vim.configure(config)
    git.configure(config)
    mpv.configure(config)

    # copy package.{use,keywords,...}

    # generate shell install script
    with create_file(Path(config['path_to_root'], 'gentoo-install.sh')) as f:
        print('echo mounting ...', file=f)
        print('mount -t proc proc {}'.format(str(Path(config['path_to_root'], 'proc'))), file=f)
        print('mount --rbind /sys {}'.format(str(Path(config['path_to_root'], 'sys'))), file=f)
        print('mount --rbind /dev {}'.format(str(Path(config['path_to_root'], 'dev'))), file=f)
        print('\n', file=f)
        print('echo chrooting ...', file=f)
        print('chroot {} /bin/bash'.format(config['path_to_root']), file=f)
        print('source /etc/profile', file=f)
        print('export PS1="(chroot) $PS1"', file=f)
        print('\n', file=f)
        print('emerge-webrsync', file=f)
        print('emerge --sync --quiet', file=f)
        print('\n', file=f)
        print('', file=f)
        print('', file=f)
        print('', file=f)
        print('', file=f)

        # eselect profile list

        # ls /usr/share/zoneinfo
        # echo "Europe/Brussels" > /etc/timezone
        #emerge --config sys-libs/timezone-data

        print('locale-gen\n', file=f)
        print('eselect locale set 0\n', file=f)
        print('env-update && source /etc/profile', file=f)

        print('emerge ' + ' '.join(applications_start), file=f)
        print('\n', file=f)
        print('rc-update add syslog-ng default', file=f)
        print('rc-update add cronie default', file=f)
        print('crontab /etc/crontab', file=f)
        print('rc-update add sshd default\n', file=f)
        print('grep -v rootfs /proc/mounts > /etc/mtab\n', file=f)

        print('useradd -m -G wheel,audio,cdrom,video,usb,users,portage,games,android,vboxusers,kvm -s /bin/bash ' + config['user_name'] + '\n')

        print('echo "Enter new root passwd"', file=f)
        print('passwd', file=f)

        # kernel install
        # grub

    with create_file(Path(config['path_to_root'], 'gentoo-exit.sh')) as f:
        print("""
echo "exit && cd / && umount -l /mnt/gentoo/dev{/shm,/pts,} && umount -l /mnt/gentoo{/boot,/proc,}"
""", file=f)

    with create_file(Path(config['path_to_root'], 'gentoo-install-my-tools.sh')) as f:
        print('emerge ' + ' '.join(applications_base) + ' '.join(applications_X) + ' '.join(applications_big) +
            ' '.join(applications_games) + ' '.join(applications_kde), file=f)
