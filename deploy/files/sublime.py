#!/usr/bin/env python3.4

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('sublime')

    with create_file(Path(config['path_to_root'], 'home', config['user_name'],'.config/sublime-text-2/Packages/User/Preferences.sublime-settings')) as f:
        print("""{
    "color_scheme": "Packages/Color Scheme - Default/Sunburst.tmTheme",
    "font_face": "Liberation Mono",
    "font_size": 10,
    "translate_tabs_to_spaces": true,
    "tab_size": 4,
    "auto_complete_delay": 10,
    "rulers": [80, 120],
    "highlight_modified_tabs": true,
    "draw_white_space": "all"
}
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp'}
    configure(config)