import sys

from general import Dir, create_file

def configure():
    print('configure sysctl.conf ... ', end='')
    sys.stdout.flush()
    
    with create_file('/etc/sysctl.conf') as f:
        print("""
net.ipv4.ip_forward = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.rp_filter = 1

vm.dirty_bytes = 67108864
vm.dirty_background_bytes = 67108864

vm.swappiness=0
""", file=f)
    print('ok')

