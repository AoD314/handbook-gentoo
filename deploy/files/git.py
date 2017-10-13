#!/usr/bin/env python3.4

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('git')
    path_to_mpv_dir = Path(config['path_to_root'], 'home', config['user_name'])

    with create_file(Path(path_to_mpv_dir, '.gitconfig')) as f:
        print("""[user]
name = Andrey Morozov
email = morozov.andrey.vmk@gmail.com

[core]
    editor = vim
    whitespace = -indent-with-non-tab,-space-before-tab,-trailing-space,-cr-at-eol
    autocrlf = true

[alias]
    s = status
    d = diff
    c = commit
    l = log --graph --pretty=format:'%C(red)%h%C(yellow)%d%Creset %s %C(white) [%C(green)%an:%Creset %ar]'
    ll = log --graph --branches --decorate --stat --all --abbrev-commit
    lll = log --graph --branches --decorate --stat --all --abbrev-commit -p
    co = checkout
    b = branch -vv 
    ba = branch -a -vv 
    up = fetch --all --prune --recurse-submodules=yes -j4 --progress
    report = shortlog --all --branches --no-merges -n --since=7.days.ago
    wd = show --stat -p # whatdiff

[color]
    ui = true
    interactive = auto

[color "branch"]
    current = yellow bold
    local = green bold
    remote = cyan bold

[color "diff"]
    meta = yellow bold
    frag = magenta bold
    old = red bold
    new = green bold
    whitespace = white reverse

[color "status"]
    added = green bold
    changed = yellow bold
    untracked = red bold

[github]
    user = AoD314

[http]
    postBuffer = 536870912

[filter "tabspace"]
    smudge = unexpand --tabs=4 --first-only
    clean = expand --tabs=4 --initial
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)
