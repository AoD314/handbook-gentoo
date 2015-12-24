from general import create_file


def configure():
    with create_file('/etc/portage/repos.conf/gentoo.conf') as f:
        print("""
[gentoo]
location=/usr/portage
sync-type=git
sync-uri=https://github.com/gentoo-mirror/gentoo
auto-sync=true
""", file=f)
