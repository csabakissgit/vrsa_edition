"""
Checks apparatus in a .cred file.
Usage:
    textprocess.py -appcheck filename 'msA, msB, msC' [last line num to check OR 0] [nomssall]
Don't add notes or anything else than one single siglum in the file in a lacuna_start: or lacuna_end: line
and add sigla without a backslash
Checks section between <START/> and <STOP/>')
TODO: when there is an emendation, order is not checked properly
NEW: you can add a line in the source file to automatize:
%appcheck: msA, msB, msC
"""

import re
import sys
import subprocess

def gocheckIfFullPada(app2check, lineNum):
    # CHECK is lemma contains a full pāda, so maybe it should be hidden
    vowels = ['ai', 'au', 'a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'e', 'o']
    app2checkLEM = re.sub('.*<LEM>', '', app2check)
    app2checkLEM = re.sub('</LEM>.*', '', app2checkLEM)
    for vowel in vowels:
        app2checkLEM = re.sub(vowel, '×', app2checkLEM)
    if app2checkLEM.count('×') > 7 and '<LEM!>' not in app2checkLEM:
        print('\033[34mWarning: full pāda in line', lineNum, '?\033[0m')
        print(app2check)


def gocheck_mssALL(app2check, mss2check, lineNum, problem):
    # check if no more than 2 variants/mss are in the rejected variants section
    # and mssALL is still missing
    app2check1stHalf = re.sub(';.*', '', app2check)
    app2check2ndHalf = re.sub('.*;', '', app2check)
    app2check2ndHalf = re.sub('acorr', '', app2check2ndHalf)
    app2check2ndHalf = re.sub('pcorr', '', app2check2ndHalf)
    app2check2ndHalf = re.sub('ac', '', app2check2ndHalf)
    app2check2ndHalf = re.sub('pc', '', app2check2ndHalf)
    rejectedVariants = 0
    for ms in mss2check:
        if ms in app2check2ndHalf:
            rejectedVariants = rejectedVariants + app2check2ndHalf.count(ms)
    if rejectedVariants < 3 and 'mssALL' not in app2check1stHalf:
        print("\033[31mmssALL missing in line\033[0m", lineNum, app2check)
        problem += 1
    elif rejectedVariants > 2 and 'mssALL' in app2check1stHalf:
        print("\033[31mmssALL not needed in line\033[0m", lineNum, app2check)
        problem += 1
    return problem


def gocheckorder(app2check, mss2check, lineNum, problem, lineNums):
    '''
    Check order of sigla:
    1) within sequences of sigla after each variant
    2) the first siglum in each sequence
    '''
    # clean up one entry in apparatus
    app2check = re.sub('acorr', '', app2check)
    app2check = re.sub('pcorr', '', app2check)
    app2check = re.sub('ac', '', app2check)
    app2check = re.sub('pc', '', app2check)
    app2check = re.sub('<.?hideNepMss>', '', app2check)
    app2check = re.sub('<.?hideSouthMss>', '', app2check)
    app2check = re.sub('<.?hideSouthMss>', '', app2check)
    app2check = re.sub('msCamsCbmsCc', 'msCa\\\\msCb\\\\msCc', app2check)
    tempapp2check = re.sub('.*</LEM>', '', app2check)
    tempapp2check = re.sub('</APP>', '', app2check)
    tempapp2check = re.sub(';', ',', tempapp2check)
    # make list of mss sequences
    sequences = tempapp2check.split(',')
    # this will contain the first siglum in each sequence
    varseq_1st_mss = []
    for seq in sequences:
        # individual ms in sequence
        mssinseq = seq.split('\\') 
        # go through the sigla of this sequence and the first that is in our list of mss
        # is saved in a list of first sigla in each sequence
        for m in mssinseq:
            if m in mss2check:
                varseq_1st_mss.append(m)
                break
        for i in range(len(mssinseq)-1):
            # check only if these are indeed sigla
            if mssinseq[i] in mss2check and mssinseq[i+1] in mss2check:
                # 1) checking if order is right
                if mss2check.index(mssinseq[i]) >  mss2check.index(mssinseq[i+1]):
                    print('\033[31mError in order around line\033[0m', lineNum, app2check)
                    problem += 1
                    lineNums.append(lineNum)
    # 2) first ms in each sequence: they should also be in order, i.e. the sequences after the lemma and its mss
    # start at the second element because we ignore the mss that contain the lemma
    for i in range(1, len(varseq_1st_mss)-1):
        # check only if these are indeed sigla to be checked
        if varseq_1st_mss[i] in mss2check and varseq_1st_mss[i+1] in mss2check:
            if mss2check.index(varseq_1st_mss[i]) > mss2check.index(varseq_1st_mss[i+1]):
                print('\033[31mError in order of mss groups around line\033[0m', varseq_1st_mss[i], varseq_1st_mss[i+1], lineNum, app2check)
                problem += 1
                lineNums.append(lineNum)
    varseq_1st_mss = []
    return problem


def gocheckpadas(app2check, padas, lineNum, problem, anustubhflag):
    if '\\v' in app2check: #this is not perfect
        for pada in padas:
            if pada in app2check:
                return problem
        print('\033[31mThere is some problem with the pāda signs in line\033[0m', lineNum, padas, anustubhflag, app2check)
        return problem+1
    return problem


def openineditor(filename, lineNums):
    for l in lineNums:
        print('\nOpen file in VIM? (y/n)')
        answer = input()
        if answer == 'y':
            print(l)
            command = ["vim" , filename, "+" + str(l)]
            subprocess.call(command)
        else:
            return


def checkAcorrPcorr(app2check, mss2check, lineNum):
    corrProblem = 0
    for ms in mss2check:
        if (ms + 'acorr' in app2check and ms + 'pcorr' not in app2check) or (ms + 'pcorr' in app2check and ms + 'acorr' not in app2check):
               print("PROBLEM in line", str(lineNum) + ", " + ms + "acorr or pcorr is missing:")
               print(app2check)
               corrProblem += 1
    return corrProblem
    


def app_check(filename):
    print('Usage:\n  textprocess.py -appcheck filename \'msA, msB, msC\' [last line num to check OR 0] [nomssall]\n\nDon\'t add notes or anything else than one single siglum in the file in a lacuna_start: or lacuna_end: line\nand add sigla without a backslash\n\nChecks section between <START/> and <STOP/>')
    appflag = False
    onflag = False
    anustubhflag = True
    padas = ['']
    textflag = False
    lacunae = ''
    last_line = 0
    if len(sys.argv) > 3:
        mss2check = re.sub(" ", "", sys.argv[3]).split(',') 
    else:
        mss2check = []
    if len(sys.argv) > 4:
        last_line = int(sys.argv[4])
    check_mssALL = True
    if len(sys.argv) > 5 and (sys.argv[4] == 'nomssall' or sys.argv[5] == 'nomssall'):
        check_mssALL = False
    app2check = ""
    openfile = open(filename, "r")
    tempfl = ""
    for line in openfile:
        line = re.sub('\\\\oo', '</APP>\nEXTRALINE<APP>', line)
        # when I put variants of both pādas in one <APP></APP>:
        if appflag == True and '<APP>' not in line:
            line = re.sub('\\\\v', '</APP>\nEXTRALINE<APP>', line)
        # to restore siglum of group to sigla of mss:
        line = re.sub('mssCaCbCc', 'msCamsCbmsCc', line)
        tempfl = tempfl + line
    problem = 0
    lineNum = 0
    lineNums = []
    for line in tempfl.split("\n"):
        lineNum += 1
        #print(line, lineNum)
        if '%appcheck: ' in line:
            mss2check = re.sub('%appcheck: ', '', line)
            mss2check = re.sub(' ', '', mss2check).split(',')
        if '%lacuna_start:' in line:
            line = re.sub('%lacuna_start:', '', line)
            lacunae = lacunae + line.strip() 
        if '%lacuna_end:' in line:
            line = re.sub('%lacuna_end:', '', line)
            lacunae = re.sub(line.strip(), '', lacunae)  
        if 'EXTRALINE' in line:
            line = re.sub('EXTRALINE', '', line)
            lineNum -= 1
        if '<START/>' in line:
            onflag = True
        if '<STOP/>' in line:
            onflag = False
            continue
        if '<ANUSTUBH/>' in line:
            anustubhflag = True
            padas = ['']
        if '<NOTANUSTUBH/>' in line:
            anustubhflag = False
            padas = ['']
        if '<TEXT>' in line:
            textflag == True

            if anustubhflag == True:
                if '|*' in line:
                        padas = ['\\vo']
                elif '||' in line:
                        if padas == ['\\va', '\\vb', '\\vab', '\\vo']:
                             padas = ['\\vc', '\\vd', '\\vcd', '\\vo', 'ENDOFVERSE']
                        elif padas == ['\\vc', '\\vd', '\\vcd', '\\vo']:
                             padas = ['\\ve', '\\vf', '\\vef', '\\vo', 'ENDOFVERSE']
                elif '|' in line:
                        if padas == ['']:
                             padas = ['\\va', '\\vb', '\\vab', '\\vo']
                        elif padas == ['\\vo']:
                             padas = ['\\va', '\\vb', '\\vab', '\\vo']
                        elif padas == ['\\va', '\\vb', '\\vab', '\\vo']:
                             padas = ['\\vc', '\\vd', '\\vcd', '\\vo']
                        elif padas == ['\\vc', '\\vd', '\\vcd', '\\vo']:
                             padas = ['\\ve', '\\vf', '\\vef', '\\vo']
                        elif padas == ['\\vc', '\\vd', '\\vcd', '\\vo', 'ENDOFVERSE']:
                             padas = ['\\va', '\\vb', '\\vab', '\\vo']
                        elif padas == ['\\ve', '\\vf', '\\vef', '\\vo', 'ENDOFVERSE']:
                             padas = ['\\va', '\\vb', '\\vab', '\\vo']
            elif anustubhflag == False:
                if '|*' in line:
                    padas = ['\\vo']
                elif '||' in line:
                    if padas == ['\\vc']:
                        padas = ['\\vd', 'ENDOFVERSE']
                    elif padas == ['\\ve']:
                        padas = ['\\vf', 'ENDOFVERSE']
                elif '|' in line:
                    if padas == ['\\va']:
                        padas = ['\\vb']
                    elif padas == ['\\vc']:
                        padas = ['\\vd']
                elif '|' not in line:
                    if padas == ['\\vb']:
                        padas = ['\\vc']
                    elif padas == ['\\vd']:
                        padas = ['\\ve']
                    else:
                        padas = ['\\va']

        if onflag == True and ('<APP>' in line or appflag == True):
            appflag = True
            app2check = app2check + line
            if '</APP>' in line:
                appflag = False
                # checking ;s
                semicolons = app2check.count(';')
                if semicolons != 1:
                    print('\033[31mThere are', semicolons, ';s in line\033[0m', lineNum, app2check)
                    problem += 1
                    lineNums.append(lineNum)
                for ms in mss2check:
                        if ms not in app2check and ms not in lacunae:
                            check = False
                            print("\033[31mPROBLEM in line", str(lineNum) + ", " + ms, "is missing:\033[0m")
                            print(app2check)
                            problem += 1
                            lineNums.append(lineNum)
                        # checking if a siglum appears twice or more times by mistake
                        if app2check.count(ms) > 1 and (ms+'acorr' not in app2check and ms+'ac' not in app2check):
                            print("\033[31mPROBLEM in line", str(lineNum) + ", " + ms, 'occurs more than once:\033[0m')
                            print(app2check)
                            problem += 1
                            lineNums.append(lineNum)
                        problem = problem + checkAcorrPcorr(app2check, mss2check, lineNum)
                # new module to check order of sigla
                problem = gocheckorder(app2check, mss2check, lineNum, problem, lineNums)
                problem = gocheckpadas(app2check, padas, lineNum, problem, anustubhflag)
                if check_mssALL:
                    problem = gocheck_mssALL(app2check, mss2check, lineNum, problem)
                gocheckIfFullPada(app2check, lineNum)
                app2check = ''
        # if user gave number for last line to check
        if lineNum == last_line:
            break

    num_of_mss2check = len(mss2check)
    print("\nWe have been checking the presence of", num_of_mss2check, "witness(es):\n  ", mss2check)
    print("And also the integrity of the apparatus...\n")
    if problem == 0:
        print("\033[32mThere were no problems. CONGRATULATIONS! \n\033[0m")
    elif problem == 1:
        print("\033[31mThere was only one problem.\n\033[0m")
        openineditor(filename, lineNums)
    else:
        print("\033[31mThere were", problem, "problems.\n\033[0m")
        openineditor(filename, lineNums)
