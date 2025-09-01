import re
from textprocess import change_sigla

def trtex(filename):
    chapter = 0
    vsnum = 0
    twodandas_just_passed = False
    lastNoteFinished = False
    onFlag = False        
    trflag = False
    noteflag = False
    noanustubh = False
    andFoll = False
    ignoreNext = False    
    firstHeader = True
    header = ''    
    collectedTr = ''
    collectedNotes = ''
    note = ''
    openfile = open(filename, "r")
    #title = 'Title'
    print("\\newcommand{\danda}{\\thinspace$\cal j$ }")
    print("\\newcommand{\\twodanda}{\\thinspace$\cal k$ }")
    print("\\input{/home/csaba/indology/dharma_project/vrsa_edition/sigla_for_tr_file.tex}")
    print("\\thispagestyle{empty}\\label{startoftranslation}")
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
        if andFoll == True:
                chap_and_vsnum = chap_and_vsnum + "--" + str(vsnum + 1)
        if '<NOTANUSTUBH/>' in line:
            notanustubh = True
        if '<ANUSTUBH/>' in line:
            notanustubh = False
        if '<TEXT>' in line:
            if '||' in line:
                vsnum += 1
                vsnum_needed = True
                twodandas_just_passed = True
            elif twodandas_just_passed == True and ignoreNext == False:
                    # MAIN print out part, prints PREVIOUS sloka's translation !
                    if collectedNotes != '':
                        print("\n\n\\slokawithfn{" + chap_and_vsnum + "}{" + collectedTr + "}")
                        print("{" + collectedNotes + "}\n\n")
                    else:
                        print("\n\n\\slokawithoutfn{" + chap_and_vsnum + "}{" + collectedTr + "}\n\n")
                    collectedTr = ''
                    collectedNotes = ''
                    print(header)
                    header = ''
                    if andFoll == True:
                       andFoll = False
                       ignoreNext = True
                    lastNoteFinished = False
                    twodandas_just_passed = False
                    firstHeader = False
            # check if we'll have to skip next verse number because we have had something like 1.8-9 before:
            elif twodandas_just_passed == True and ignoreNext == True:
                    ignoreNext = False
                    collectedTr = ''
                    collectedNotes = ''
                    lastNoteFinished = False
                    twodandas_just_passed = False
                    print(header)
                    header = ''
                    
        if '<TR>' in line or trflag == True:
            trflag = True
            if '</TR>' in line:
                trflag = False
            v01 = re.sub('.*<TR>', '', line.strip())
            if '|F|' in line:
                andFoll = True
            v01 = re.sub('\|F\|', '', v01)
            v01 = re.sub('</TR>.*', ' ', v01)
            v01 = re.sub('Ł', '\\\\skt{', v01)
            v01 = re.sub('\$', '}', v01)
            v01 = re.sub('\^', '${\\\\uparrow}$', v01)
            # final white spaces
            v01 = v01.rstrip()
            v01 = change_sigla.change_sigla(v01)                    
            # print("\ " + v01 + "%")
            collectedTr = collectedTr + " " + v01
        if '<NOTE>' in line or noteflag == True:
            noteflag = True
            v01 = re.sub('.*<NOTE>', '', line[:-1])
            v01 = re.sub('</NOTE>.*', ' ', v01)
            v01 = re.sub('\\|\\|', '\\\\twodanda', v01)
            v01 = re.sub('\\|', '\\\\danda', v01)
            v01 = re.sub('<sep/>', '\n\n', v01)
            #v01 = re.sub('<br/>', '\n', v01)
            v01 = re.sub('<br/>', ' ', v01)
            v01 = re.sub('Ł', '\\\\skt{', v01)
            v01 = re.sub('\$', '}', v01)
            v01 = re.sub('<cite>', '\\\\mycite{', v01)
            v01 = re.sub('</cite>', '}', v01)            
            v01 = re.sub('<citep>', '\\\\mycitep{', v01)
            v01 = re.sub('</citep>', '}', v01)            
            v01 = re.sub('<pnum>', '}{', v01)
            v01 = re.sub('</pnum>', '', v01)            
            #v01 = re.sub('<br/?>', '\\\\\\\\', v01)            
            v01 = change_sigla.change_sigla(v01)                                
            note = note + v01 + " "
            if '</NOTE>' in line:
                noteflag = False
            collectedNotes = collectedNotes + " " + v01
            if twodandas_just_passed == True:
               lastNoteFinished = True

            
        if '<startchapter-n="' in line:
            v01 = re.sub('.*<startchapter-n="', '', line)
            v01 = re.sub('".*', '', v01)
            chapter = int(v01) 
            #print("\\vfill\pagebreak\\begin{center}{\large\\textbf{Chapter " + str(chapter) + "}}\\end{center}")
            vsnum = 0
            firstHeader = True            
        if '<NEWCHAPTER/>' in line:
                chapter += 1
                vsnum = 1
                print("\\vfill\pagebreak\\begin{center}{\large\\textbf{Chapter " + str(chapter) + "}}\\end{center}\n\n")
        if '<TRCHAPTER>' in line:
            v01 = re.sub('.*<TRCHAPTER>', '', line)
            v01 = re.sub('</TRCHAPTER>.*', '', v01)
            print('\\vfill\pagebreak\n\n\\thispagestyle{empty}\\addcontentsline{toc}{section}{Chapter ' + str(chapter) + '}\n\\begin{center}\n{\large{' + v01.strip() + '}}\n\\end{center}\n\n')
            
        if '<TRSUBCHAPTER>' in line:
            v01 = re.sub('.*<TRSUBCHAPTER>', '', line)
            v01 = re.sub('</TRSUBCHAPTER>.*', '', v01)
            header = header + "\n\n\\begin{center}\n{{[" + v01.strip() + "]}}\n\\end{center}\n\n"
            # We need this because headers are printed after verse otherwise
            if firstHeader:
                  print(header)
                  header = ''
                  firstHeader = False

        if '<TRSUBSUBCHAPTER>' in line:
            v01 = re.sub('.*<TRSUBSUBCHAPTER>', '', line)
            v01 = re.sub('</TRSUBSUBCHAPTER>.*', '', v01)
            header = header + "\n\n\\begin{center}{{[" + v01.strip() + "]}}\\end{center}\n\n"
    openfile.close()

