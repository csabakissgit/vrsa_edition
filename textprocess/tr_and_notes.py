import re

def tr_and_notes(filename):
   chapter = 0
   vsnum = 1
   vsnum_needed = True
   twodandas_just_passed = True
   textflag = False
   trflag = False
   noteflag = False
   noanustubh = False
   note = ''
   onflag = False
   skipNextVsnum = False
   openfile = open(filename, "r")
   for line in openfile:
       if '<START/>' in line:
            onflag = True
            continue
       if '<STOP/>' in line:
            onflag = False
            continue
       if onflag == True:
        chap_and_vsnum = (str(chapter) + "." + str(vsnum)) 
        if '<NOTANUSTUBH/>' in line:
            notanustubh = True
        if '<ANUSTUBH/>' in line:
            notanustubh = False
        if '<TEXT>' in line:
            twodandas_just_passed = False
            if '||' in line:
                vsnum += 1
                vsnum_needed = True
                twodandas_just_passed = True
            elif ('|' in line or notanustubh == True) and ( vsnum_needed == True or twodandas_just_passed == True):
                if skipNextVsnum:
                    skipNextVsnum = False
                else:
                    print("\n\n" + chap_and_vsnum, end=' ')
                vsnum_needed = False
        if '<TR>' in line or '<TRCOLOPHON>' in line or trflag == True:
            trflag = True
            if '</TR>' in line or '</TRCOLOPHON>' in line:
                trflag = False
            v01 = re.sub('.*<TR>', '\n\n', line[:-1])
            v01 = re.sub('.*<TRCOLOPHON>', '\n\n-- ', v01)
            if '|F|' in line: 
                v01 = re.sub('\|F\|', '-- ' + str(chapter) + "." + str(vsnum), v01)
                skipNextVsnum = True
            v01 = re.sub('</TR>.*', ' ', v01)
            v01 = re.sub('</TRCOLOPHON>.*', ' --', v01)
            v01 = re.sub('Ł', '_', v01)
            v01 = re.sub('\$', '_', v01)
            v01 = re.sub('\^', '${\\\\uparrow}$', v01)
            # final white spaces
            v01 = v01.strip()
            print(v01)
        if '<NOTE>' in line or noteflag == True:
            noteflag = True
            if '</NOTE>' in line:
                noteflag = False
            v01 = re.sub('.*<NOTE>', '', line.strip())
            v01 = re.sub('</NOTE>.*', ' ', v01)
            v01 = re.sub('<sep/>', '\n', v01)
            v01 = re.sub('Ł', '_', v01)
            v01 = re.sub('\$', '_', v01)
            note = note + "\n    " + v01 
            if noteflag == False and twodandas_just_passed:
                v01 = re.sub('</NOTE>.*', ' ', v01)
                noteflag = False
                print("\nNOTE:\n\n    " + note)
                note = ""
                twodandas_just_passed = False
        if '<startchapter-n="' in line:
            v01 = re.sub('.*<startchapter-n="', '', line)
            v01 = re.sub('".*', '', v01)
            chapter = int(v01) 
            vsnum = 1
        if '<TRCHAPTER>' in line:
            v01 = re.sub('.*<TRCHAPTER>', '\n\n= ', line.strip())
            v01 = re.sub('</TRCHAPTER>.*', ' =', v01)
            print(v01) 
   openfile.close()

