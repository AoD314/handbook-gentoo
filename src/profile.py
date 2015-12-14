
import subprocess

def configure():
    print('Setting profile:')
    print(subprocess.getoutput('eselect profile list'))
    print('Enter number of profile: ', end='')
    eselect = input()
    subprocess.getstatusoutput('eselect profile set {}'.format(eselect))