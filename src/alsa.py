import os
import general import run_command


def configure():
    run_command('emerge -1v media-sound/pulseaudio media-plugins/alsa-plugins')
