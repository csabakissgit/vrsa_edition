import re
from textprocess import change_sigla
from textprocess import toDevanagariExceptTagsAndCommands


numsToDevnag = {'1': '१', '2': '२', '3': '३', '4': '४', '5': '५', '6': '६', '7': '७', '8': '८', '9': '९', '0': '०'}

def turnVsnumIntoDevnagNums(chapter, vsnum):
        strChapter = str(chapter)
        devnagChapter = ''
        for digit in strChapter:
                devnagChapter = devnagChapter + numsToDevnag[digit]
        strVsnum = str(vsnum)
        devnagVsnum = ''
        for digit in strVsnum:
                devnagVsnum = devnagVsnum + numsToDevnag[digit]
        return devnagChapter + ':' + devnagVsnum
                

def tex_dn_xelatex(filename):
    chapter = 0
    firstchapter_flag = True
    vsnum = 0
    onflag = False
    textflag = False
    appflag = False
    paralflag = False
    lacunaflag = False    
    collectedLacuna = ''
    collectedParal = ''
    anustubh = True
    hemistich = 0
    proseflag = False
    pvarflag = False
    just_uvaca = False
    #print("\\renewcommand{\\dnapp}[1]{}\\renewcommand{\\rmapp}[1]{#1}")
    print("\\fejno=0\\versno=0")
    openfile = open(filename, "r")
    for line in openfile:
        # Dharma transliteration tricks
        #line = re.sub("ṃ", "\\\\.m", line)
        #line = re.sub("ṛ", "\\\\textsubring{r}", line)
        #line = re.sub("ṝ", "\\\\textsubring{\\\\=r}", line)
        #line = re.sub("ḷ", "\\\\textsubring{l}", line)
        # org *s:
        line = re.sub("^\**", "", line)
        if '<START/>' in line:
            onflag = True
        if '<STOP/>' in line:
            onflag = False
        if '<NOTANUSTUBH/>' in line:
