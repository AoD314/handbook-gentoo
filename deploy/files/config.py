#config_file_list = ['make.conf']
import bash, vim, git, mpv, profile

applications = []

applications_start = [
    'app-editors/vim',
    'app-portage/eix',
    'app-portage/genlop',
    'app-portage/gentoolkit',
    'app-portage/layman',
    'app-portage/mirrorselect',
    'app-portage/portage-utils',
    'app-shells/bash-completion',
    'app-text/tree',
    'dev-util/cmake',
    'dev-util/ninja',
    'dev-vcs/git',
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
    'sys-apps/lm_sensors',
    'sys-devel/clang',
    'sys-devel/llvm',
    'sys-devel/gdb'
]

applications_base = [
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
    'www-client/links',
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
    'x11-drivers/xf86-input-keyboard',
]

applications_1 = [
    'dev-cpp/tbb',
    'app-doc/doxygen',
    'dev-java/oracle-jre-bin',
    'dev-libs/gmp',
    'dev-qt/qt-creator',
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
    'x11-apps/mesa-progs',
    '',
    '',
    '',
    '',
]

applications_games = [
    'games-arcade/sdlroids',
    'games-fps/xonotic',
    'games-action/violetland'
]

applications_kde = [
    'kde-base/kdebase-runtime-meta',
    'kde-base/kdebase-startkde',
    ''
]


def configure_applications(config):
    profile.configure(config)
    bash.configure(config)
    vim.configure(config)
    git.configure(config)
    mpv.configure(config)

