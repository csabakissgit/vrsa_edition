import re
from textprocess import change_sigla
from textprocess import velthview_with_rm
#from textprocess import correctDevanagariMTglyphs

useFont = ''

numsToDevnag = {'1': '१', '2': '२', '3': '३', '4': '४', '5': '५', '6': '६', '7': '७', '8': '८', '9': '९', '0': '०'}



def changes_in_apparatus(line):
    englishfont = '\\\\englishfont'
    devanagarifont = '\\\\englishfont'
    danda = '।'
    twodandas = '॥'
    line = re.sub(' ?</APP>', '}}%', line)
    line = re.sub('{ }', " ", line)
    line = re.sub('{-}', "", line)
    # to make the lemma bold (2)
    line = re.sub(' *<LEM>', '{', line)
    #line = re.sub('<LEM>', '', line)
    #commas and semicolons
    #line = re.sub(',', '\ ', line)
    #line = re.sub(';', '\ ', line)
    #line = re.sub('\\\\va ', '{\\\\englishfont ' + str(vsnum) + 'a }', line)
    #line = re.sub('\\\\vb ', '{\\\\englishfont ' + str(vsnum) + 'b }', line)
    #line = re.sub('\\\\vc ', '{\\\\englishfont ' + str(vsnum) + 'c }', line)
    #line = re.sub('\\\\vd ', '{\\\\englishfont ' + str(vsnum) + 'd }', line)
    line = re.sub('<UNCL>', '\\\\uncl{', line)
    line = re.sub('</UNCL>', '}', line)
    line = re.sub('<MNTR>', '\\\\mntr{', line)
    line = re.sub('</MNTR>', '}', line)
    line = re.sub('<EYESKIP>', '\\\\eyeskip{'+englishfont+' ', line)
    line = re.sub('</EYESKIP>', '}', line)
    line = re.sub('</EYESKIP>', '}', line)
    line = re.sub('ṝ', '\\\d{\\\=r}', line)
    line = re.sub('ḹ', '\\\d{\\\=l}', line)
    line = re.sub('\\Ł', '{'+englishfont+' ', line)
    line = re.sub('\\$', '}', line)
    line = re.sub('\\\\csa ?', ' ', line)
    line = re.sub('\\\\csi ?', ' ', line)
    line = re.sub(' *\|\|', '\\\\thinspace{'+devanagarifont+' '+twodandas+'}', line)
    line = re.sub(' *\|', '\\\\thinspace{'+devanagarifont+' '+danda+'}', line)
    #line = re.sub('\|', '{'+devanagarifont+' '+danda+'}', line)
    line = re.sub('\*', '{\\\\il}', line)
    line = re.sub('¤', '{\\\\il}', line)
    #line = re.sub('×', '{\\\\lost}', line)
    line = re.sub('×', '', line)
    line = re.sub("<hifen>", "$\-$", line)
    line = change_sigla.change_sigla(line)
    line = re.sub('\\\\lac10', '\\\\lacwithnum{10}', line)
    line = re.sub('\\\\lac11', '\\\\lacwithnum{11}', line)
    line = re.sub('\\\\lac12', '\\\\lacwithnum{12}', line)
    line = re.sub('\\\\lac13', '\\\\lacwithnum{13}', line)
    line = re.sub('\\\\lac14', '\\\\lacwithnum{14}', line)
    line = re.sub('\\\\lac15', '\\\\lacwithnum{15}', line)
    line = re.sub('\\\\lac16', '\\\\lacwithnum{16}', line)
    line = re.sub('\\\\lac17', '\\\\lacwithnum{17}', line)
    line = re.sub('\\\\lac18', '\\\\lacwithnum{18}', line)
    line = re.sub('\\\\lac19', '\\\\lacwithnum{19}', line)
    line = re.sub('\\\\lac9', '\\\\lacwithnum{9}', line)
    line = re.sub('\\\\lac8', '\\\\lacwithnum{8}', line)
    line = re.sub('\\\\lac7', '\\\\lacwithnum{7}', line)
    line = re.sub('\\\\lac6', '\\\\lacwithnum{6}', line)
    line = re.sub('\\\\lac5', '\\\\lacwithnum{5}', line)
    line = re.sub('\\\\lac4', '\\\\lacwithnum{4}', line)
    line = re.sub('\\\\lac3', '\\\\lacwithnum{3}', line)
    line = re.sub('\\\\lac2', '\\\\lacwithnum{2}', line)
    line = re.sub('\\\\lac1', '\\\\lacwithnum{1}', line)
    return line