#            print("\n\\nemsloka% ")
            anustubh = False 
            proseflag = False
            hemistich = 0
        if '<ANUSTUBH/>' in line:
            print("\n\\vers\n")
            anustubh = True
            proseflag = False
            #hemistich = 0
        if '<LONGVERSELINES/>' in line:
            print("\n\\nemslokalong\n")
        if '<NORMALVERSELINES/>' in line:
            print("\n\\nemslokanormal\n")
        if '<LITEM/>' in line:
            print("\n")
        if '<PROSE>' in line and onflag == True:
            proseflag = True
            anustubh = False
            print("\n\\prose%")
        if '</PROSE>' in line:
            proseflag = False
        if '<SETVSNUM' in line:
            v01 = re.sub('.*<SETVSNUM="', '', line)
            v01 = re.sub('".*', '', v01)
            vsnum = int(v01) - 1
            print("\\versno=" + str(vsnum))
        # the next to IF blocks function to get to the same; will get rid of <SETCHNUM at some point
        if '<SETCHNUM' in line:
            v01 = re.sub('.*<SETCHNUM="', '', line)
            v01 = re.sub('".*', '', v01)
            chapter = int(v01) 
        if '<startchapter-n="' in line and onflag == True:
            v01 = re.sub('.*<startchapter-n="', '', line)
            v01 = re.sub('".*', '', v01)
            chapter = int(v01) 
            if firstchapter_flag == False:
                # not the first chapter to process:
                print("\n\\bekveg\\szamveg\n\\vfill\n\\phpspagebreak\n\n\\szam\\bek\n\\versno=0\\fejno=" + str(chapter) + "\n\\thispagestyle{empty}\n")
                # augment chapter number
            else:
                print("\\szam\\bek\\versno=0\\fejno=" + str(chapter) + "\n\\thispagestyle{empty}\n")
                firstchapter_flag = False 
            vsnum = 0
            hemistich = 0
        # OBSOLETE
        if '<NEWCHAPTER/>' in line and onflag == True:
            if firstchapter_flag == False:
                # not the first chapter to process:
                print("\\bekveg\\szamveg\\vfill\\phpspagebreak\\szam\\bek\\fejno=" + str(chapter) + "\n")
                # augment chapter number
                v01 = "\nBACKSLASHjumpBACKSLASHnewchapter"
            else:
                # the first chapter to process:
                chapter += 1
                v01 = "BACKSLASHujfejBACKSLASHszamBACKSLASHbek\\fejno=" + str(chapter) + "\n"
            v01 = re.sub('BACKSLASH', '\\\\', v01)
            firstchapter_flag = False 
            print(v01)
            chapter += 1
            vsnum = 0
            hemistich = 0
        # if it is the main text:        
        if ('<TEXT>' in line or textflag == True) and onflag == True:
            line = re.sub("{-}", "", line)
            line = re.sub('<crux>', ' {\\\\englishfont$\\\\dag$} ', line)
            line = re.sub('</crux>', ' {\\\\englishfont$\\\\dag$} ', line)
            # before turning it into Devnag: it is needed when there is no daṇḍa and no space at the end (non-anuṣṭubh pādas a and c)
            line = re.sub('</TEXT>', ' </TEXT>', line)
            line = toDevanagariExceptTagsAndCommands.main(line)
            textflag = True
            if '</TEXT>' in line:
                textflag = False
            # check if this is the end of a verse
            if '||' in line and anustubh == True and proseflag == False:
                devnagChaptAndVsnum = turnVsnumIntoDevnagNums(chapter, vsnum)
                outputline = re.sub('\|\|', '{॥'+devnagChaptAndVsnum+'॥} \\\\vegBACKSLASHdontdisplaylinenum', line)
                hemistich = 0
                print("\n%Verse", str(chapter) + ":" + str(vsnum))
            elif '||' in line and anustubh == False and proseflag == False:
                devnagChaptAndVsnum = turnVsnumIntoDevnagNums(chapter, vsnum)
                outputline = re.sub('\|\|', '{॥'+devnagChaptAndVsnum+'॥} \\\\vegBACKSLASHdontdisplaylinenum', line)
                outputline = "\n\n\\nemslokad\n" + outputline 
                hemistich = 0
            elif '||' in line and anustubh == False and proseflag == True:
                outputline = re.sub('\|\|', '\\\\thinspace{\\\\ketdanda}', line)
            elif '|' in line and anustubh == False and proseflag == True:
                outputline = re.sub('\|', '\\\\thinspace{\\\\danda}', line)
            # special danda: it does increase verse number, e.g. after devy uvāca, but sets the next dandab to danda
            elif '|*' in line and proseflag == False:
                vsnum += 1
                outputline = re.sub('\|\*', '~{\\\\dandab}BACKSLASHdontdisplaylinenum ', line)
                just_uvaca = True
            # with anuṣṭubh, a danda increases verse number if it is the first single danda
            elif '|' in line and hemistich == 0 and anustubh == True and proseflag == False:
                if just_uvaca == False:
                    vsnum += 1                
                    outputline = re.sub('\|', '\\\\thinspace{\\\\dandab} BACKSLASHdontdisplaylinenum', line)
                else:
                    outputline = re.sub('\|', '\\\\thinspace{\\\\danda} BACKSLASHdontdisplaylinenum', line)
                    # the next single danda not a first single danda
                hemistich = 1 
                just_uvaca = False
            # if this is a first single danda but it is not anuṣṭubh, don't increase verse number    
            elif '|' in line and anustubh == False and proseflag == False:
                outputline = re.sub('\|', ' \\\\dandaBACKSLASHdontdisplaylinenum', line)
                outputline = "\n\\nemslokab\n" + outputline
                hemistich = hemistich + 1 
            elif '|' in line and hemistich > 0 and anustubh == True and proseflag == False:
                outputline = re.sub('\|', ' \\\\dandaBACKSLASHdontdisplaylinenum', line)
                hemistich = hemistich + 1 
            # check if this is a non-anuṣṭubh first line
            elif '|' not in line and hemistich == 0 and anustubh == False and proseflag == False:
                if just_uvaca == False:
                    # no indent
                    vsnum += 1
                    outputline = "\nBACKSLASHujversBACKSLASHnemsloka {" + line + "BACKSLASHdontdisplaylinenum} "
                else:
                    outputline = "\nBACKSLASHnemsloka " + line + "BACKSLASHdontdisplaylinenum "
                hemistich = 1
                just_uvaca = False
            elif '|' not in line and hemistich == 2 and anustubh == False and proseflag == False:
                # no indent
                outputline = "\nBACKSLASHnemslokac\n" + line + "BACKSLASHdontdisplaylinenum "
                hemistich = hemistich + 1
            else:
                outputline = line
            # simple substitutions
            if proseflag == False:
                v01 = re.sub('<TEXT> ?', '\n{\\\\devanagarifont ', outputline[:-1])
            if proseflag == True:
                v01 = re.sub('<TEXT> ?', '', outputline[:-1])
            # to eliminate spaces in prose passages    
            if proseflag == False:
                v01 = re.sub('</TEXT>.*', '}%', v01)
            else:
                v01 = re.sub('</TEXT>.*', '%', v01)
            v01 = re.sub('</PROSE>', '', v01)
            v01 = re.sub('<PROSE> ?', '', v01)
            v01 = re.sub('<MNTR>', '\\\\mntr{', v01)
            v01 = re.sub('</MNTR>', '}', v01)
            v01 = re.sub('<LITEM/>', '', v01)
            v01 = re.sub('{ }', " ", v01)
            v01 = re.sub('{-}', "", v01)
            v01 = re.sub('<COLOPHON>', "\n\\\\jump\n\\\\begin{center}\nBACKSLASHketdandaBACKSLASH ", v01)
            v01 = re.sub('</COLOPHON>', "BACKSLASHketdanda\n\\\\end{center}\n\\\\dontdisplaylinenum\\\\vers ", v01)
            v01 = re.sub('Ó', '{\\\\dn :}', v01)
            v01 = re.sub('ṝ', '\\\d{\\\=r}', v01)
            v01 = re.sub('ḹ', '\\\d{\\\=l}', v01)
            v01 = re.sub('<uvaca>', '', v01)
            v01 = re.sub('</uvaca>', '', v01)
            v01 = re.sub('<ja>', ' ', v01)
            v01 = re.sub('</ja>', ' ', v01)
            v01 = re.sub('BACKSLASH', '\\\\', v01)
            print(v01, end="")
        if ('<APP>' in line or appflag == True) and onflag == True:
            line = re.sub("{-}", "", line)
            line = re.sub('</LEM>', ' \\\\lem ', line)
            line = toDevanagariExceptTagsAndCommands.main(line.strip())
            # doing this to avoid line break, but it should be done after it has been turned into Devnag
            # because of final viramas
            line = re.sub(' \\\\lem ', '~\\\\lem', line)
            line = re.sub("°", "॰", line)
            appflag = True
            v01 = re.sub('<APP> ?', '    \\\\var{{\\\\devanagarifont ', line[:-1])
            if '</APP>' in line:
                appflag = False
            v01 = re.sub(' ?</APP>', '}}%', v01)
            v01 = re.sub('{ }', " ", v01)
            v01 = re.sub('{-}', "", v01)
            v01 = re.sub('<LEM>', '', v01)
            v01 = re.sub('<UNCL>', '\\\\uncl{', v01)
            v01 = re.sub('</UNCL>', '}', v01)
            v01 = re.sub('<MNTR>', '\\\\mntr{', v01)
            v01 = re.sub('</MNTR>', '}', v01)
            v01 = re.sub('<EYESKIP>', '\\\\eyeskip{\\\\englishfont ', v01)
            v01 = re.sub('</EYESKIP>', '}', v01)
            v01 = re.sub('</EYESKIP>', '}', v01)
            v01 = re.sub('ṝ', '\\\d{\\\=r}', v01)
            v01 = re.sub('ḹ', '\\\d{\\\=l}', v01)
            v01 = re.sub('\\Ł', '{\\\\englishfont ', v01)
            v01 = re.sub('\\$', '}', v01)
            v01 = re.sub('\\\\csa ?', '{ā}', v01)
            v01 = re.sub('\\\\csi ?', '{i}', v01)
            v01 = re.sub(' *\|\|', '\\\\thinspace{\\\\devanagarifont ॥}', v01)
            v01 = re.sub(' *\|', '\\\\thinspace{\\\\devanagarifont ।}', v01)
            #v01 = re.sub('\|', '{\\\\devanagarifont ।}', v01)
            v01 = re.sub('\*', '{\\\\il}', v01)
            v01 = re.sub('¤', '{\\\\il}', v01)
            v01 = re.sub('×', '{\\\\lost}', v01)
            v01 = change_sigla.change_sigla(v01)
            print(v01)
        if ('<PARAL>' in line or paralflag == True) and onflag == True:
            paralflag = True
            # " " is for final Devanagari consonant
            collectedParal = collectedParal + line + " "
            if '</PARAL>' in line:
                    paralflag = False
                    collectedParal = re.sub("°", "॰", collectedParal)
                    # for final Devanagari consonant  
                    collectedParal = re.sub("</PARAL>", " </PARAL>", collectedParal)  
                    # alternatives to Ł and $:
                    collectedParal = re.sub('<rm>', 'Ł', collectedParal)
                    collectedParal = re.sub('</rm>', '$', collectedParal)
                    collectedParal = toDevanagariExceptTagsAndCommands.main(collectedParal)                              
                    #collectedParal = re.sub('{ }', " ", collectedParal)
                    collectedParal = re.sub('<PARAL>', '    \\\\paral{{\\\\devanagarifont ', collectedParal.strip())
                    collectedParal = re.sub('</PARAL>', '}}\n', collectedParal)
                    #collectedParal = re.sub('{ }', " ", collectedParal)
                    collectedParal = re.sub('\\Ł', '{\\\\englishfont ', collectedParal)
                    collectedParal = re.sub('\\$', '}', collectedParal)
                    collectedParal = re.sub(' *\|\|', '\\\\thinspace{\\\\devanagarifont ॥}', collectedParal)
                    collectedParal = re.sub(' *\|', '\\\\thinspace{\\\\devanagarifont ।}', collectedParal)
                    collectedParal = change_sigla.change_sigla(collectedParal)                    
                    print(collectedParal, end='')
                    collectedParal = ''
        if ('<LACUNA>' in line or lacunaflag == True) and onflag == True:
            lacunaflag = True
            collectedLacuna = collectedLacuna + re.sub('{ }', "", line)
            if '</LACUNA>' in line:
                    lacunaflag = False
                    collectedLacuna = re.sub("°", "॰", collectedLacuna)
                    collectedLacuna = re.sub('<rm>', 'Ł', collectedLacuna)
                    collectedLacuna = re.sub('</rm>', '$', collectedLacuna)
                    collectedLacuna = toDevanagariExceptTagsAndCommands.main(collectedLacuna.strip())            
                    collectedLacuna = re.sub('<LACUNA> ?', '    \\\\lacuna{\\\\devanagarifont ', collectedLacuna)
                    collectedLacuna = re.sub('</LACUNA>', '}%\n', collectedLacuna)
