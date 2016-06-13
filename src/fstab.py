from general import create_file, run_command, print_log


def configure():
    with create_file('/etc/fstab') as f:
        print("""
# /etc/fstab: static file system information.
#
# See the manpage fstab(5) for more information.
#

#<fs>                                              <mountpoint>    <type>   <opts>                                     <dump/pass>

UUID=ccb93eec-a8b4-422b-974c-11edf8151371          /               ext4     noatime                                    0     1
UUID=ccb93eec-a8b4-422b-974c-11edf8151371          /boot           vfat     noatime                                    0     2
UUID=d3253c40-93e7-4f4d-84dc-e4336f37da5a          /disk           ext4     noatime                                    0     0
UUID=9ea5323b-bfc1-4b56-b991-2f60ff79401a          /home           ext4     noatime,defaults                           0     0
/dev/cdrom                                         /mnt/cdrom      auto     noauto,user,ro,utf8                        0     0
tmpfs                                              /tmp            tmpfs    noatime,nodiratime,nodev,nosuid,size=16G   0     0

""", file=f)
