
import subprocess

from general import run_command

def configure():
    print('Setting profile:')

    run_command('eselect profile list')
    
    print('Enter number of profile: ', end='')
    eselect = input()
    run_command('eselect profile set {}'.format(eselect))