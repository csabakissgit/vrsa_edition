let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <Down> <Nop>
inoremap <Up> <Nop>
inoremap <Right> <Nop>
inoremap <Left> <Nop>
inoremap <silent> <C-S> :w
inoremap <C-H> i
inoremap <C-L> lli
xmap  <Plug>SpeedDatingUp
nmap  <Plug>SpeedDatingUp
vnoremap <NL> dp   " the same downwards
nnoremap <NL> :move+
vnoremap  dkkp " for org: open subtree (if it's closed), close subtree, delete, move up, paste
nnoremap  :move-2
nnoremap <silent>  :w
vnoremap <silent>  :w
onoremap <silent>  :w
xmap  <Plug>SpeedDatingDown
nmap  <Plug>SpeedDatingDown
map @t o        <!-- <TR></TR> -->2T>
map H ^
xnoremap J :move'>+gv=gv
xnoremap K :move-2gv=gv
map L $
map Q gq
nnoremap WW :w
nmap <silent> [e <Plug>JumpDiffCharPrevEnd
nmap <silent> [b <Plug>JumpDiffCharPrevStart
nnoremap \m yiw:!grep -R --colour=always -e /home/csaba/indology/monier/mw_colored.xml 5T/2h i "^.....<pa" A | less -RF"h
vnoremap \m y:!grep -R --colour=always -e /home/csaba/indology/monier/mw_colored.xml 45h i "^.....<pa"59la | less -R70h
nmap <silent> ]e <Plug>JumpDiffCharNextEnd
nmap <silent> ]b <Plug>JumpDiffCharNextStart
vnoremap _f :!fmt -w60
nnoremap _f :!fmt -w60
nnoremap _w :VimwikiSplitLink
vnoremap _S :!sw
nnoremap _S :!sw
vnoremap _g y:!vimgrep "$(velthviewline "")"4hp  
nnoremap _g yw:!vimgrep "$(velthviewline "")"4hp
nnoremap _M y:!grep --colour=always -e /home/csaba/indology/monier/mw_colored.xml 44h i "<pi"59la | less -R70h
vnoremap _M y:!grep --colour=always -e /home/csaba/indology/monier/mw_colored.xml 45h i "<pa"59la | less -R70h
nnoremap _, yiwjjoa<APP>\vX <LEM>pa</LEM> ;</APP>0fXs
nnoremap _l yiwjoa<APP>\vX <LEM>pa</LEM> ;</APP>0fXs
nnoremap _p yiwoa<APP>\vX <LEM>pa</LEM> ;</APP>>>0fXs
vnoremap _, yjjoa<APP>\vX <LEM>pa</LEM> ;</APP>0fXs
vnoremap _l yjoa<APP>\vX <LEM>pa</LEM> ;</APP>0fXs
vnoremap _ő yoa<APP>\vX <LEM>apa°</LEM> ;</APP>>>0fXs
vnoremap _o yoa<APP>\vX <LEM>a°pa</LEM> ;</APP>>>0fXs
vnoremap _P yoa<APP>\vX <LEM>a°pa°</LEM> ;</APP>>>0fXs
vnoremap _p yoa<APP>\vX <LEM>pa</LEM> ;</APP>>>0fXs
nmap d<C-X> <Plug>SpeedDatingNowLocal
nmap d <Plug>SpeedDatingNowLocal
nmap d<C-A> <Plug>SpeedDatingNowUTC
nmap d <Plug>SpeedDatingNowUTC
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
nnoremap gV `[v`]
nnoremap j gj
nnoremap k gk
nnoremap msm a\msM
nnoremap msp a\msP
nnoremap msnd a\msNd
nnoremap msnc a\msNc
nnoremap msnb a\msNb
nnoremap msna a\msNa
nnoremap mscc a\msCc
nnoremap mscb a\msCb
nnoremap msca a\msCa
map wf :wincmd F
nnoremap <silent> <C-S> :w
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(expand((exists("g:netrw_gx")? g:netrw_gx : '<cfile>')),netrw#CheckIfRemote())
noremap <F1> :call OpenManual()
nmap <silent> <F8> <Plug>ToggleDiffCharCurrentLine
nmap <silent> <F7> <Plug>ToggleDiffCharAllLines
vnoremap <silent> <Plug>(calendar) :Calendar
nnoremap <silent> <Plug>(calendar) :Calendar
map <M-Left> :vertical resize -1
map <M-Right> :vertical resize +1
map <M-Down> :resize -1
map <M-Up> :resize +1
nnoremap <C-@> :OrgCheckBoxToggle
nnoremap <Nul> :OrgCheckBoxToggle
map <F4>  :! runvrsa  
vnoremap <F3> y:!vimgrep 'pa' 
map <F2> :! mwcolor '<<'hi
vnoremap <Up> <Nop>
vnoremap <Right> <Nop>
vnoremap <Left> <Nop>
vnoremap <Down> <Nop>
nnoremap <Down> <Nop>
nnoremap <Up> <Nop>
nnoremap <Right> :bn
nnoremap <Left> :bp
vnoremap <silent> <C-S> :w
onoremap <silent> <C-S> :w
vnoremap <C-J> dp   " the same downwards
vnoremap <C-K> dkkp " for org: open subtree (if it's closed), close subtree, delete, move up, paste
nnoremap <C-Down> zozcddpzc   " the same downwards
nnoremap <C-Up> zozcddkkpzc " for org: open subtree (if it's closed), close subtree, delete, move up, paste
nnoremap <C-J> :move+
nnoremap <C-K> :move-2
xmap <C-X> <Plug>SpeedDatingDown
xmap <C-A> <Plug>SpeedDatingUp
nmap <C-X> <Plug>SpeedDatingDown
nmap <C-A> <Plug>SpeedDatingUp
nnoremap <silent> <Plug>SpeedDatingNowUTC :call speeddating#timestamp(1,v:count)
nnoremap <silent> <Plug>SpeedDatingNowLocal :call speeddating#timestamp(0,v:count)
vnoremap <silent> <Plug>SpeedDatingDown :call speeddating#incrementvisual(-v:count1)
vnoremap <silent> <Plug>SpeedDatingUp :call speeddating#incrementvisual(v:count1)
nnoremap <silent> <Plug>SpeedDatingDown :call speeddating#increment(-v:count1)
nnoremap <silent> <Plug>SpeedDatingUp :call speeddating#increment(v:count1)
inoremap  i
inoremap  lli
inoremap <silent>  :w
cnoremap WW :w
inoremap WW :w
inoremap \sa :r! date +'<\%Y-\%m-\%d \%a>'
inoremap msm \msM
inoremap msp \msP
inoremap msnd \msNd
inoremap msnc \msNc
inoremap msnb \msNb
inoremap msna \msNa
inoremap mscc \msCc
inoremap mscb \msCb
inoremap msca \msCa
iabbr Csba Csaba
let &cpo=s:cpo_save
unlet s:cpo_save
set keymap=sanskrit
set background=dark
set backspace=indent,eol,start
set backup
set diffexpr=DiffCharExpr(200)
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set guifont=Monospace\ 16
set helplang=en
set hlsearch
set ignorecase
set iminsert=1
set incsearch
set laststatus=2
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/plugged/vim-orgmode,~/.vim/plugged/goyo.vim,~/.vim/plugged/diffchar.vim,~/.vim/pack/git-plugins/start/speeddating,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim81,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set scrolloff=12
set showcmd
set statusline=\ %F%m%r%h%w\ %=%({%{&ff}|%{(&fenc==\"\"?&enc:&fenc).((exists(\"+bomb\")\ &&\ &bomb)?\",B\":\"\")}%k|%Y}%)\ %([%l,%v][%p%%]\ %)\ %{wordcount()[\"words\"]}
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set ttimeout
set ttimeoutlen=10
set undodir=~/.vim/undodir
set undofile
set wildignore=*/.git/*,*/tmp/*,*.swp,*~,*.log,#*
set wildmenu
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/indology/dharma_project/vrsa_edition
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd vrsasarasamgraha.xml
edit vrsasarasamgraha.xml
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
lnoremap <buffer> "S Ś
lnoremap <buffer> "N Ṅ
let s:cpo_save=&cpo
set cpo&vim
lnoremap <buffer> "s ś
lnoremap <buffer> "n ṅ
lnoremap <buffer> .H Ḥ
lnoremap <buffer> .M Ṃ
lnoremap <buffer> .S Ṣ
lnoremap <buffer> .N Ṇ
lnoremap <buffer> .D Ḍ
lnoremap <buffer> .T Ṭ
lnoremap <buffer> .L Ḷ
lnoremap <buffer> .RR Ṝ
lnoremap <buffer> .R Ṛ
lnoremap <buffer> .s ṣ
lnoremap <buffer> .n ṇ
lnoremap <buffer> .d ḍ
lnoremap <buffer> .t ṭ
lnoremap <buffer> .h ḥ
lnoremap <buffer> .m ṃ
lnoremap <buffer> .ll ḹ
lnoremap <buffer> .l ḷ
lnoremap <buffer> .rr ṝ
lnoremap <buffer> .r ṛ
lnoremap <buffer> AA Ā
lnoremap <buffer> E` È
lnoremap <buffer> II Ī
lnoremap <buffer> UU Ū
lnoremap <buffer> _l ḻ
lnoremap <buffer> _r ṟ
lnoremap <buffer> a` à
lnoremap <buffer> aa ā
lnoremap <buffer> dgr °
lnoremap <buffer> e` è
lnoremap <buffer> i^ î
lnoremap <buffer> i` ì
lnoremap <buffer> ii ī
lnoremap <buffer> o` ò
lnoremap <buffer> u` ù
lnoremap <buffer> uu ū
lnoremap <buffer> ~N Ñ
lnoremap <buffer> ~n ñ
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=sanskrit
setlocal noarabic
setlocal noautoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s:<!--,e:-->
setlocal commentstring=<!--%s-->
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'xml'
setlocal filetype=xml
endif
setlocal fixendofline
setlocal foldcolumn=0
set nofoldenable
setlocal nofoldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=xmlformat#Format()
setlocal formatoptions=croql
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=1
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=o,O,*<Return>,<>>,<<>,/,{,},!^F
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=xmlcomplete#CompleteTags
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=8
setlocal noshortname
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=0
set spell
setlocal spell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'xml'
setlocal syntax=xml
endif
setlocal tabstop=8
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal undofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let s:l = 12253 - ((18 * winheight(0) + 15) / 31)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
12253
normal! 0108|
lcd ~/indology/dharma_project/vrsa_edition
tabnext 1
badd +1 ~/indology/dharma_project/vrsa_edition/vssbook/naples_xelatex_version/vss_book_xelatex.tex
badd +1 ~/indology/dharma_project/vrsa_edition/vrsasarasamgraha.xml
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
