#!/usr/bin/python3

import re
import sys

onFlag = False
textFlag = False
appFlag = False
trFlag = False
paralFlag = False
noteFlag = False
lacunaFlag = False
verseFinished = False
vsnum = 1
chapter = 1
noOfChapters = 24
mainText = []
apparatus = []
parallels = []
lacunae = []
translation = []
notes = []
samePada = False
anustubh = False
hemistich = -1
pada = ''

anustubhPadas = {-1: 'uvaca', 0: 'ab', 1: 'cd', 2: 'ef'}
nonanustubhPadas = {-1: 'uvaca', 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}

subdict ={'\\\\msNC45': '\\\\msNCfortyfive',
              '\\\\msNC94': '\\\\msNCninetyfour',
              '\\\\msNK12':  '\\\\msNKtwelve',
              '\\\\msNK12a':  '\\\\msNKtwelvea',
              '\\\\msNK12b':  '\\\\msNKtwelveb',
              '\\\\msNK82':  '\\\\msNKeightytwo',
              '\\\\msNCA12':  '\\\\msNCAtwelve',
              '\\\\msNK28':  '\\\\msNKtwentyeight',
              '\\\\msNKo77':  '\\\\msNKoseventyseven',
              '\\\\msNKA12':  '\\\\msNKAtwelve',
              '\\\\msNKA14':  '\\\\msNKAfourteen',
              '\\\\msKA14':  '\\\\msKAfourteen',
              '\\\\msGP43':  '\\\\msGPfortythree',
              '\\\\msTb72':  '\\\\msTbseventytwo',
              '\\\\msGP74':  '\\\\msGPseventyfour',
              '\\\\msS67':  '\\\\msSsixtyseven'}


filename = sys.argv[1]
openfile = open(filename, "r")

def printColophon(text):
    text = re.sub('.*<COLOPHON>', '\n\\\\centerline{\\\\maintext{\\\\dbldanda\\\\thinspace ', text)
    text = re.sub('</COLOPHON>.*', '\\\\thinspace\\\\dbldanda}}', text)
    text = re.sub('.*<TRCOLOPHON>', '\\\\translation{', text)
    text = re.sub('</TRCOLOPHON>.*', '}', text)
    print(text)


class aSktVerseLine(object):

    def __init__(self,line):
        text = line.strip()
        global hemistich
        global anustubh
        global vsnum
        global chapter
        global pada
        global onFlag
        hemistich = hemistich + 1
        if anustubh == True:
            self.metre = 'anustubh'
        else:
            self.metre = 'non-anustubh'
        if anustubh == True:
            pada = anustubhPadas[hemistich]
        elif anustubh == False:
            pada = nonanustubhPadas[hemistich]
        self.pada = pada
        self.hemistich = hemistich 
        if '||' in line or 'END' in line:
            self.endOfVerse = True
            hemistich = -1
        else:
            self.endOfVerse = False
        self.loc = (chapter, vsnum)
        self.text = text.strip()
        self.printit = onFlag

    def getText(self):
        return self.text

    def getMetre(self):
        return self.metre

    def getLoc(self):
        return self.loc

    def getPada(self):
        return self.pada

    def getHemistich(self):
        return self.hemistich

    def getTextRomanSpaces(self):
        return re.sub('{ }', ' ', self.text.strip())

    def getTextDevnagSpaces(self):
        return re.sub('{ }', '', self.text)

    def shouldPrint(self):
        return self.printit

    def getIfEndOfVerse(self):
        return self.endOfVerse