def turnVsnumIntoDevnagNums(chapter, vsnum):
        strChapter = str(chapter)
        devnagChapter = ''
        for digit in strChapter:
                devnagChapter = devnagChapter + numsToDevnag[digit]
        strVsnum = str(vsnum)
        devnagVsnum = ''
        for digit in strVsnum:
                devnagVsnum = devnagVsnum + numsToDevnag[digit]
        # to have the chapter number (and the verse number) printed for each verse
        #return devnagChapter + ':' + devnagVsnum
        # to have only the verse number printed for each verse
        return devnagVsnum

def tex_roman_xelatex(filename, LaTeXDn):
    if LaTeXDn:
        englishfont = '\\\\rm'
        devanagarifont = '\\\\dn'
        devanagarifontsmall = '\\\\dn'
        devanagarifontbold = '\\\\devanagarifontbold'
        devanagarifontvar = '\\\\dn'
        danda = '|'
        twodandas = '||'
    else:
        englishfont = '\\\\englishfont'
        devanagarifont = '\\\\englishfont'
        devanagarifontsmall = '\\\\englishfont'
        devanagarifontbold = '\\\\englishfont'
        devanagarifontvar = '\\\\englishfont'
        danda = '।'
        twodandas = '॥'
    romanflag = False
    chapter = 0
    firstchapter_flag = True
    # this controls an effect in the apparatus: the first entry for a verse is emphasised
    appstartforverse = '\\\\numnoemph'
    vsnum = 0
    prevvsnum = 0
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
    header = ''
    headertitle = ''
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
        if '<NOTANUSTUBH/>' in line and onflag == True:
