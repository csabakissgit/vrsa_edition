import re


def rtf_substitutions(line):
        subdict = {'ā': '{\\\\u257}',
                   'ī': '{\\\\u299}',
                   'ū': '{\\\\u363}',
                   'ṛ': '{\\\\u7771}',
                   'ṝ': '{\\\\u7773}',
                   'ṃ': '{\\\\u7747}',
                   'ḥ': '{\\\\u7717}',
                   'ṅ': '{\\\\u7749}',
                   'ñ': '{\\\\u241}',
                   'ṭ': '{\\\\u7789}',
                   'ḍ': '{\\\\u7693}',
                   'ṇ': '{\\\\u7751}',
                   'ś': '{\\\\u347}', 
                   'ṣ': '{\\\\u7779}',
                   # add capitals!
                   'Ā': '{\\\\u256}',
                   'Ī': '{\\\\u298}',
                   'Ū': '{\\\\u362}',
                   'Ṛ': '{\\\\u7770}',
                   'Ṝ': '{\\\\u7772}',
                   'Ṃ': '{\\\\u7746}',
                   'Ḥ': '{\\\\u7716}',
                   'Ṅ': '{\\\\u7748}',
                   'Ñ': '{\\\\u240}',
                   'Ṭ': '{\\\\u7788}',
                   'Ḍ': '{\\\\u7692}',
                   'Ṇ': '{\\\\u7750}',
                   'Ś': '{\\\\u346}', 
                   'Ṣ': '{\\\\u7778}',
                '\\\\msALL': '<ms>∑</ms>',
                '\\\\msNC45': '<ms>N<sub>C45</sub></ms>',
                '\\\\msNK82': '<ms>N<sub>K82</sub></ms>',
                '\\\\msNCA12': '<ms>N<sub>CA12</sub></ms>',
                '\\\\msNK28': '<ms>N<sub>K28</sub></ms>',
                '\\\\msNKo77': '<ms>N<sub>Ko77</sub></ms>',
                '\\\\msNKA12': '<ms>N<sub>KA12</sub></ms>',
                '\\\\msGP74': '<ms>G<sub>P74</sub></ms>',
                '\\\\msCa': '{Ca}',
                '\\\\msCb': '{Cb}',
                '\\\\msCc': '{Cc}',
                '\\\\mssCaCbCc': '{C}',
                '\\\\msNa': '{Na}',
                '\\\\msNb': '{Nb}',
                '\\\\msNc': '{Nc}',
                '\\\\msBod': '{B}',
                '\\\\msL': '<ms>L</ms>',
                '\\\\msA': '<ms>A</ms>',
                '\\\\msB': '<ms>B</ms>',
                '\\\\msC': '<ms>C</ms>',
                '\\\\msD': '<ms>D</ms>',
                '\\\\msE': '<ms>E</ms>',
                '\\\\msF': '<ms>F</ms>',
                '\\\\msP': '<ms>P</ms>',
                '\\\\Ed': '{Ed}',
                '\\\\om': '{\\\\i omitted in }',
                '\\\\eme': '{\\\\i eme. }',
                '\\\\conj': '{\\\\i conj. }',
                '\\\\corr': '{\\\\i corr. }',
                '\\\\skt': '',
                '\\\\vab': '',
                '\\\\vcd': '',
                '\\\\vef': '',
                '\\\\va': '',
                '\\\\vb': '',
                '\\\\vc': '',
                '\\\\ve': '',
                '\\\\vf': '',
                'acorr': '<corr>ac</corr>',
                'pcorr': '<corr>pc</corr>',
                '\\\\-': '',
                '\\\\oo': "{\\\\u8226}", 
                '\\\\uncl': "",
                '\\\\kb': "≈",
                '\\\\unmetrical': "(<i>unmetrical</i>)",
                '\\\\unmetr': "(<i>unmetrical</i>)",
                '\\\\cancelled': "(<i>cancelled</i>)",
                '\\Ł': '<SKT>', 
                '\\$': '</SKT>',
                '<UNCL>': '{\\\\u8768}',
                '</UNCL>': '{\\\\u8768}',
                '<MNTR>': '<b>',
                '</MNTR>': '</b>',
                '<EYESKIPTO>': '(<i>eyeskip ',
                '</EYESKIPTO>': '</i>)',
                '--': '-',
                '°': '{\\\\u176}',
                'Ó': 'oṃ'
                } 
        for c in subdict:
            line = re.sub(c, subdict[c], line)
        return line



