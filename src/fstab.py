from general import create_file, run_command


def configure():
    with create_file('/etc/fstab') as f:
        print("""
# /etc/fstab: static file system information.
#
# See the manpage fstab(5) for more information.
#

#<fs>                                              <mountpoint>    <type>   <opts>                                     <dump/pass>

UUID=ccb93eec-a8b4-422b-974c-11edf8151371          /               ext4     noatime                                    0     1
UUID=c82f93da-793b-4bfd-98f8-88ac891ee77b          /music          ext4     noatime                                    0     0
UUID=d3253c40-93e7-4f4d-84dc-e4336f37da5a          /work           ext4     noatime                                    0     0
UUID=a608e1c0-aee4-49a8-b47a-8052e4f7a7fe          /youtube        ext4     noatime                                    0     0
UUID=955cb880-9e50-4bf6-87e1-64e856f84a3b          /torrent        ext4     noatime                                    0     0
UUID=0fcd1b4b-e6c9-4e4d-91de-be727b14b0a0          /movie          ext4     noatime                                    0     0
UUID=db6a0ca3-2495-42b3-988a-d17b5dc284f9          /video          ext4     noatime                                    0     0
UUID=9ea5323b-bfc1-4b56-b991-2f60ff79401a          /home           ext4     noatime,defaults                           0     0
/dev/cdrom                                         /mnt/cdrom      auto     noauto,user,ro,utf8                        0     0
tmpfs                                              /tmp            tmpfs    noatime,nodiratime,nodev,nosuid,size=8G    0     0

""", file=f)