#                   v01 = re.sub('{ }', " ", v01)
                    collectedLacuna = re.sub('\\Ł', '{\\\\englishfont ', collectedLacuna)
                    collectedLacuna = re.sub('\\$', '}', collectedLacuna)
                    collectedLacuna = re.sub('\|\|', '{\\\\devanagarifont ॥}', collectedLacuna)
                    collectedLacuna = re.sub('\|', '{\\\\devanagarifont ।}', collectedLacuna)
                    collectedLacuna = change_sigla.change_sigla(collectedLacuna)
                    print(collectedLacuna, end='')
                    collectedLacuna = ''
        if ('<PVAR>' in line or pvarflag == True) and onflag == True:
            pvarflag = True
            if '</PVAR>' in line:
                pvarflag = False
            v01 = re.sub('{ }', " ", line)
            v01 = re.sub('<PVAR>', '    \\\\prosevar{', v01[:-1])
            v01 = re.sub('</PVAR>', '}%', v01)
            v01 = re.sub('<UNCL>', '\\\\uncl{', v01)
            v01 = re.sub('</UNCL>', '}', v01)
            v01 = re.sub('<LEM>', '', v01)
            v01 = re.sub('</LEM>', '\\\\lem ', v01)
            v01 = re.sub('\\Ł', '\\\\skt{', v01)
            v01 = re.sub('\\$', '}', v01)
            print(v01)
        if '<SUBCHAPTER>' in line and onflag == True:
            line = re.sub('</SUBCHAPTER>', ' </SUBCHAPTER>', line)
            v01 = toDevanagariExceptTagsAndCommands.main(line)
            v01 = re.sub('<SUBCHAPTER>', '\n\n\\\\alalfejezet{', v01[:-1])
            v01 = re.sub('</SUBCHAPTER>', '}', v01)
            v01 = re.sub('{ }', " ", v01)
            print(v01, end="")
        if '<SUBSUBCHAPTER>' in line and onflag == True:
            line = re.sub('</SUBSUBCHAPTER>', ' </SUBSUBCHAPTER>', line)
            v01 = toDevanagariExceptTagsAndCommands.main(line)
            v01 = re.sub('<SUBSUBCHAPTER>', '\n\n\\\\alalalfejezet{', v01[:-1])
            v01 = re.sub('</SUBSUBCHAPTER>', '}', v01)
            v01 = re.sub('{ }', "", v01)
            print(v01)
        if '<CHAPTER>' in line and onflag == True:
            line = re.sub('</CHAPTER>', ' </CHAPTER>', line)
            line = toDevanagariExceptTagsAndCommands.main(line.lower().strip())
            v01 = re.sub('<chapter>', '\\\\begin{center}{\\\\Large\\\\devanagarifont{[   ', line[:-1])
            v01 = re.sub('</chapter>', ']}}\\\\end{center}', v01)
            v01 = re.sub('{ }', " ", v01)
            print(v01, end="")
        if '<TITLE>' in line and onflag == True:
            line = re.sub('</TITLE>', ' </TITLE>', line)
            line = toDevanagariExceptTagsAndCommands.main(line.lower().strip())
            v01 = re.sub('<title>', '\\\\begin{center}{\\\\Huge\\\\devanagarifont\\\\textbf{ ', line[:-1])
            v01 = re.sub('</title>', ' }}\\\\end{center}', v01)
            v01 = re.sub('{ }', "", v01)
            print(v01, end="")
        if '<TAMIL>' in line and onflag == True:
            v01 = re.sub('<TAMIL>', '', line[:-1])
            v01 = re.sub('</TAMIL>', '', v01)
            #v01 = tamil.txt2unicode.diacritic2unicode(v01)
            print(v01, "\n")
    openfile.close()


