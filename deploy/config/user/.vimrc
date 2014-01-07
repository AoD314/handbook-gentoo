set nu
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

vnoremap < <gv  " better indentation
vnoremap > >gv  " better indentation


" Real programmers don't use TABs but spaces
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab


" " Make search case insensitive
set hlsearch
set incsearch
set ignorecase
set smartcase


" " Disable stupid backup and swap files - they trigger too many events
" " for file system watchers
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

    set lines=999
    set columns=999
    set guioptions-=m
    set guioptions-=T
endif

set history=25000
set showcmd

" python mode

set nocompatible
syntax on
set showmatch
set ignorecase
set showmode
set ts=4
set sw=4

imap <c-space> <c-x><c-o>

let g:pydiction_location = '~/vim/pydiction-1.2/'

set backspace=2
if has("autocmd")
    autocmd FileType python set complete+=k~/.vim/pydiction-1.2/pydiction isk+=.,(
endif
autocmd FileType python runtime! autoload/pythoncomplete.vim
autocmd! BufNewFile * silent! 0r ~/.vim/skeleton/template.%:e

filetype plugin on
filetype indent on

iab utf! # -*- coding: UTF-8 -*-
iab python! #!/usr/bin/env python

" Mappings
nmap <C-N> :noh <CR>

" End python mode

set incsearch
set hlsearch

set nocompatible

filetype on
filetype plugin on
filetype indent on
set ofu=syntaxcomplete#Complete

"TagList
nnoremap <silent> <F8> :TlistToggle<CR>

set showtabline=1               " File tabs allways visible
nmap <S-Left> :tabprevious<CR>
imap <S-Left> :tabprevious<CR>
map  <S-Left> :tabprevious<CR>

nmap <S-Right> :tabnext<CR>
imap <S-Right> :tabnext<CR>
map  <S-Right> :tabnext<CR>

" use Alt-Left and Alt-Right to move current tab to left or right
nnoremap <silent> <A-Left> :execute 'silent! tabmove ' . (tabpagenr()-2)<CR>
nnoremap <silent> <A-Right> :execute 'silent! tabmove ' . tabpagenr()<CR>

nmap <F3> :tab sp . <CR>
imap <F3> :tab sp . <CR>
map  <F3> :tab sp . <CR>


" вставка текста без комментариев
set fo-=ro

" Настройка свертки
set foldenable
set foldlevel=25
set foldmethod=indent
set foldnestmax=2
nnoremap <space> za
vnoremap <space> zf
"set nofoldenable       "set this to disable folding on file open

set t_Co=256

set udf

set nobackup
set nowritebackup
set noswapfile