#            print("\n\\nemsloka% ")
            anustubh = False 
            proseflag = False
            hemistich = 0
        if '<ANUSTUBH/>' in line and onflag == True:
            print("\n\\vers\n")
            anustubh = True
            proseflag = False
            #hemistich = 0
        if '<LONGVERSELINES/>' in line and onflag == True:
            print("\n\\nemslokalong\n")
            continue
        if '<NORMALVERSELINES/>' in line and onflag == True:
            print("\n\\nemslokanormal\n")
            continue
        if '<PHANTOMLINE/>' in line and onflag == True:
            print("\n{\\vrule depth.5em width0pt}\n")
            continue
        if '<EXTRAVSPACE/>' in line and onflag == True:
            print("\n{\\extravspace}\n")
            continue
        if '<LITEM/>' in line and onflag == True:
            print("\n")
        if '<PROSE>' in line and onflag == True:
            proseflag = True
            anustubh = False
            print("\n\\prose")
        if '</PROSE>' in line:
            proseflag = False
        if '<SETVSNUM' in line and onflag == True:
            v01 = re.sub('.*<SETVSNUM="', '', line)
            v01 = re.sub('".*', '', v01)
            vsnum = int(v01) - 1
            print("\\versno=" + str(vsnum))
        if '<startchapter-n="' in line and onflag == True:
            v01 = re.sub('.*<startchapter-n="', '', line)
            v01 = re.sub('".*', '', v01)
            chapter = int(v01) 
            if firstchapter_flag == False:
                # not the first chapter to process:
                print("\\bekveg\\szamveg\n\\vfill\n\\phpspagebreak\n\n\\versno=0\\fejno=" + str(chapter) + "\n\\thispagestyle{empty}\n")
                # augment chapter number
            else:
                print("\\versno=0\\fejno=" + str(chapter) + "\n\\thispagestyle{empty}\n")
                firstchapter_flag = False 
            vsnum = 0
            hemistich = 0
        # IF IT IS THE MAIN TEXT:        
        if ('<TEXT>' in line or textflag == True) and onflag == True:
            line = re.sub("{-}", "", line)
            # before turning it into Devnag: it is needed when there is no daṇḍa and no space at the end (non-anuṣṭubh pādas a and c)
            line = re.sub('</TEXT>', ' </TEXT>', line)
            '''
            if LaTeXDn:
                line, romanflag = velthview_with_rm.velthview_with_rm(line, romanflag)
            else:
                line = toDevanagariExceptTagsAndCommands.main(line)
            '''
            textflag = True
            if '</TEXT>' in line:
                textflag = False
            # check if this is the end of a verse
            if '||' in line and anustubh == True and proseflag == False:
                if LaTeXDn:
                    line = line + '\n'
                    devnagChaptAndVsnum = '\\\\dn\ '+str(chapter) + ':'+str(vsnum)+''
                else:
                    devnagChaptAndVsnum = turnVsnumIntoDevnagNums(chapter, vsnum)
                outputline = re.sub('\|\|', '{'+twodandas+" "+devnagChaptAndVsnum+twodandas+'} \\\\vegBACKSLASHdontdisplaylinenum', line)
                hemistich = 0
                print("\n%Verse", str(chapter) + ":" + str(vsnum))
            elif '||' in line and anustubh == False and proseflag == False:
                if LaTeXDn:
                    line = line + '\n'
                    devnagChaptAndVsnum = '\\\\dn\ '+str(chapter) + ':'+str(vsnum)+''
                else:
                    devnagChaptAndVsnum = turnVsnumIntoDevnagNums(chapter, vsnum)
                outputline = re.sub('\|\|', '{'+twodandas+" "+devnagChaptAndVsnum+twodandas+'} \\\\vegBACKSLASHdontdisplaylinenum', line)
                outputline = "\n\n\\nemslokad\n" + outputline 
                hemistich = 0
                print("\n%Verse", str(chapter) + ":" + str(vsnum))
            elif '||' in line and anustubh == False and proseflag == True:
                outputline = re.sub('\|\|', '\\\\thinspace{\\\\ketdanda}', line)
            elif '|' in line and anustubh == False and proseflag == True:
                outputline = re.sub('\|', '\\\\thinspace{\\\\danda}', line)
            # special danda: it does increase verse number, e.g. after devy uvāca, but sets the next dandab to danda
            elif '|*' in line and proseflag == False:
                vsnum += 1
                outputline = re.sub('\|\*', '{\\\\dandab}BACKSLASHdontdisplaylinenum ', line)
                just_uvaca = True
                appstartforverse = '\\\\numemph'
            # with anuṣṭubh, a danda increases verse number if it is the first single danda
            elif '|' in line and hemistich == 0 and anustubh == True and proseflag == False:
                if just_uvaca == False:
                    vsnum += 1
                    outputline = re.sub('\|', '\\\\thinspace{\\\\dandab} BACKSLASHdontdisplaylinenum', line)
                    appstartforverse = '\\\\numemph'
                else:
                    outputline = re.sub('\|', '\\\\thinspace{\\\\danda} BACKSLASHdontdisplaylinenum', line)
                    # the next single danda not a first single danda
                hemistich = 1
                just_uvaca = False
            # if this is a first single danda but it is not anuṣṭubh, don't increase verse number    
            elif '|' in line and anustubh == False and proseflag == False:
                outputline = re.sub('\|', ' \\\\dandaBACKSLASHdontdisplaylinenum', line)
                outputline = "\n\n\\nemslokab\n" + outputline
                hemistich = hemistich + 1 
            elif '|' in line and hemistich > 0 and anustubh == True and proseflag == False:
                outputline = re.sub('\|', ' \\\\dandaBACKSLASHdontdisplaylinenum', line)
                hemistich = hemistich + 1 
            # check if this is a non-anuṣṭubh first line
            elif '|' not in line and hemistich == 0 and anustubh == False and proseflag == False:
                if LaTeXDn:
                    line = line[:-1]
                if just_uvaca == False:
                    # no indent
                    vsnum += 1
                    appstartforverse = '\\\\numemph'
                    outputline = "\nBACKSLASHujversBACKSLASHnemsloka {" + line + "BACKSLASHdontdisplaylinenum} "
                else:
                    outputline = "\nBACKSLASHnemsloka " + line + "BACKSLASHdontdisplaylinenum "
                hemistich = 1
                just_uvaca = False
            elif '|' not in line and hemistich == 2 and anustubh == False and proseflag == False:
                if LaTeXDn:
                    line = line[:-1]
                # no indent
                outputline = "\nBACKSLASHnemslokac\n" + line + "BACKSLASHdontdisplaylinenum "
                hemistich = hemistich + 1
            elif '|' not in line and hemistich == 4 and anustubh == False and proseflag == False:
                if LaTeXDn:
                    line = line[:-1]
                # no indent
                outputline = "\nBACKSLASHnemslokae\n" + line + "BACKSLASHdontdisplaylinenum "
                hemistich = hemistich + 1
            else:
                outputline = line
            # simple substitutions
            if proseflag == False:
                v01 = re.sub('<TEXT> ?', '\n{'+devanagarifont+' ', outputline[:-1])
            if proseflag == True:
                v01 = re.sub('<TEXT> ?', '', outputline[:-1])
            # to eliminate spaces in prose passages    
            if proseflag == False:
                v01 = re.sub('</TEXT>.*', '}%\n', v01)
            else:
                v01 = re.sub('</TEXT>.*', '%\n', v01)
            v01 = re.sub('</PROSE>', '', v01)
            v01 = re.sub('<PROSE> ?', '', v01)
            v01 = re.sub('<MNTR>', '\\\\mntr{', v01)
            v01 = re.sub('</MNTR>', '}', v01)
            v01 = re.sub('<LITEM/>', '', v01)
            v01 = re.sub('{ }', " ", v01)
            v01 = re.sub('{-}', "", v01)
            v01 = re.sub('<COLOPHON>', "\n\\\\jump\n\\\\begin{center}\nBACKSLASHketdanda~", v01)
            v01 = re.sub('</COLOPHON>', "~BACKSLASHketdanda\n\\\\end{center}\n\\\\dontdisplaylinenum\\\\vers ", v01)
            v01 = re.sub('Ó', '{\\\\dn :}', v01)
            v01 = re.sub('ṝ', '\\\d{\\\=r}', v01)
            v01 = re.sub('ḹ', '\\\d{\\\=l}', v01)
            v01 = re.sub('<uvaca>', '', v01)
            v01 = re.sub('</uvaca>', '', v01)
            v01 = re.sub('<ja>', ' ', v01)
            v01 = re.sub('</ja>', ' ', v01)
            v01 = re.sub('BACKSLASH', '\\\\', v01)
            #v01 = re.sub('<crux>', '\\\\cruxdn{', v01)
            #v01 = re.sub('</crux>', '}', v01)
            #v01 = correctDevanagariMTglyphs.main(v01, useFont)
            print(v01, end="")
        if ('<APP>' in line or appflag == True) and onflag == True:
            #line = re.sub("<hy/>", "- ", line)
            line = re.sub("{-}", "", line)
            # this is the new method to hide the lemma
            #line = re.sub('<LEM!>.*</LEM>', ' \\\\lem ', line)
            # if the above is not needed, you want this:
            line = re.sub('<LEM!>', '<LEM>', line)
            # to make the lemma bold (1)
            line = re.sub('</LEM>', ' } \\\\lem ', line)
            #line = re.sub('</LEM>', ' \\\\lem ', line)
            # if a Sigma/mssALL is there before the ';' , clear the sigla before the ';'
            line = re.sub('\\\\mssALL.*;', '\\\\mssALL;', line)
            line = re.sub('<hideNepMss>', '\\\\mssN%', line)
            line = re.sub('</hideNepMss>', '%\n', line)
            line = re.sub('<hideSouthMss>', '\\\\mssS%', line)
            line = re.sub('</hideSouthMss>', '%\n', line)
            line = re.sub("\\\\-", "<hifen>", line)
            line = re.sub("<hidePada>.*</hidePada>", "", line)
            '''
            if LaTeXDn:
                line, romanflag = velthview_with_rm.velthview_with_rm(line[:-1], romanflag)
            else:
                line = toDevanagariExceptTagsAndCommands.main(line.strip())
            '''
            # doing this to avoid line break, but it should be done after it has been turned into Devnag
            # because of final viramas
            line = re.sub(' \\\\lem ', '\\\\lem', line)
            line = re.sub(' }', '}', line)
            line = re.sub("°", "॰", line)
            appflag = True
            v01 = re.sub('<APP> ?', '    \\\\var{{'+devanagarifontvar + appstartforverse, line[:-1])
            if '</APP>' in line:
                appflag = False
            v01 = changes_in_apparatus(v01)
            # spacing out a little bit:
            v01 = re.sub(",", ",\\\\hskip1em plus .9em minus .9em", v01)
            # if the ; after the lemma's witnesses should be a , instead
            v01 = re.sub(";", ",\\\\hskip1em plus .9em minus .9em", v01)
            # after first entry in app for a verse, switch off verse num highlight
            # beginning of verse switches it back
            appstartforverse = '\\\\numnoemph'
            #v01 = correctDevanagariMTglyphs.main(v01, useFont)
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
                    # hyphenation in the apparatus: \- will trigger this:
                    collectedParal = re.sub("\\\\-", "<hifen>", collectedParal)
                    '''
                    if LaTeXDn:
                        collectedParal, romanflag = velthview_with_rm.velthview_with_rm(collectedParal, romanflag)
                        collectedParal = re.sub('\|\|', twodandas, collectedParal)
                        collectedParal = re.sub('\|', danda, collectedParal)
                    else:
                        collectedParal = toDevanagariExceptTagsAndCommands.main(collectedParal.strip())
                    '''
                    #collectedParal = re.sub('{ }', " ", collectedParal)
                    collectedParal = re.sub('<PARAL>', '    \\\\paral{{'+devanagarifontsmall+' ', collectedParal.strip())
                    collectedParal = re.sub('</PARAL>', '}}\n', collectedParal)
                    #collectedParal = re.sub('{ }', " ", collectedParal)
                    collectedParal = re.sub('\\Ł', '{'+englishfont+' ', collectedParal)
                    collectedParal = re.sub('\\$', '}', collectedParal)
                    collectedParal = re.sub("<hifen>", "$\-$", collectedParal)
                    collectedParal = re.sub("<hideLPpar>", "\\\\hideLPpar{", collectedParal)
                    collectedParal = re.sub("</hideLPpar>", "}", collectedParal)
                    collectedParal = re.sub("<hideBhavPpar>", "\\\\hideBhavPpar{", collectedParal)
                    collectedParal = re.sub("</hideBhavPpar>", "}", collectedParal)
                    collectedParal = re.sub("<hideKKTpar>", "\\\\hideKKTpar{", collectedParal)
                    collectedParal = re.sub("</hideKKTpar>", "}", collectedParal)
                    collectedParal = re.sub(' *\|\|', '\\\\thinspace{'+devanagarifontsmall+' '+twodandas+'}', collectedParal)
                    collectedParal = re.sub(' *\|', '\\\\thinspace{'+devanagarifontsmall+' '+danda+'}', collectedParal)
                    #collectedParal = re.sub("<hy/>", "- ", collectedParal)
                    collectedParal = change_sigla.change_sigla(collectedParal)
                    #collectedParal = correctDevanagariMTglyphs.main(collectedParal, useFont)
                    print(collectedParal, end='')
                    collectedParal = ''
        if ('<LACUNA>' in line or lacunaflag == True) and onflag == True:
            lacunaflag = True
            collectedLacuna = collectedLacuna + re.sub('{ }', "", line)
            if LaTeXDn:
                collectedLacuna = collectedLacuna[:-1]
            if '</LACUNA>' in line:
                    lacunaflag = False
                    collectedLacuna = re.sub("°", "॰", collectedLacuna)
                    collectedLacuna = re.sub('<rm>', 'Ł', collectedLacuna)
                    collectedLacuna = re.sub('</rm>', '$', collectedLacuna)
                    collectedLacuna = re.sub('</LACUNA>', ' </LACUNA>', collectedLacuna)
                    collectedLacuna = re.sub("\\\\-", "<hifen>", collectedLacuna)
                    #collectedLacuna = toDevanagariExceptTagsAndCommands.main(collectedLacuna.strip())
                    collectedLacuna = re.sub('<LACUNA> ?', '    \\\\lacuna{'+devanagarifontsmall+' ', collectedLacuna)
                    collectedLacuna = re.sub('</LACUNA>', '}%\n', collectedLacuna)
