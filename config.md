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
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'
```
