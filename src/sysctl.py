from general import create_file


def configure():
    with create_file('/etc/sysctl.conf') as f:
        print("""
net.ipv4.ip_forward = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.rp_filter = 1

vm.dirty_bytes = 67108864              # 64 MB
vm.dirty_background_bytes = 67108864   # 64 MB

vm.swappiness=0
""", file=f)
