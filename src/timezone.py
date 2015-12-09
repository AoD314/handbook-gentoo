from general import Dir, create_file

def configure():
    print('configure timezone ... ', end='')
    sys.stdout.flush()
    
    with create_file('/etc/timezone') as f:
        print('Europe/Moscow', file=f)
    subprocess.getstatusoutput('emerge --config sys-libs/timezone-data')
    print('done')