class makeAppLine(object):

    def __init__(self,line):
        global anustubh
        global vsnum
        global chapter
        global pada
        global onFlag
        self.pada = pada
        self.loc = (chapter, vsnum)
        self.text = line
        plaintext = re.sub('\\\\vo', str(self.loc[1]), line)
        plaintext = re.sub('\\\\vab', str(self.loc[1])+'ab', plaintext)
        plaintext = re.sub('\\\\vcd', str(self.loc[1])+'cd', plaintext)
        plaintext = re.sub('\\\\vef', str(self.loc[1])+'ef', plaintext)
        plaintext = re.sub('\\\\va', str(self.loc[1])+'a', plaintext)
        plaintext = re.sub('\\\\vb', str(self.loc[1])+'b', plaintext)
        plaintext = re.sub('\\\\vc', str(self.loc[1])+'c', plaintext)
        plaintext = re.sub('\\\\vd', str(self.loc[1])+'d', plaintext)
        plaintext = re.sub('\\\\ve', str(self.loc[1])+'e', plaintext)
        plaintext = re.sub('\\\\vf', str(self.loc[1])+'f', plaintext)
        plaintext = re.sub('Ł', '\\\\textit{', plaintext)
        plaintext = re.sub('\$', '}', plaintext)
        self.plaintext = plaintext
        self.printit = onFlag

    def getText(self):
        return self.text

    def getLoc(self):
        return self.loc

    def getPada(self):
        return self.pada

    def getTextRomanSpaces(self):
        return re.sub('{ }', ' ', self.text)

    def getTextDevnagSpaces(self):
        return re.sub('{ }', '', self.text)

    def getPlainTextRoman(self):
        return re.sub('{ }', ' ', self.plaintext)

    def getPlainTextDevnag(self):
        return re.sub('{ }', '', self.plaintext)

    def shouldPrint(self):
        return self.printit







class ParallelLine(object):

    def __init__(self,line):
        global anustubh
        global vsnum
        global chapter
        global pada
        global onFlag
        self.pada = pada
        self.loc = (chapter, vsnum)
        self.text = line
        plaintext = re.sub('\\\\vo', str(self.loc[1]), line)
        plaintext = re.sub('\\\\vab', str(self.loc[1])+'ab', plaintext)
        plaintext = re.sub('\\\\vcd', str(self.loc[1])+'cd', plaintext)
        plaintext = re.sub('\\\\vef', str(self.loc[1])+'ef', plaintext)
        plaintext = re.sub('\\\\va', str(self.loc[1])+'a', plaintext)
        plaintext = re.sub('\\\\vb', str(self.loc[1])+'b', plaintext)
        plaintext = re.sub('\\\\vc', str(self.loc[1])+'c', plaintext)
        plaintext = re.sub('\\\\vd', str(self.loc[1])+'d', plaintext)
        plaintext = re.sub('\\\\ve', str(self.loc[1])+'e', plaintext)
        plaintext = re.sub('\\\\vf', str(self.loc[1])+'f', plaintext)
        plaintext = re.sub('Ł', '\\\\textit{', plaintext)
        plaintext = re.sub('\\$', '}', plaintext)
        self.plaintext = plaintext
        self.printit = onFlag

    def getText(self):
        return self.text

    def getLoc(self):
        return self.loc

    def getPada(self):
        return self.pada

    def getTextRomanSpaces(self):
        return re.sub('{ }', ' ', self.text)

    def getTextDevnagSpaces(self):
        return re.sub('{ }', '', self.text)

    def getPlainTextRoman(self):
        return re.sub('{ }', ' ', self.plaintext)

    def getPlainTextDevnag(self):
        return re.sub('{ }', '', self.plaintext)

    def shouldPrint(self):
        return self.printit





class LacunaLine(ParallelLine):

    pass
    '''
    def __init__(self,line):
        global anustubh
        global vsnum
        global chapter
        global pada
        global onFlag
        self.pada = pada
        self.loc = (chapter, vsnum)
        self.text = line
        plaintext = re.sub('\\\\vo', str(self.loc[1]), line)
        plaintext = re.sub('\\\\vab', str(self.loc[1])+'ab', plaintext)
        plaintext = re.sub('\\\\vcd', str(self.loc[1])+'cd', plaintext)
        plaintext = re.sub('\\\\vef', str(self.loc[1])+'ef', plaintext)
        plaintext = re.sub('\\\\va', str(self.loc[1])+'a', plaintext)
        plaintext = re.sub('\\\\vb', str(self.loc[1])+'b', plaintext)
        plaintext = re.sub('\\\\vc', str(self.loc[1])+'c', plaintext)
        plaintext = re.sub('\\\\vd', str(self.loc[1])+'d', plaintext)
        plaintext = re.sub('\\\\ve', str(self.loc[1])+'e', plaintext)
        plaintext = re.sub('\\\\vf', str(self.loc[1])+'f', plaintext)
        plaintext = re.sub('Ł', '\\\\textit{', plaintext)
        plaintext = re.sub('\\$', '}', plaintext)
        self.plaintext = plaintext
        self.printit = onFlag

    def getText(self):
        return self.text

    def getLoc(self):
        return self.loc

    def getPada(self):
        return self.pada

    def getTextRomanSpaces(self):
        return re.sub('{ }', ' ', self.text)

    def getTextDevnagSpaces(self):
        return re.sub('{ }', '', self.text)

    def getPlainTextRoman(self):
        return re.sub('{ }', ' ', self.plaintext)

    def getPlainTextDevnag(self):
        return re.sub('{ }', '', self.plaintext)

    def shouldPrint(self):
        return self.printit
    '''





