#!/usr/bin/env python3.4
import multiprocessing

from pathlib import Path
from general import create_dir, create_file, configure_print


def configure(config):
    configure_print('git')
    path_to_mpv_dir = Path(config['path_to_root'], 'home', config['user_name'])

    with create_file(Path(path_to_mpv_dir, '.gitconfig')) as f:
        print("""[user]
  name = Andrey Morozov
  email = morozov.andrey.vmk@gmail.com

[giggle]
  main-window-view = HistoryView
  history-view-vpane-position = 279

[color]
  diff = auto
  status = auto
  branch = auto
  interactive = auto
  ui = true
  pager = true

[color "branch"]
    current = yellow bold
    local = green bold
    remote = cyan bold

[color "diff"]
    meta = yellow bold
    frag = magenta bold
    old = red bold
    new = green bold
    whitespace = red reverse

[color "status"]
    added = green bold
    changed = yellow bold
    untracked = red bold

[core]
    editor = vim
    whitespace = fix,-indent-with-non-tab,trailing-space,cr-at-eol

[alias]
    s = status
    d = diff
    c = commit
    ls = log --graph --branches --decorate --stat --all
    ll = log --graph --branches --decorate --all --oneline
    lg = log --oneline --graph --decorate
    co = checkout
    b = branch -vv
    ba = branch -a -vv
    up = fetch --all --prune

[github]
  user = AoD314

[push]
  default = current

[http]
  postBuffer = 536870912""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)