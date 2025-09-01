import re

def change_sigla(line):
    subdict ={'\\\\msNC45': '\\\\msNCfortyfive',
              '\\\\msNC94': '\\\\msNCninetyfour',
              '\\\\msNK12':  '\\\\msNKtwelve',
              '\\\\msNK12a':  '\\\\msNKtwelvea',
              '\\\\msNK12b':  '\\\\msNKtwelveb',
              '\\\\msNKB12':  '\\\\msNKtwelveb',
              '\\\\msNK82':  '\\\\msNKeightytwo',
              '\\\\msNK28':  '\\\\msNKtwentyeight',
              '\\\\msNKo77':  '\\\\msNKoseventyseven',
              '\\\\msNKA12':  '\\\\msNKAtwelve',
              '\\\\msNKA14':  '\\\\msNKAfourteen',
              '\\\\msKA14':  '\\\\msKAfourteen',              
              '\\\\msGP43':  '\\\\msGPfortythree',
              '\\\\msTb72':  '\\\\msTbseventytwo',
              '\\\\msTAd14': '\\\\msTAdfourteen',
              '\\\\msMTr66':  '\\\\msMTrsixtysix',
              '\\\\msGP74':  '\\\\msGPseventyfour',
              '\\\\msS67':  '\\\\msSsixtyseven',
              '\\\\msDP75': '\\\\msDPseventyfive'}
    for c in subdict:
        line = re.sub(c, subdict[c], line)
    return line