class TrLine(object):

    def __init__(self,line):
        global vsnum
        global chapter
        global onFlag
        self.loc = (chapter, vsnum)
        self.text = line
        plaintext = re.sub('ŁŁ', '\\\\sktx{', line)
        plaintext = re.sub('\$\$', '}', plaintext)
        plaintext = re.sub('-##Ł', '\\\\mysktindex{', plaintext)
        plaintext = re.sub('\$##-', '}', plaintext)
        plaintext = re.sub('Ł', '\\\\textit{', plaintext)
        plaintext = re.sub('\$', '}', plaintext)
        plaintext = re.sub('<skt>', '\\\\textit{', plaintext)
        plaintext = re.sub('</skt>', '}', plaintext)
        plaintext = re.sub('.*<TR> *', '', plaintext)
        plaintext = re.sub('</TR>.*', '', plaintext)
        plaintext = re.sub(' +', ' ', plaintext)
        plaintext = re.sub('-##', '\\\\myidx{', plaintext)
        plaintext = re.sub('##-', '}', plaintext)
        plaintext = re.sub('-#', '\\\\enx{', plaintext)
        plaintext = re.sub('#-', '}', plaintext)
        #plaintext = re.sub('<tothepowerof>', '\\\\raise .5em\\\\hbox{\\\\footnotesize ', plaintext)
        plaintext = re.sub('<tothepowerof>', '$^{\\\\englishfont\\\\tiny ', plaintext)
        plaintext = re.sub('</tothepowerof>', '\\\\thinspace}$', plaintext)
        self.plaintext = plaintext
        self.printit = onFlag

    def getText(self):
        return self.text

    def getLoc(self):
        return self.loc

    def getTextRomanSpaces(self):
        return re.sub('{ }', ' ', self.text)

    def getTextDevnagSpaces(self):
        return re.sub('{ }', '', self.text)

    def getPlainTextRoman(self):
        return re.sub('{ }', ' ', self.plaintext)

    def getPlainTextDevnag(self):
        return re.sub('{ }', '', self.plaintext)

    def shouldPrint(self):
        return self.printit


def addLineToApp(line):
    apparatus.append(makeAppLine(line))

def addLineToTr(line):
    translation.append(TrLine(line))

def addLineToParallels(line):
    parallels.append(ParallelLine(line))

def addLineToLacunae(line):
    lacunae.append(LacunaLine(line))

def addLineToNotes(line):
    notes.append(NoteLine(line))

def processSigla(line):
    global subdict
    for siglum in subdict:
        line = re.sub(siglum, subdict[siglum], line)
    return line


