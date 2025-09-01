#!/usr/bin/python3
# By Csaba Kiss

# regex:
import re
# for the commandline arguments:
import sys


vowels = ['a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'e', 'ai', 'o', 'au']

def isFullPada(text):
    '''
    Decides if there are 8 Skt vowels in line or not
    '''
    canBeDiphtong = False
    numOfVowels = 0
    for letter in text:
        if letter in vowels:
            numOfVowels += 1
            if letter == 'a':
                canBeDiphtong = True
            elif letter != 'i' and letter != 'u':
                canBeDiphtong = False
            if canBeDiphtong and (letter == 'i' or letter == 'u'):
                canBeDiphtong = False
                numOfVowels -= 1
        else:
            canBeDiphtong = False
    return numOfVowels == 8


def main(filename):
    '''
    If this is a full pāda within <LEM></LEM>, with 8 vowels, it inserts <hidePada></hidePada> tags
    '''
    countInserts = 0
    openfile = open(filename, "r")
    for line in openfile:
        if '\\va <LEM>' in line or '\\vb <LEM>' in line or '\\vc <LEM>' in line or '\\vd <LEM>' in line:
            lemma = re.sub('.*<LEM>', '', line)
            lemma = re.sub('</LEM>.*', '', lemma)
            if isFullPada(lemma):
               countInserts += 1
               line = re.sub('<LEM>', '<LEM><NewhidePada>', line)
               line = re.sub('</LEM>', '</hidePada></LEM>', line)
        print(line, end='')
    print("Inserted", countInserts, "<hidePada> Tags")



filename = sys.argv[1]
main(filename)