#                   v01 = re.sub('{ }', " ", v01)
                    collectedLacuna = re.sub('\\Ł', '{'+englishfont+' ', collectedLacuna)
                    collectedLacuna = re.sub('\\$', '}', collectedLacuna)
                    collectedLacuna = re.sub(' *\|\|', '\\\\,{'+devanagarifontsmall+' '+twodandas+'}', collectedLacuna)
                    collectedLacuna = re.sub(' *\|', '\\\\,{'+devanagarifontsmall+' '+danda+'}', collectedLacuna)
                    collectedLacuna = change_sigla.change_sigla(collectedLacuna)
                    collectedLacuna = re.sub("<hifen>", "$\-$", collectedLacuna)
                    #collectedLacuna = correctDevanagariMTglyphs.main(collectedLacuna, useFont)
                    print(collectedLacuna, end='')
                    collectedLacuna = ''
        if ('<PVAR>' in line or pvarflag == True) and onflag == True:
            pvarflag = True
            if '</PVAR>' in line:
                pvarflag = False
            v01 = re.sub('{ }', "", line)
            v01 = re.sub('<PVAR>', '    \\\\prosevar{', v01[:-1])
            v01 = re.sub('</PVAR>', '}%', v01)
            v01 = re.sub('<UNCL>', '\\\\uncl{', v01)
            v01 = re.sub('</UNCL>', '}', v01)
            v01 = re.sub('<LEM>', '', v01)
            v01 = re.sub('</LEM>', '\\\\lem ', v01)
            v01 = re.sub('\\Ł', '\\\\skt{', v01)
            v01 = re.sub('\\$', '}', v01)
            '''
            if LaTeXDn:
                v01, romanflag = velthview_with_rm.velthview_with_rm(v01[:-1], romanflag)
            else:
                v01 = toDevanagariExceptTagsAndCommands.main(v01.strip())
            '''
            print(v01)
        if '<SUBCHAPTER>' in line and onflag == True:
            if LaTeXDn:
                line, romanflag = velthview_with_rm.velthview_with_rm(line.lower(), romanflag)
                line = re.sub('.*<subchapter>', '\n{\\\\centerline{{\\\\dn\\\\large [', line)
                v01 = re.sub('</subchapter>.*', ' ]}}}', line)
            else:
                line = re.sub('</SUBCHAPTER>', ' </SUBCHAPTER>', line)
                #v01 = toDevanagariExceptTagsAndCommands.main(line)
                #v01 = correctDevanagariMTglyphs.main(v01, useFont)
                v01 = re.sub('<SUBCHAPTER>', '\n\n\\\\alalfejezet{', v01.strip())
                v01 = re.sub('.?</SUBCHAPTER>', '}', v01)
                v01 = re.sub('{ }', " ", v01)
            print(v01, end="")
        if '<SUBSUBCHAPTER>' in line and onflag == True:
            if LaTeXDn:
                line, romanflag = velthview_with_rm.velthview_with_rm(line.lower(), romanflag)
                line = re.sub('<subsubchapter>', '\n{\\\\centerline{{\\\\dn [', line)
                v01 = re.sub('</subsubchapter>', ' ]}}}', line)
            else:
                line = re.sub('</SUBSUBCHAPTER>', ' </SUBSUBCHAPTER>', line)
                v01 = toDevanagariExceptTagsAndCommands.main(line)
                #v01 = correctDevanagariMTglyphs.main(v01, useFont)
                v01 = re.sub('<SUBSUBCHAPTER>', '\n\n\\\\alalalfejezet{', v01.strip())
                v01 = re.sub('.?</SUBSUBCHAPTER>', '}', v01)
                v01 = re.sub('{ }', "", v01)
            print(v01)
        if '<HEADERTITLE>' in line and onflag == True:
            if LaTeXDn:
                continue
            line = re.sub('</HEADERTITLE>', ' </HEADERTITLE>', line)
            #line = toDevanagariExceptTagsAndCommands.main(line.lower().strip())
            #line = correctDevanagariMTglyphs.main(line, useFont)
            v01 = re.sub('<headertitle>', '', line[:-1])
            headertitle = re.sub('</headertitle>', '', v01)
        if '<CHAPTER>' in line and onflag == True:
            if LaTeXDn:
                line, romanflag = velthview_with_rm.velthview_with_rm(line.lower(), romanflag)
                line = re.sub('<chapter>', '{\\\\centerline{{\\\\dn\\\\large [', line)
                v01 = re.sub('</chapter>', ' ]}}}', line)
            else:
                line = re.sub('</CHAPTER>', ' </CHAPTER>', line)
                #line = toDevanagariExceptTagsAndCommands.main(line.lower().strip())
                #line = correctDevanagariMTglyphs.main(line, useFont)
                header = re.sub('<chapter>', '', line[:-1])
                header = re.sub('</chapter>', '', header)
                if header.strip() != '':
                    v01 = re.sub('<chapter>', '\\\\centerline{\\\\Large'+devanagarifontbold+' [   ', line[:-1])
                    v01 = re.sub('</chapter>', ' ]}{\\\\vrule depth10pt width0pt}', v01)
                    v01 = re.sub('{ }', " ", v01)
                    print(v01, end="")
                if header != '':
                    print('\\fancyhead[CE]{{\\footnotesize\\devanagarifont ' + headertitle + '}}\n\\fancyhead[CO]{{\\footnotesize\\devanagarifont ' + header + '}}\n\\fancyhead[LE]{}\n\\fancyhead[RE]{}\n\\fancyhead[LO]{}\n\\fancyhead[RO]{}\n\\szam\\bek\n')
                else:
                    print('\n\\szam\\bek\n')
        if '<TITLE>' in line and onflag == True:
            if LaTeXDn:
                line, romanflag = velthview_with_rm.velthview_with_rm(line.lower(), romanflag)
                line = re.sub('<title>', '{\\\\centerline{{\\\\dn\\\\huge ', line)
                v01 = re.sub('</title>', ' }}}', line)
            else:
                line = re.sub('</TITLE>', ' </TITLE>', line)
                line = re.sub('{ }', "", line)
                #line = toDevanagariExceptTagsAndCommands.main(line.lower().strip())
                #line = correctDevanagariMTglyphs.main(line, useFont)
                v01 = re.sub('<title>', '\\\\centerline{\\\\Huge'+devanagarifontbold+' ', line[:-1])
                v01 = re.sub('</title>', ' }\n\n', v01)
            print(v01, end="\n{\\vrule depth10pt width0pt}\n")
        if '<TAMIL>' in line and onflag == True:
            v01 = re.sub('<TAMIL>', '', line[:-1])
            v01 = re.sub('</TAMIL>', '', v01)
            #v01 = tamil.txt2unicode.diacritic2unicode(v01)
            print(v01, "\n")
        if '<PAGEBREAK/>' in line and onflag == True:
            #print('\n\\vfill\n\\pageparbreak\n\\vers')
            print('\n\\pend\n\\endnumbering\n\\vfill\\pagebreak\\beginnumbering\\pstart\n\\vers')
    openfile.close()


