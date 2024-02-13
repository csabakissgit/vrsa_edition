- the main file has now the extension .cred ('critical editio'), mostly because
  I have made a .cred syntax file (~/.vim/syntax/cred.vim) in Vim, which works
  well with ~/.vim/colors/csabacolors.vim; but .xml is also ol

- to produce a xelatex critical edition pdf, the .cred file is fed into
  ~/bin/textprocess.py -texdnxelatex ... and the resulting file is \input into
  a tex file; there are several additional macro files

- to produce a pdf with the Sanskrit in Roman plus translation and notes, the
  .cred file is fed into ~/bin/objectoriented_textprocess.py; it is inputed
  into the main book.tex file

- to produce a html file, -html ...; the resulting html file works
  with some static css and js scripts
 
- the above is collected in runvrsa and rundsdhs10 with additional 
  makeindex and bibtex processes there is of course a corresponding 
  .bib file in each case

- if the notes are separately, e.g. extracted by the javascipt page
  textprocess_javascript.html (each note is one line, starting with verse
  numner thus: '10.38:'), you can put them back into a new file by using
  ~/bin/textprocess/externalnotes.py; the resulting file should be the new .cred file

- search for problems in the apparatus with textprocess.py -appcheck xxx.cred 'list, of, sigla' [lastlinenumtocheck]
