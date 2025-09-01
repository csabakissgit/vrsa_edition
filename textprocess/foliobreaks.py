# BEGINNING of file: folioinfo.py
# lists foliobreaks and other info in ms with preceding line  
# usage: textprocess.py -folioinfo 'msCa' | less -R
import re
import sys

def main(filename):
    chapter = 0
    vsnum = 0
    textflag = False
    onflag = False
    openfile = open(filename, "r")
    storedSkt = ''
    ms = sys.argv[3]
    afterFolioInfo = True
    for line in openfile:
        # not yet used here:
        if '<START/>' in line:
            onflag = True
        if '<STOP/>' in line:
            onflag = False
        if '%' == line[0]:
            textflag = False
        if '<startchapter-n="' in line:
            v01 = re.sub('.*<startchapter-n="', '', line)
            v01 = re.sub('".*', '', v01)
            chapter = int(v01) 
            vsnum = 0
            #print("\n\n\n")
            # hemistich = 0
        # OBSOLETE
        if '<NEWCHAPTER/>' in line:
                chapter += 1
                vsnum = 0
        if '<TEXT>' in line or textflag == True:
            textflag = True
            if '</TEXT>' in line:
                textflag = False
            if '||' in line:
                vsnum += 1
                chap_and_vsnum = (str(chapter) + "." + str(vsnum) + "||") 
            else:
                chap_and_vsnum = ('(in: ' + str(chapter) + "." + str(vsnum+1) + ')') 
            v01 = re.sub('.*<TEXT> ?', '', line[:-1])
            v01 = re.sub('\|\*', '|', v01)
            v01 = re.sub('\-', '|', v01)
            v01 = re.sub('</TEXT>.*', chap_and_vsnum, v01)
            v01 = re.sub('{ }', " ", v01)
            v01 = re.sub('<COLOPHON>', "\n||", v01)
            v01 = re.sub('</COLOPHON>', "||", v01)
            v01 = re.sub('<uvaca>', '', v01)
            v01 = re.sub('</uvaca>', '', v01)
            v01 = re.sub('<MNTR>', '', v01)
            v01 = re.sub('</MNTR>', '', v01)
            storedSkt = v01
            if afterFolioInfo:
                print(storedSkt)
                afterFolioInfo = False
                print()
        if '<SUBCHAPTER>' in line:
            v01 = re.sub('<SUBCHAPTER>', '\n---- ', line)
            v01 = re.sub('</SUBCHAPTER>', ' ----', v01)
        if '%folioinfo' in line and ms in line:
            print(storedSkt)
            print('\033[37;33m' + line + '\033[0m', end='')
            afterFolioInfo = True
    openfile.close()