class NoteLine(object):

    def __init__(self,line):
        global vsnum
        global chapter
        global onFlag
        self.loc = (chapter, vsnum)
        self.text = line
        plaintext = re.sub('ŁŁ', '\\\\sktx{', line)
        plaintext = re.sub('\$\$', '}', plaintext)
        plaintext = re.sub('-##Ł', '\\\\mysktindex{', plaintext)
        plaintext = re.sub('\$##-', '}', plaintext)
        plaintext = re.sub('Ł', '\\\\textit{', plaintext)
        plaintext = re.sub('\$', '}', plaintext)
        plaintext = re.sub('<skt>', '\\\\textit{', plaintext)
        plaintext = re.sub('</skt>', '}', plaintext)
        plaintext = re.sub('<b>', '\\\\textbf{', plaintext)
        plaintext = re.sub('</b>', '}', plaintext)
        plaintext = re.sub('.*<NOTE>', '', plaintext)
        plaintext = re.sub('</NOTE>.*', '', plaintext)
        plaintext = re.sub(' +', ' ', plaintext)
        plaintext = re.sub('-##', '\\\\myidx{', plaintext)
        plaintext = re.sub('##-', '}', plaintext)
        plaintext = re.sub('-#', '\\\\enx{', plaintext)
        plaintext = re.sub('#-', '}', plaintext)
        plaintext = re.sub('<br\/>', '\n ', plaintext)
        #plaintext = re.sub('<br\/>', ' ', plaintext)
        plaintext = re.sub('<sep\/>', '\n ', plaintext)
        plaintext = re.sub('<sep\/>', ' %', plaintext)
        plaintext = re.sub('<nocite>', '\\\\nocite{', plaintext)
        plaintext = re.sub('</nocite>', '}', plaintext)
        plaintext = re.sub('<cite>', '\\\\mycite{', plaintext)
        plaintext = re.sub('</cite>', '}', plaintext)
        plaintext = re.sub('<citeyear>', '\\\\citeyear{', plaintext)
        plaintext = re.sub('</citeyear>', '}', plaintext)
        plaintext = re.sub('<citep>', '\\\\mycitep{', plaintext)
        plaintext = re.sub('</citep>', '}', plaintext)
        plaintext = re.sub('<pnum>', '{', plaintext)
        plaintext = re.sub('</pnum>', '}', plaintext)
        plaintext = re.sub('<pageref>', '\\\\pageref{', plaintext)
        plaintext = re.sub('</pageref>', '}', plaintext)
        plaintext = re.sub('<tothepowerof>', '$^{', plaintext)
        plaintext = re.sub('</tothepowerof>', '}$', plaintext)
        plaintext = re.sub('<UNCL>', '\\\\uncl{', plaintext)
        plaintext = re.sub('</UNCL>', '}', plaintext)
        plaintext = re.sub('\\\\rightarrow', '$\\\\rightarrow$', plaintext)
        plaintext = re.sub('\\\\leftarrow', '$\\\\leftarrow$', plaintext)
        plaintext = re.sub(' \|', '\\\\thinspace |', plaintext)

        self.plaintext = plaintext
        self.printit = onFlag

    def getText(self):
        return self.text

    def getLoc(self):
        return self.loc

    def getTextRomanSpaces(self):
        return re.sub('{ }', ' ', self.text)

    def getTextDevnagSpaces(self):
        return re.sub('{ }', '', self.text)

    def getPlainTextRoman(self):
        return re.sub('{ }', ' ', self.plaintext)

    def getPlainTextDevnag(self):
        return re.sub('{ }', '', self.plaintext)

    def shouldPrint(self):
        return self.printit






