# VIM

```
set nu
set list!
if has('gui_running')
    set listchars=tab:>-,trail:·,extends:\#,nbsp:.s
else
    set listchars=tab:>.,trail:.,extends:\#,nbsp:.
endif
```

# BASH

```
alias l="ls -lh"
alias lS="ls -lSh"
alias ll="ls -lah"
alias bigs="ls -Shal | head -n 25"
alias news="ls -lsaht | head -n 25"
alias hotm="ps -A -o rssize:10,time:9,%cpu:5,cmd | sort -nr | head | awk '{ printf \"%7.1f M  --- %s\n\", \$1/1024, \$4}{};'"
alias hotc="ps -A -o rssize:10,time:9,%cpu:5,cmd --sort -%cpu | head -n 13 | awk '{ printf \"%6.1f%% --- %s\n\", \$3, \$4}{};' | tail -n 12"
alias hddfree="du -h --max-depth=1 | sort -h"

bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'
```

# GIT 

```
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
    uncommit = reset HEAD~
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
[http]
    postBuffer = 536870912
[filter "tabspace"]
    smudge = unexpand --tabs=4 --first-only
    clean = expand --tabs=4 --initial
[user]
        email = name@email.com
        name = name
```

