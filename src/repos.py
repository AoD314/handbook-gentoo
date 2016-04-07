from general import create_file


def configure():
    with create_file('/etc/portage/repos.conf/gentoo.conf') as f:
        print("""
[DEFAULT]
main-repo = gentoo

#[gentoo]
#location = /usr/portage
#sync-type = git
#sync-uri = git://anongit.gentoo.org/repo/gentoo.git
#auto-sync = yes
#sync-depth = 1 

[gentoo]
location = /usr/portage
sync-type = rsync
sync-uri = rsync://rsync.gentoo.org/gentoo-portage
auto-sync = yes

""", file=f)
