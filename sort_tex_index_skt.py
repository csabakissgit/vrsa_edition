#!/usr/bin/python3

r"""
Script ID: sort_tex_index_skt.py
Author: Csaba Kiss
Timestamp: 22 Sep 2024

Input is a LaTeX .idx file, output is printout of the same
with words before the @ sign 'normalized' or 'Englicised' to
help sorting of Sanskrit entries according to the English ABC.
The process should be:
    1. run your doc, e.g.:
        xelatex book.tex
    2. run this script on the produced book.idx file and save it:
        python sort_tex_index_skt.py book.idx > book_sorted.idx
    3. run makeindex on the new file thus to save it in place of the old one:
        makeindex -o book.idx book_sorted.idx
    4. run your doc again (twice):
        xelatex book.tex

All original index entries should have a blahblah@ bit echoing the indexed word to be altered
(i.e., ācārya\index{ācārya@\textit{ācārya}},
i.e. define macros for yourself to always include '...@' in all index entries:
    E.g.:
    \newcommand{\myidx}[1]{#1\index{#1@#1}}
    \newcommand{\sktx}[1]{\skt{#1}\index{#1@\skt{#1}}}
    \newcommand{\mysktindex}[1]{\index{#1@\skt{#1}}}
    \newcommand{\enx}[1]{#1\index{#1@#1}}
Any other entry without an @ sign will be passed on as it is.
"""

import re
import sys

dict = {'ṃ': 'm', 'ḥ': 'h', 'ā': 'a', 'ī': 'i', 'ū': 'u', 'ṛ': 'r', 'ṅ': 'n', 'ṭ': 't', 'ḍ': 'd', 'ṇ': 'n', 'ś': 's', 'ṣ': 's', 'Ā': 'A', 'Ī': 'I', 'Ū': 'U', 'Ṛ': 'R', 'Ṅ': 'N', 'Ñ': 'N', 'Ṭ': 'T', 'Ḍ': 'D', 'Ṇ': 'N', 'Ś': 'S', 'Ṣ': 'S', '\\\\ae ': 'ae', '\\\\AE ': 'AE'}

#addSeeElsewhereLinesDict = ["vrata": "observance"]

def changesktletters2eng(lemma):
    for l in dict:
        lemma = re.sub(l, dict[l], lemma)
    return lemma

def addSeeElsewhereLines(output):
    pass


filename = sys.argv[1]  
with open(filename, "r", encoding="utf-8") as openfile:
    output = ''
    for line in openfile:
        if 'indexentry' in line and '@' in line and '!' not in line:
            # extract lemma before @
            lemma = re.sub('.*indexentry{', '', line)
            lemma = re.sub('@.*', '', lemma)
            englemma = changesktletters2eng(lemma)
            # change bit before @
            newline = re.sub('dexentry{.*@', 'dexentry{'+englemma.strip()+'@', line)
            output = output + newline
        else:
            output = output + line
        #output = addSeeElsewhereLines(output)
    print(output)