def rtf_output(filename):
    chapter = 0
    vsnum = 0
    textflag = False
    appflag = False
    paralflag = False
    anustubh = True
    hemistich = 0
    proseflag = False
    pvarflag = False
    trflag = False
    noteflag = False
    onflag = False
    note = ''
    pada = '<padaab>'
    # header?
    header = '''{\\rtf1\\ansi\\deff3\\adeflang1025{\\fonttbl{\\f0\\froman\\fprq2\\fcharset0 Times New Roman;}{\\f1\\froman\\fprq2\\fcharset2 Symbol;}{\\f2\\fswiss\\fprq2\\fcharset0 Arial;}{\\f3\\froman\\fprq2\\fcharset0 Liberation Serif{\\*\\falt Times New Roman};}{\\f4\\fswiss\\fprq2\\fcharset0 Liberation Sans{\\*\\falt Arial};}{\\f5\\fnil\\fprq2\\fcharset0 Noto Sans CJK SC;}{\\f6\\fnil\\fprq2\\fcharset0 Lohit Devanagari;}{\\f7\\fnil\\fprq0\\fcharset128 Lohit Devanagari;}}
{\\colortbl;\\red0\\green0\\blue0;\\red0\\green0\\blue255;\\red0\\green255\\blue255;\\red0\\green255\\blue0;\\red255\\green0\\blue255;\\red255\\green0\\blue0;\\red255\\green255\\blue0;\\red255\\green255\\blue255;\\red0\\green0\\blue128;\\red0\\green128\\blue128;\\red0\\green128\\blue0;\\red128\\green0\\blue128;\\red128\\green0\\blue0;\\red128\\green128\\blue0;\\red128\\green128\\blue128;\\red192\\green192\\blue192;}{\\stylesheet{\\s0\\snext0\\hich\\af3\\dbch\\af8\\langfe2052\\dbch\\af6\\afs24\\alang1081\\widctlpar\\hyphpar0\\ltrpar\\cf0\\loch\\f3\\fs24\\lang2057\\kerning1 Normal;}{\\*\\cs15\\snext15 Footnote Characters;}{\\*\\cs16\\snext16\\super Footnote Anchor;}{\\*\\cs17\\snext17\\super Endnote Anchor;}{\\*\\cs18\\snext18 Endnote Characters;}{\\s19\\sbasedon0\\snext20\\dbch\\af5\\dbch\\af6\\afs28\\sb240\\sa120\\keepn\\loch\\f4\\fs28 Heading;}{\\s20\\sbasedon0\\snext20\\sl276\\slmult1\\sb0\\sa140 Text Body;}{\\s21\\sbasedon20\\snext21\\dbch\\af7\\sl276\\slmult1\\sb0\\sa140 List;}{\\s22\\sbasedon0\\snext22\\dbch\\af7\\afs24\\ai\\sb120\\sa120\\noline\\fs24\\i Caption;}{\\s23\\sbasedon0\\snext23\\dbch\\af7\\noline Index;}{\\s24\\sbasedon0\\snext24\\afs20\\li339\\ri0\\lin339\\rin0\\fi-339\\noline\\fs20 Footnote;}}{\\*\\generator LibreOffice/6.4.7.2$Linux_X86_64 LibreOffice_project/40$Build-2}{\\info{\\creatim\\yr2022\\mo3\\dy21\\hr14\\min35}{\\revtim\\yr2022\\mo3\\dy21\\hr14\\min35}{\\printim\\yr0\\mo0\\dy0\\hr0\\min0}}{\\*\\userprops}\\deftab709\\hyphauto1\\viewscale120
{\\*\\pgdsctbl{\\pgdsc0\\pgdscuse451\\pgwsxn11906\\pghsxn16838\\marglsxn1134\\margrsxn1134\\margtsxn1134\\margbsxn1134\\pgdscnxt0 Default Style;}}
\\formshade\\paperh16838\\paperw11906\\margl1134\\margr1134\\margt1134\\margb1134\\sectd\\sbknone\\sectunlocked1\\pgndec\\pgwsxn11906\\pghsxn16838\\marglsxn1134\\margrsxn1134\\margtsxn1134\\margbsxn1134\\ftnbj\\ftnstart1\\ftnrstcont\\ftnnar\\aenddoc\\aftnrstcont\\aftnstart1\\aftnnrlc
{\\*\\ftnsep\\chftnsep}\\pgndec\\ql\\ltrpar\\pard\\plain \\s0\\hich\\af3\\dbch\\af8\\langfe2052\\dbch\\af6\\afs24\\alang1081\\widctlpar\\hyphpar0\\ltrpar\\cf0\\loch\\f3\\fs24\\lang2057\\kerning1\\ql\\ltrpar'''
    openfile = open(filename, "r")
    print(header)
    for line in openfile:
        if '<START/>' in line:
            onflag = True
        if '<STOP/>' in line:
            print("\n}")        
            onflag = False
            quit()
        if '<NOTANUSTUBH/>' in line:
            anustubh = False 
            proseflag = False
            hemistich = 0
        if '<ANUSTUBH/>' in line:
            anustubh = True
            proseflag = False
            #hemistich = 0
        if '<PROSE>' in line:
            proseflag = True
            anustubh = False
            print("<PROSE>")
        if '</PROSE>' in line:
            proseflag = False
            anustubh = False
            #print("</PROSE>")
        if '<startchapter-n="' in line:
            outputline = re.sub('.*<startchapter-n="', '', line)
            outputline = re.sub('".*', '', outputline)
            chapter = int(outputline) 
            vsnum = 0
            print('\par[ Chapter', chapter, ' ]\par')
        if '<SETVSNUM' in line:
            v01 = re.sub('.*<SETVSNUM="', '', line)
            v01 = re.sub('".*', '', v01)
            vsnum = int(v01) - 1
        # if it is the main text:        
        if '<TEXT>' in line or textflag == True:
            line = rtf_substitutions(line)
            textflag = True
            uvacaflag = 0
            if '</TEXT>' in line:
                textflag = False
            # check if this is the end of a verse
            if '||' in line and proseflag == False:
                chap_and_vsnum = (str(chapter) + "." + str(vsnum) + "||") 
            else:
                chap_and_vsnum = "" 
            if '||' in line and anustubh == True and hemistich == 1 and proseflag == False:
                outputline = re.sub('\|\|', '||' + chap_and_vsnum, line)
                outputline = re.sub('<TEXT>', '\\\\par', outputline)
                hemistich = 0
            elif '||' in line and anustubh == False and proseflag == False:
                outputline = re.sub('\|\|', '||' + chap_and_vsnum, line)
                outputline = re.sub('<TEXT>', '\\\\par', outputline)
                hemistich = 0
            # special danda: it does not increase verse number, e.g. after devy uvāca
            elif '|*' in line:
                uvacaflag = 1
                outputline = re.sub('\|\*', '| ', line)
                outputline = re.sub('<TEXT>', '\\\\par', outputline)
                outputline = re.sub('</TEXT>', '', outputline)
                hemistich = 0
            # with anuṣṭubh, a danda increases verse number if it is the first single danda
            elif '|' in line and hemistich == 0 and anustubh == True and proseflag == False:
                vsnum += 1
                #outputline = '\n\n<verse verseno="' + str(chapter) + "." + str(vsnum) + '"/>' + line  
                outputline = re.sub('<TEXT>', '\\\\par', line)
                # the next single danda not a first single danda
                hemistich = 1 
            # check if this is a non-anuṣṭubh first line
            elif '|' not in line and hemistich == 0 and anustubh == False:
                # no indent
                vsnum += 1
                outputline = re.sub('<TEXT>', '\\\\par', line)
                hemistich = 1
            # check if this is a non-anuṣṭubh third line
            elif '|' not in line and hemistich == 2 and anustubh == False:
                # no indent
                outputline = re.sub('<TEXT>', '\\\\par', line)
                hemistich = hemistich + 1
            # if this is a first single danda but it is not anuṣṭubh, don't increase verse number    
            elif '|' in line and anustubh == False and proseflag == False:
                outputline = re.sub('<TEXT>', '\\\\par', line)
                hemistich = hemistich + 1 
            elif '||' in line and hemistich == 2 and anustubh == True:
                outputline = re.sub('\|\|', '||' + chap_and_vsnum, line)
                outputline = re.sub('<TEXT>', '\\\\par', line)
                hemistich = 0 
            elif '|' in line and hemistich == 1 and anustubh == True:
                outputline = re.sub('<TEXT>', '\\\\par', line)
                hemistich = 2 
            else:
                outputline = line 
            v01 = re.sub('{ }', " ", outputline)
            v01 = re.sub('<COLOPHON>', "\\\\par ||", v01)
            v01 = re.sub('</COLOPHON>', "||\\\\par", v01)
            v01 = re.sub('</TEXT>.*', '', v01)
            v01 = re.sub('Ó', "oṃ", v01)
            #v01 = re.sub('<uvaca>', '', v01)
            #v01 = re.sub('</uvaca>', '', v01)
            v01 = re.sub('<ja>', ' ', v01)
            v01 = re.sub('</ja>', ' ', v01)
            v01 = re.sub('\\\\-', '', v01)
            print(v01)
        if '<APP>' in line or appflag == True:
            appflag = True
            if '</APP>' in line:
                appflag = False
            v01 = re.sub('{ }', " ", line)
            v01 = re.sub('<APP>', '{\\\\footnote {\\\\chftn ) }', v01)
            v01 = re.sub('</APP>', '}', v01)
            v01 = re.sub('<LEM>', '{\\\\b ', v01)
            v01 = re.sub('</LEM>', '] } ', v01)
            v01 = re.sub('\\\\vo', str(vsnum+uvacaflag), v01)
            v01 = re.sub('\\\\v', str(vsnum+uvacaflag), v01)
            v01 = re.sub('\\\\csa', 'ā', v01)
            v01 = re.sub('\\\\csi', 'i', v01)
            #v01 = xml_substitutions.xml_substitutions(v01)
            v01 = rtf_substitutions(v01)
            print(v01)
        if '<PARAL>' in line or paralflag == True:
            line = rtf_substitutions(line)
            paralflag = True
            if '</PARAL>' in line:
                paralflag = False
            v01 = re.sub('{ }', " ", line)
            v01 = re.sub('<PARAL>\\\\vo', "{\\\\footnote {\\\\chftn ) Parallel: }" + str(vsnum+uvacaflag), v01)
            v01 = re.sub('<PARAL>\\\\v', "{\\\\footnote {\\\\chftn ) Parallel: }" + str(vsnum+uvacaflag), v01)
            v01 = re.sub('<PARAL>', "{\\\\footnote {\\\\chftn ) Parallel: }" + str(vsnum+uvacaflag), v01)
            v01 = re.sub('</PARAL>', '}', v01)
            #v01 = xml_substitutions.xml_substitutions(v01)
            print(v01)
        if '<PVAR>' in line or pvarflag == True:
            pvarflag = True
            if '</PVAR>' in line:
                pvarflag = False
            v01 = re.sub('{ }', " ", line)
            v01 = re.sub('<PVAR>\\\\vo', "<PVAR>", v01)
            v01 = re.sub('<PVAR>\\\\v', "<PVAR>", v01)
            #v01 = xml_substitutions.xml_substitutions(v01)
            print(v01)
        if '<TR>' in line or trflag == True:
            trflag = True
            if '</TR>' in line:
                trflag = False
            v01 = re.sub('<!-- <TR>', '<TR>', line)
            v01 = re.sub('</TR> -->', '</TR>', v01)
            #v01 = xml_substitutions.xml_substitutions(v01)
            #print(v01)
        if '<NOTE>' in line or noteflag == True:
            line = rtf_substitutions(line)
            noteflag = True
            note = note + line
            if '</NOTE>' in line:
                noteflag = False
                note = re.sub('<NOTE>', "{\\\\footnote {\\\\chftn ) Note: }", note)
                note = re.sub('</NOTE>', "}", note)
                print(note)
                note = '' 
        if '<SUBCHAPTER>' in line or '<CHAPTER>' in line or '<TITLE>' in line:
            line = re.sub('{ }', " ", line)
            line = re.sub('<SUBCHAPTER>', " ", line)
            line = re.sub('</SUBCHAPTER>', " ", line)
            line = re.sub('<CHAPTER>', " ", line)
            line = re.sub('</CHAPTER>', " ", line)
            line = re.sub('<TITLE>', " ", line)
            line = re.sub('</TITLE>', " ", line)
            line = rtf_substitutions(line)
            print('\par{\\b [ ' + line + ' ]}')
    openfile.close()

#filename = "/home/csaba/indology/dharma_project/sdhs10/sivadharmasastra10_kiss.xml"

#rtf_output(filename)
