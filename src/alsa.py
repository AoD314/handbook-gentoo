import os


def configure():
    print('configure alsa + pulseaudio')
    os.system('emerge -1v media-sound/pulseaudio media-plugins/alsa-plugins')
