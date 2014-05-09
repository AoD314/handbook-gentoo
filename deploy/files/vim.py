#!/usr/bin/env python3.4

from pathlib import Path
from files.general import configure_print, create_file


def configure(config):
    configure_print('vim')
    path_to_root = config['path_to_root']
    user_name = config['user_name']

    with create_file(Path(path_to_root, 'home', user_name, '.vimrc')) as f:
        print("""set nu
set encoding=utf-8
set background=dark
colorscheme pablo
set completeopt=longest,menuone
nnoremap * *N
set tabstop=4
set softtabstop=4
set shiftwidth=4
set smarttab
set expandtab
set pastetoggle=<F2>
set clipboard=unnamed
map <c-j> <c-w>j
map <c-k> <c-w>k
map <c-l> <c-w>l
map <c-h> <c-w>h
vnoremap < <gv
vnoremap > >gv
set hlsearch
set incsearch
set ignorecase
set smartcase
set nobackup
set nowritebackup
set noswapfile
set smartcase
set incsearch
set autowrite
set hidden
set laststatus=2
set statusline=%<%F%h%m%r%h%w%y\ %{&ff}\ %{strftime(\"%c\")}%=\ line:%l\/%L\ col:%c%V\ pos:%o\ ascii:%b\ %P
set hlsearch
if has("gui_running")
    if has("gui_gtk2")
        set guifont=Droid\ Sans\ Mono\ 11
    elseif has("gui_win32")
        set guifont=Consolas:h11:cANSI
    endif
    set lines=9999
    set columns=999
    set guioptions-=m
    set guioptions-=T
endif
set history=25000
set showcmd
set nocompatible
syntax on
set showmatch
set ignorecase
set showmode
set ts=4
set sw=4
imap <c-space> <c-x><c-o>
set backspace=2
filetype plugin on
filetype indent on
iab utf! # -*- coding: UTF-8 -*-
iab python! #!/usr/bin/env python
nmap <C-N> :noh <CR>
set incsearch
set hlsearch
set nocompatible
filetype on
filetype plugin on
filetype indent on
set ofu=syntaxcomplete#Complete
nnoremap <silent> <F8> :TlistToggle<CR>
set showtabline=1
nmap <S-Left> :tabprevious<CR>
imap <S-Left> :tabprevious<CR>
map  <S-Left> :tabprevious<CR>
nmap <S-Right> :tabnext<CR>
imap <S-Right> :tabnext<CR>
map  <S-Right> :tabnext<CR>
nnoremap <silent> <A-Left> :execute 'silent! tabmove ' . (tabpagenr()-2)<CR>
nnoremap <silent> <A-Right> :execute 'silent! tabmove ' . tabpagenr()<CR>
nmap <F3> :tab sp . <CR>
imap <F3> :tab sp . <CR>
map  <F3> :tab sp . <CR>
set fo-=ro
set foldenable
set foldlevel=25
set foldmethod=indent
set foldnestmax=2
nnoremap <space> za
vnoremap <space> zf
set t_Co=256
set udf
set nobackup
set nowritebackup
set noswapfile
""", file=f)


if __name__ == '__main__':
    config = {'path_to_root': '/tmp', 'user_name': 'aod314'}
    configure(config)