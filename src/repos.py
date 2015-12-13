import sys

from general import Dir, create_file

def configure():
    print('configure repos.conf ... ', end='')
    sys.stdout.flush()
    
    with create_file('/etc/portage/repos.conf/gentoo.conf') as f:
        print("""
[gentoo]
location=/usr/portage
sync-type=git
sync-uri=https://github.com/gentoo-mirror/gentoo
auto-sync=true
""", file=f)
    print('ok')

