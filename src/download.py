
import os
import re
import requests
import time

def download_file_from_internet(path_from_internet, path_to_disk):
    with open(path_to_disk, 'wb') as handle:
        t = time.time()

        response = requests.get(path_from_internet, stream=True)
        length = int(response.headers['Content-Length'])

        print('Downloading ... ')
        print('destination: {}'.format(path_to_disk))
        print('     source: {}'.format(path_from_internet))
        print('     size  : {}  ({:.3f} Mb)'.format(length, length / (1024.0 * 1024.0)))
        print('     data  : {}'.format(response.headers['Last-Modified']))

        if not os.path.exists(path_to_disk) or os.path.getsize(path_to_disk) != length:
            block_size = min(max(length >> 10, 1024 * 16), 1024 * 1024 * 16) # block_size = [16kb ... 16mb]
            i = 0
            for block in response.iter_content(block_size):
                print("progress: {:7.2%} (left: {:10.3f} Mb)".format(i * block_size / length, (length - i * block_size) / (1024.0 * 1024.0)), end='\r')
                i += 1
                handle.write(block)

        print("progress: 100.00%" + " " * 50 + '\n')
        sec = time.time() - t
        print("done. [time: {:.3f} sec    speed: {:.3f} Mb/sec]".format(sec, float(length / (1024.0 * 1024.0)) / sec))

def download_stage3():
    path_to_stage3 = 'http://mirror.yandex.ru/gentoo-distfiles/releases/amd64/autobuilds/current-stage3-amd64/'
    response = requests.get(path_to_stage3)
    text = str(response.content)
    pattern = re.compile('<a href="stage3-amd64-(\d+).tar.bz2">')
    path_to_stage3 = path_to_stage3 + 'stage3-amd64-{}.tar.bz2'.format(pattern.findall(text)[0])
    download_file_from_internet(path_to_stage3, '/tmp/stage3-amd64-latest.tar.bz2')
