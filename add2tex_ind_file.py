#!/usr/bin/python3
'''
Script ID: add2tex_ind_file.py
Author: Csaba Kiss
Timestamp: 1 Sep 2025

The process can be:
xelatex sdhs10_book.tex
sort_tex_index_skt.py sdhs10_book.idx > sdhs10_book_sorted.idx
mv sdhs10_book_sorted.idx sdhs10_book.idx
makeindex sdhs10_book
add2tex_ind_file.py sdhs10_book.ind > sdhs10_book_extra.ind
mv sdhs10_book_extra.ind sdhs10_book.ind
xelatex sdhs10_book.tex
xelatex sdhs10_book.tex
'''

import re
import sys

#see also items
dict = {"CHECK add2tex_ind_file.py": "CHECK"}
        #"observance": "\\\\textit{vrata}", "vrata": "observance", "mahādāna": 'donation',
        #"vehicles": "\\\\textit{vimāna}", "vimāna": "\\\\ae rial vehicles", "eating at night":
        #"\\\\textit{naktabhojana}", "naktabhojana": "eating at night", "third gender": "\\\\textit{napuṃsaka}",
        #"napuṃsaka": "third gender", "religious duties": "\\\\textit{dharma}", "dharma":"religious duties",
        #"three pure substances": "\\\\textit{triśukla}", "triśukla": "three pure substances",
        #"transmigration": "\\\\textit{saṃsāra}", "saṃsāra": "transmigration", "non-violence": "\\\\textit{ahiṃsā}",
        #"ahiṃsā": "non-violence", "non-stealing": "\\\\textit{asteya}", "asteya": "non-stealing", 'devotee': '\\\\textit{bhakta}',
        #'donation': 'gift', 'gift': 'donation', 'śivaliṅga': '\\\\textit{liṅga}', 'śivaliṅgamahāvrata': '\\\\textit{liṅgavrata}',
        #'śṛṅgodaka': 'horn-water', 'ghee': 'clarified butter', 'clarified butter': 'ghee', 'cow': 'cattle'}


filename = sys.argv[1]  
with open(filename, "r", encoding="utf-8") as openfile:
    #f = openfile.readlines()
    output = ''
    for line in openfile:
        for item in dict:
            #print(line, item)
            if '\\item' in line and ' '+item+',' in line:
                line = re.sub(item+',', item+' (see also '+dict[item]+'),', line)
                break
            elif '\\item' in line and '{'+item+'},' in line:
                line = re.sub('{'+item+'},', '{'+item+'} (see also '+dict[item]+'),', line)
                break
        output = output + line
    print(output)
