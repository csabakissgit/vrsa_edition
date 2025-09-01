import re
from textprocess import change_sigla

def trtex(filename):
    chapter = 0
    vsnum = 1
    vsnum_needed = True
    twodandas_just_passed = True
    onFlag = False        
    textflag = False
    trflag = False
    noteflag = False
    noanustubh = False
    note = ''
    openfile = open(filename, "r")
    title = 'Title'
    
    print('''
    % !TEX TS-program = xelatex
    % !TEX encoding = UTF-8
    \\documentclass[12pt]{book}
    \\usepackage{fontspec} % Font selection for XeLaTeX; see fontspec.pdf for documentation
    \\defaultfontfeatures{Mapping=tex-text} % to support TeX conventions like ``---''
    \\usepackage{xunicode} % Unicode support for LaTeX character names (accents, European chars, etc)
    \\usepackage{polyglossia}
    \\newfontfamily\devanagarifont[Script=Devanagari]{Noto Serif Devanagari}
    \\newfontfamily\englishfont[Script=Latin]{EB Garamond}
    \\setmainlanguage{english}
    \\setotherlanguages{sanskrit}
    \\setmainfont{EB Garamond} 
    \\usepackage{xltxtra}
    \\usepackage[total={11.7cm,20cm}, top=4cm, left=5cm, headsep=1.1cm, footskip=1.7cm, footnotesep=1cm]{geometry}
    \\renewcommand{\\baselinestretch}{.95}
    ''')
    
    print("\\newcommand{\skt}[1]{\\textit{#1}}")
    print("\\newcommand{\danda}{\\thinspace$\cal j$ }")
    print("\\newcommand{\\twodanda}{\\thinspace$\cal k$ }")
    print("\\input{/home/csaba/indology/dharma_project/vrsa_edition/sigla_for_tr_file.tex}")
    print("\\begin{document}\\thispagestyle{empty}")
    print("\\thispagestyle{empty}")
    for line in openfile:
        if '<START/>' in line:
            onFlag = True    
        if '<STOP/>' in line:
            onFlag = False    
        if onFlag == False:
            continue
        if '<TITLE>' in line:
            title = re.sub('<.?TITLE>', '', line)
            print("\\ \\vskip6em\\begin{center}{\Huge \\textit{" + title + "}}\\vskip1em {\Large (translation)}\\bigskip\\\\ {\large\\today}\end{center}")
        chap_and_vsnum = (str(chapter) + "." + str(vsnum)) 
        if '<NOTANUSTUBH/>' in line:
            notanustubh = True
        if '<ANUSTUBH/>' in line:
            notanustubh = False
        if '<TEXT>' in line:
            if '||' in line:
                vsnum += 1
                vsnum_needed = True
                twodandas_just_passed = True
            elif ('|' in line or notanustubh == True) and ( vsnum_needed == True or twodandas_just_passed == True):
                print("\n\n\\textbf{" + chap_and_vsnum + "}%")
                vsnum_needed = False
                twodandas_just_passed = False
        if '<TR>' in line or trflag == True:
            trflag = True
            if '</TR>' in line:
                trflag = False
            v01 = re.sub('.*<TR>', '', line[:-1])
            v01 = re.sub('\|F\|', '--\\\\textbf{' + str(chapter) + "." + str(vsnum) + '}', v01)
            v01 = re.sub('</TR>.*', ' ', v01)
            v01 = re.sub('Ł', '\\\\skt{', v01)
            v01 = re.sub('\$', '}', v01)
            v01 = re.sub('\^', '${\\\\uparrow}$', v01)
            # final white spaces
            v01 = v01.rstrip()
            v01 = change_sigla.change_sigla(v01)                    
            print("\ " + v01 + "%")
        if '<NOTE>' in line or noteflag == True:
            noteflag = True
            v01 = re.sub('.*<NOTE>', '', line[:-1])
            v01 = re.sub('</NOTE>.*', ' ', v01)
            v01 = re.sub('\\|\\|', '\\\\twodanda', v01)
            v01 = re.sub('\\|', '\\\\danda', v01)
            v01 = re.sub('<sep/>', '\n\n', v01)
            v01 = re.sub('<br/>', '\n', v01)
            v01 = re.sub('Ł', '\\\\skt{', v01)
            v01 = re.sub('\$', '}', v01)
            v01 = change_sigla.change_sigla(v01)                                
            note = note + v01 + " "
            if '</NOTE>' in line:
                noteflag = False
                print("\\footnote{" + note + "}%")
                note = ""
        if '<startchapter-n="' in line:
            v01 = re.sub('.*<startchapter-n="', '', line)
            v01 = re.sub('".*', '', v01)
            chapter = int(v01) 
            vsnum = 1
        if '<NEWCHAPTER/>' in line:
                chapter += 1
                vsnum = 1
                print("\\vfill\pagebreak\\begin{center}{\large\\textbf{Chapter " + str(chapter) + "}}\\end{center}")
        if '<TRCHAPTER>' in line:
            v01 = re.sub('.*<TRCHAPTER>', '', line)
            v01 = re.sub('</TRCHAPTER>.*', '', v01)
            print("\\vfill\pagebreak\\begin{center}{\large\\textbf{" + v01 + "}}\\end{center}")
    print("\\end{document}")
    openfile.close()