def texrm_tr_notes(mainText, apparatus, translation, notes):
    # the main function to print Skt, translation and notes
    global samePada
    global hemistich
    #Anything to be printed before we print the stuff?
    output = ''
    #output = '\\begin{center}{\\huge\\textbf{\\englishfont Śivadharmaśāstra}}\\end{center}\\vskip2em'
    # go through the items in the Skt
    for item in mainText:
        #print(item.getText(), item.getLoc())
        indentation = ''
        chapterNum = item.getLoc()[0]
        verseNum = item.getLoc()[1]

        if item.shouldPrint():
            if 'COLOPHON' in item.getText():
                printColophon(item.getText())
                continue
            text = re.sub('.*<TEXT> *', '\\\\maintext{', item.getTextRomanSpaces())
            text = re.sub('</TEXT>.*', '}', text)
            # this is done here not to mess up the \fancyhead etc line below
            text = re.sub('\[', '{\\\\rm [}', text)
            text = re.sub(']', '{\\\\rm ]}', text)
            text = re.sub('.*<CHAPTER>', '\n\\\\chptr{', text)
            #multiple chapters (VSS)
            text = re.sub('</CHAPTER>.*', '}\n\\\\fancyhead[CO]{{\\\\footnotesize\\\\textit{Translation of chapter ' + str(chapterNum) + '}}}', text)
            #text = re.sub('</CHAPTER>.*', '}\n\\\\addcontentsline{toc}{section}{Chapter '+str(chapterNum)+'}\n\\\\fancyhead[CO]{{\\\\footnotesize\\\\textit{Translation of chapter ' + str(chapterNum) + '}}}', text)
            #one chapter (ŚDhŚ10)
            #text = re.sub('</CHAPTER>.*', '}\n\\\\fancyhead[CO]{{\\\\footnotesize\\\\textit{Translation of Śivadharmaśāstra ' + str(chapterNum) + '}}}', text)
            text = re.sub('.*<TRCHAPTER>', '\\\\trchptr{', text)
            text = re.sub('</TRCHAPTER>.*', '}', text)
            text = re.sub('.*<SUBCHAPTER>', '\\\\subchptr{', text)
            text = re.sub('</SUBCHAPTER>.*', '}', text)
            text = re.sub('.*<TRSUBCHAPTER>', '\\\\trsubchptr{', text)
            text = re.sub('</TRSUBCHAPTER>.*', '}', text)
            text = re.sub('.*<SUBSUBCHAPTER>', '\\\\subsubchptr{', text)
            text = re.sub('</SUBSUBCHAPTER>.*', '}', text)
            text = re.sub('.*<TRSUBSUBCHAPTER>', '\\\\trsubsubchptr{', text)
            text = re.sub('</TRSUBSUBCHAPTER>.*', '}', text)
            text = re.sub('\|', ' |', text)
            text = re.sub('\| \|', '', text)
            text = re.sub('\|\*', '|', text)
            text = re.sub('<crux>', '{\\\\rm †}', text)
            text = re.sub('</crux>', '{\\\\rm †}', text)
            if item.getIfEndOfVerse():
                ##if you need the chapter numbers:
                tail = '||\\thinspace' + str(chapterNum) + ':' + str(verseNum) + '\\thinspace||'
                ##if you don't need the chapter numbers:
                #tail = '||\\thinspace ' + str(verseNum) + '\\thinspace||'
            else:
                tail = ''
            if item.getPada() == 'b' or item.getPada() == 'd' or item.getPada() == 'f':
                indentation = '\\nonanustubhindent'
            # here we print the Sanskrit text
            output += '\n ' + indentation + " " + text.strip() + tail + '%\n'

            # uncomment if you need the apparatus
            '''
            for appitem in apparatus:
                if appitem.getLoc() == (chapterNum, verseNum) and (appitem.getPada() in item.getPada() or appitem.getPada() == ''):
                    appLine = re.sub('<APP>', '\\\\var{\\\\textbf{', appitem.getPlainTextRoman())
                    appLine = re.sub('</APP>', '}', appLine)
                    appLine = processSigla(appLine)
                    if samePada:
                        appLine = re.sub(' *<LEM>', ' ', appLine)
                    else:
                        appLine = re.sub(' *<LEM>', '} ', appLine)
                    if '\\oo' in appLine:
                        samePada = True
                        appLine = re.sub('\\\\oo', ' •', appLine)
                    else:
                        samePada = False
                    appLine = re.sub('</LEM>', '~]', appLine)
                    print('       ', appLine.strip())

            for paralitem in parallels:
                if paralitem.getLoc() == (chapterNum, verseNum) and (paralitem.getPada() in item.getPada() or paralitem.getPada() == ''):
                    paralLine = re.sub('<PARAL>', '\\\\paral{', paralitem.getPlainTextRoman())
                    paralLine = re.sub('</PARAL>', '}', paralLine)
                    paralLine = processSigla(paralLine)
                    print(paralLine.strip())

            for lacunaitem in lacunae:
                if lacunaitem.getLoc() == (chapterNum, verseNum) and (lacunaitem.getPada() in item.getPada() or lacunaitem.getPada() == ''):
                    lacunaLine = re.sub('<LACUNA>', '\\\\lacuna{', lacunaitem.getPlainTextRoman())
                    lacunaLine = re.sub('</LACUNA>', '}', lacunaLine)
                    lacunaLine = processSigla(lacunaLine)
                    print(lacunaLine.strip())

            '''


            # when we have finished printing the Skt verse:
            if item.getIfEndOfVerse():

                # PRINT TRANSLATION
                output += '\\translation{'
                trStarted = False
                for tritem in translation:
                        if tritem.getLoc() == (chapterNum, verseNum):
                            if trStarted != True:
                                # uncomment this section if you need chapter and verse numbers for the translation
                                '''
                                if '|F|' in tritem.getPlainTextRoman():
                                    print(str(chapterNum) + ':' + str(verseNum-1) + "--" + str(verseNum))
                                else:
                                    print(str(chapterNum) + ':' + str(verseNum))
                                trStarted = True
                                '''
                            # here we print the translation
                            output += processSigla(re.sub('\|F\|', '', tritem.getPlainTextRoman())).strip() + " "


                   #     print(tritem.getText())
                # here we print the notes
                firstNotehere = True
                for noteitem in notes:
                        if noteitem.getLoc() == (chapterNum, verseNum):
                            if firstNotehere:
                                output += '\\blankfootnote{' + str(noteitem.getLoc()[0]) + '.' + str(noteitem.getLoc()[1]) + " "
                                #output += '\\blankfootnote{v.~' + str(noteitem.getLoc()[1]) + " "
                                firstNotehere = False
                            output += processSigla(noteitem.getPlainTextRoman()) + " "
                if firstNotehere == False:
                    output += '}' # closing footnotes
                output += '}'     # closing translation
                # this gets rid of the \translation{ } bits that only contain a footnote and no translation
                output = re.sub('\\\\translation{\\\\blank', '{\\\\blank', output)
                # this gets rid of the \translation{} bits that only contain no translation
                output = re.sub('\\\\translation{}', '', output)
                # makeing all these non-italic in the translation: [ ] ( ) ([0-9]*)
                output = re.sub('(\([0-9]*\))', '{\\\\rm \\1}', output)
                output = re.sub('\(', '{\\\\rm (}', output)
                output = re.sub('\)', '{\\\\rm )}', output)
                output = re.sub(r' \\blankfootnote', r'\\blankfootnote', output)
                output = re.sub('PAGEBREAK.*', '}}\n\\\\vfill\\\\pagebreak\n', output)
                print(output)
                output = ''



