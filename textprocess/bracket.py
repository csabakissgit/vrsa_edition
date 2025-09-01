'''
Finds and alters closing brackets in TeX file for a given open bracket, e.g., after \var
Usage:
    python3 brackets.py filename.tex 'var'
'''
import re
import sys


filename = sys.argv[1]
command = sys.argv[2]
within_brackets = False
counter = 0
addch = ''

with open(filename, "r", encoding="utf-8") as openfile:
    for line in openfile:
        if '\\'+command in line or within_brackets == True:
            line = re.sub('\\\\'+command, '<'+command.upper()+'>', line)
            within_brackets = True
            newline = ''
            for ch in line:
                if ch == '{':
                    counter += 1
                    addch = ''
                elif ch == '}':
                    counter -= 1
                    addch = ch
                    if counter == 0:
                        addch = '</'+command.upper()+'>'
                        within_brackets = False
                        counter = 0
                else:
                    addch = ch
                newline = newline + addch 
            print(newline, end='')
        else:
            print(line, end='')

