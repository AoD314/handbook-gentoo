#!/usr/bin/env python3.4

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('sysctl.conf')

    with create_file(Path(config['path_to_root'], 'etc/sysctl.conf')) as f:
        print("""
net.ipv4.ip_forward = 0
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.rp_filter = 1

vm.dirty_bytes = 67108864
vm.dirty_background_bytes = 50331648

# Устанавливаем в 256 Кб размер буферов по умолчанию для приема и отправки данных через сокеты
net.core.rmem_default = 262144
net.core.wmem_default = 262144

# Устанавливаем в 16Мб максимальный размер буфера сокетов.
net.core.rmem_max = 16777216
net.core.wmem_max = 16777216

# максимальное кол-во соединений
net.ipv4.tcp_max_orphans = 65536

net.ipv4.tcp_mem=65536 131072 262144
net.ipv4.tcp_rmem=4096 87380 16777216
net.ipv4.tcp_wmem=4096 65536 16777216

net.ipv4.tcp_sack = 1
net.ipv4.tcp_no_metrics_save = 1

net.ipv4.tcp_fin_timeout = 10

# Максимальный размер очереди 
net.core.netdev_max_backlog = 2048

vm.swappiness=0
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)