'''
def txt_and_app(mainText, apparatus):
    for item in mainText:
        chapterNum = item.getLoc()[0]
        verseNum = item.getLoc()[1]
        if item.shouldPrint():
            print(item.getTextRomanSpaces(), item.getLoc())
        if '||' in item.getTextRomanSpaces(): 
            for item in apparatus:
                if item.getLoc() == (chapterNum, verseNum) and item.shouldPrint():
                    print("       ", item.getPlainTextRoman())
'''

for line in openfile:
    if '<START/>' in line:
        onFlag = True
        hemistich = -1
    if '<STOP/>' in line:
        onFlag = False
    #if '<PROSE>' in line:
    #    onFlag = False
    #if '</PROSE>' in line:
    #    onFlag = True
    if '<NOTANUSTUBH/>' in line:
        anustubh = False
    if '<ANUSTUBH/>' in line:
        anustubh = True
    if '<TEXT>' in line or textFlag == True:
        textFlag = True
        if verseFinished == True:
            vsnum += 1
        mainText.append(aSktVerseLine(line))
    if '|*' in line:
        hemistich = -1
    if '<APP>' in line or appFlag == True:
        appFlag = True
        #addLineToApp(line)
    if '</APP>' in line:
        appFlag = False
    if '<PARAL>' in line or paralFlag == True:
        paralFlag = True
        #addLineToParallels(line)
    if '</PARAL>' in line:
        paralFlag = False
    if '<LACUNA>' in line or lacunaFlag == True:
        lacunaFlag = True
        addLineToLacunae(line)
    if '</LACUNA>' in line:
        lacunaFlag = False
    if '</PARAL>' in line:
        paralFlag = False
    if '<TR>' in line or trFlag == True:
        trFlag = True
        addLineToTr(line)
    if '</TR>' in line:
        trFlag = False
    if '<NOTE>' in line or noteFlag == True:
        noteFlag = True
        addLineToNotes(line) 
    if '</NOTE>' in line:
        noteFlag = False
    if '<TEXT>' in line or textFlag == True:
        if '||' in line:
            verseFinished = True
        else:
            verseFinished = False
    if '</TEXT>' in line:
        textFlag = False
    if '<startchapter-n="' in line and onFlag == True:
        v01 = re.sub('.*<startchapter-n="', '', line)
        v01 = re.sub('".*', '', v01)
        chapter = int(v01) 
        vsnum = 1
        hemistich = -1
    if '<CHAPTER>' in line or '<SUBCHAPTER>' in line or '<SUBSUBCHAPTER>' in line:
        hemistich = -2
        mainText.append(aSktVerseLine(line))
    if '<TRCHAPTER>' in line or '<TRSUBCHAPTER>' in line or '<TRSUBSUBCHAPTER>' in line:
        hemistich = -2
        # we actually add the translation headers to the Sanskrit...
        line = re.sub('Ł', '\\\\textit{', line)
        line = re.sub('\$', '}', line)
        mainText.append(aSktVerseLine(line))
    if '<TRCOLOPHON>' in line: 
        hemistich = -2
        line = re.sub('Ł', '\\\\textit{', line)
        line = re.sub('\$', '}', line)
        mainText.append(aSktVerseLine(line))
    if '<TRPAGEBREAK/>' in line:
            addLineToNotes("PAGEBREAK")

texrm_tr_notes(mainText, apparatus, translation, notes)



