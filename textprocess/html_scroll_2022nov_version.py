# to clean up the results, open the html file in vim
# and say:
# %s/<div class=\"wrap-content.*\n*<\/div>//g


import re
#from datetime import date
#today = date.today()

from textprocess import xml_substitutions
from textprocess import line_to_dn
from textprocess import txt_output_line
from textprocess import toDevanagariExceptTagsAndCommands

def putin_text_line(line, chapter, vsnum, pada, indent, uvacaflag):
    '''
    Puts all the required html stuff into the main text
    '''
    uv = "<uvaca>" * uvacaflag
    ind = '&#160;&#160;&#160;&#160;' * indent
    return re.sub(textOpenTag, '<TEXT id="' + str(chapter) + '.' + str(vsnum+uvacaflag) + 
                   pada + '" class="sktvrs' + str(chapter) + '.' + str(vsnum+uvacaflag) + 
                   '" onclick="showApparatus(\'app' + str(chapter) + '.' + 
                   str(vsnum+ uvacaflag)  + pada + '\')" ondblclick="showNote(\'' + 
                   'note' + str(chapter) + '.' + str(vsnum+uvacaflag) + '\')" '  + 
                   '>\n<RMTEXT>' + uv + ind, line)

def dharmaTransliteration(line):
        line = re.sub("ṃ", "ṁ", line)
        line = re.sub("ṛ", "r̥", line)
        line = re.sub("ṝ", "r̥̄", line)
        line = re.sub("ḷ", "l̥", line)
        line = re.sub("Ṃ", "Ṁ", line)
        line = re.sub("Ṛ", "R̥", line)
        line = re.sub("Ṝ", "R̥̄", line)
        line = re.sub("Ḷ", "L̥", line)
        return line

def produceDnVersion(line, textflag, proseflag, chapter, vsnum):
        # stripping line within textOpenTag and textClosingTag mainly to produce the Devanāgarī version
        maintextdn = re.sub("{ }", "", line)
        maintextdn = txt_output_line.txt_output_line(maintextdn, textflag)
        maintextdn = re.sub('<MNTR>', '', maintextdn)
        maintextdn = re.sub('</MNTR>', '', maintextdn)
        maintextdn = re.sub('<mainwrap>', '', maintextdn)
        maintextdn = re.sub('</mainwrap>', '', maintextdn)
        maintextdn = re.sub('<div>', '', maintextdn)
        maintextdn = re.sub('</div>', '', maintextdn)
        maintextdn = re.sub('{-}', '', maintextdn)
        if proseflag == False:
            maintextdn = re.sub('\|\|.*', " ॥<span  class=\"vsnum\">"+ str(chapter) + ":" + str(vsnum) + "</span>", maintextdn)
        else:
            maintextdn = re.sub('\|\|', " ॥", maintextdn)
        maintextdn = re.sub('\|', " ।", maintextdn)
        # <crux> has been turned into †, now turning back to <crux>
        # </crux> has been turned into ‡, now turning back to </crux>
        maintextdn = re.sub("†", "<crux>", maintextdn)
        maintextdn = re.sub("‡", "</crux>", maintextdn)
        maintextdn = re.sub("\n", "", maintextdn)
        # producing a Devanāgarī version of the line:
        return toDevanagariExceptTagsAndCommands.main(maintextdn) 

# define your own tags
textOpenTag = '<TEXT>'
textClosingTag = '</TEXT>'
appOpenTag = '<APP>'
appClosingTag = '</APP>'
paralOpenTag = '<PARAL>'
paralClosingTag = '</PARAL>'
noteOpenTag = '<NOTE>'
noteClosingTag = '</NOTE>'
levelOpenTags = {'<TITLE>' : 'h1', '<CHAPTER>' : 'chapter', '<SUBCHAPTER>' : 'subchapter', '<SUBSUBCHAPTER>' : 'subsubchapter'}  
levelClosingTags = {'</TITLE>' : 'h1', '</CHAPTER>' : 'chapter', '</SUBCHAPTER>' : 'subchapter', '</SUBSUBCHAPTER>' : 'subsubchapter'}  

def html_scroll(filename):
    chapter = 0
    vsnum = 0
    prev_vsnum = 0
    textflag = False
    appflag = False
    paralflag = False
    lacunaflag = False
    anustubh = True
    hemistich = 0
    proseflag = False
    pvarflag = False
    # uvacaflag is 0 or 1; used to increment vsnum temporarily when reaching an uvaca line
    uvacaflag = 0
    trflag = False
    noteflag = False
    onflag = False
    firstTEXT = True
    note = ''
    collected_tr = ""
    collected_notes = ""
    # indent verse line?
    indent = 0
    lastnotenum = "0.0"
    currentnotenum = "0.0"

    # header
    print('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
       <meta http-equiv="content-type" content="text/html; charset=UTF-8">
       <title>Loading...</title>
       <rt id="realtitle">Title</rt>
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <link rel="stylesheet" href="css/style_scroll.css">
       <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
       <script src="js/jquery.min.js"></script>
       <script src="js/colorthemes.js"></script>
       <script src="js/showhide.js"></script>
       <script src="js/onlytext.js"></script>
    </head>
       <body onload="closeapp();">
          <div class="text" id="sanskrittext">
          <br/>
        ''')

    #[Version of ' + str(today) + ']
    # color selector
    print('''<select id="themes"  style="background-color:#fff7e6">
              <option value="default">Choose Colour Theme</option>
              <option value="contrast">Contrasted</option>
              <option value="light">Light</option>
              <option value="gray">Gray</option>
             </select>
           <script>
           $("select").change(function() {
                    if ($(this).val() === "contrast") {
                        doContrastedColorTheme();
                        }
                    if ($(this).val() === "gray") {
                        doGrayColorTheme();
                        }
                    if ($(this).val() === "light") {
                        doLightColorTheme();
                        }
                    })
                    </script>
                    ''')
    # instructions box
    print('''<div class="header">
        &nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;
    <div class="wrap-main">
     <span class="instr" onclick="showApparatus(\'instructions\')">
        Help
     </span>
     <div class="wrap-content" onclick="hideFunction(\'instructions\')" id="instructions">
     <span class="instr"> 
        • Press keys \'s\', \'t\' and \'n\' to toggle the Sanskrit text, the translation and the notes, respectively; 
        press \'a\' to open all four windows; press \'o\' to open/close all apparatus entries;
        press \'d\' to toggle Roman/Devanāgarī
     </span>
     <span class="instr">
         • You can also use these buttons for the same:
     </span> 
     <span class="instr"> 
          &nbsp;&nbsp;&nbsp;&nbsp; 
          <button onclick="showonlytext()" id="showonlytext">Only Skt</button>
     </span>
     <span class="instr"> 
          &nbsp;&nbsp;&nbsp;&nbsp; 
          <button onclick="showtextandtranslation()" id="showtextandtranslation">Skt & Tr</button>
     </span> 
     <span class="instr"> 
          &nbsp;&nbsp;&nbsp;&nbsp; 
          <button onclick="showtexttrnotes()" id="txttrnotes">Skt & Tr & Notes</button>
     </span> 
     <span class="instr"> 
          &nbsp;&nbsp;&nbsp;&nbsp; 
          <button onclick="showall()" id="all">All</button>
     </span> 
     <span class="instr"> 
          &nbsp;&nbsp;&nbsp;&nbsp; 
          <button onclick="openallapp()" id="openallapp">Open all apparatus entries</button>
     </span> 
     <span class="instr">  
          &nbsp;&nbsp;&nbsp;&nbsp; 
          <button onclick="turnItDevnag()" id="switchbutton">Switch to Devanāgarī</button>
     </span> 
     <span class="instr"> 
          • Click inside this box to close it
     </span>
     <span class="instr"> 
          • Single click on Sanskrit line to display apparatus 
          and highlight translation of verse (if translation is visible)
     </span>
     <span class="instr"> 
          • Click inside apparatus box to close it
     </span>
     <span class="instr"> 
          • Double click on Sanskrit line to scroll to relevant note, if any and if notes are displayed
     </span>
     <span class="instr"> 
          • Click on translation to toggle highlighting on relevant Sanskrit verse
     </span>
     <span class="instr"> 
          • If your browser has problems rendering the Devanāgarī font, 
          change your browser\'s default font (e.g. to \'Noto Sans Devanagari\' on Ubuntu) 
     </span>
     </div>
     </div>
     </div>
     <br/>
     ''')


    openfile = open(filename, "r")
    for line in openfile:
        #line = dharmaTransliteration(line)
        line = re.sub("^\**", "", line)
        if '<START/>' in line:
            onflag = True
            continue
        if '<STOP/>' in line:
            onflag = False
            continue
        if onflag == True:
            if '<NOTANUSTUBH/>' in line:
                anustubh = False 
                proseflag = False
                hemistich = 0
                continue
            if '<ANUSTUBH/>' in line:
                anustubh = True
                proseflag = False
                continue
            if '<PROSE>' in line:
                proseflag = True
                anustubh = False
                continue
            if '</PROSE>' in line:
                proseflag = False
                anustubh = False
                continue
            if '<SETVSNUM' in line:
                outputline = re.sub('.*<SETVSNUM="', '', line)
                outputline = re.sub('".*', '', outputline)
                vsnum = int(outputline) - 1
                continue
            if '<startchapter-n="' in line:
                outputline = re.sub('.*<startchapter-n="', '', line)
                outputline = re.sub('".*', '', outputline)
                chapter = int(outputline) 
                vsnum = 0
                if firstTEXT == False:
                   print('\n</div>\n</div>\n<br/><br/><br/><!-- NEWCHAPTER -->')
                else:
                   print('<!-- NEWCHAPTER -->')
                firstTEXT = True
                continue

            if textOpenTag in line:
                 if firstTEXT == False:
                     # close div and start new wrap for verse + apparatus
                     line = re.sub(textOpenTag, '\n</div>\n</div>\n\n<mainwrap>\n<TEXT>', line)
                 else:
                     line = re.sub(textOpenTag, '\n<mainwrap>\n<TEXT>', line) 
                     firstTEXT = False
            # if it is the main text:        
            if textOpenTag in line or textflag == True:
                textflag = True
                # deleting TeX-style \- (`can break line here')
                line = re.sub('\\\\-', '', line)

                # make a Devanāgarī version of the line
                maintextdn = produceDnVersion(line, textflag, proseflag, chapter, vsnum)

                uvacaflag = 0
                if textClosingTag in line:
                    textflag = False
                # check if this is the end of a verse
                if '||' in line and proseflag == False:
                    chap_and_vsnum = ("<span class=\"vsnum\">" + str(chapter) + "." + str(vsnum) + "</span>||") 
                    # We need a little extra vertical space between verses (amount controlled in the css file)
                    vspace = "<spaceaftersloka/>"
                else:
                    chap_and_vsnum = "" 
                    vspace = ""
                if '||' in line and anustubh == True and hemistich == 1 and proseflag == False:
                    outputline = re.sub('\|\|', ' ||' + chap_and_vsnum, line)
                    # main process to put in stuff
                    pada = "cd"
                    indent = 0
                    outputline = putin_text_line(outputline, chapter, vsnum, pada, indent, uvacaflag)
                    hemistich = 0
                elif '||' in line and anustubh == False and proseflag == False:
                    outputline = re.sub('\|\|', ' ||' + chap_and_vsnum, line)
                    outputline = "\n" + outputline + "\n" 
                    # main process to put in stuff
                    pada = "d"
                    indent = 1
                    outputline = putin_text_line(outputline, chapter, vsnum, pada, indent, uvacaflag)
                    hemistich = 0
                # special danda: it does not increase verse number, e.g. after devy uvāca
                elif '|*' in line:
                    # main process to put in stuff
                    uvacaflag = 1
                    pada = "uvaca"
                    indent = 0
                    outputline = re.sub('\|\*', ' | ', line)
                    outputline = putin_text_line(outputline, chapter, vsnum, pada, indent, uvacaflag)
                    outputline = re.sub(textClosingTag, '</uvaca></TEXT>', outputline)
                    hemistich = 0
                # with anuṣṭubh, a danda increases verse number if it is the first single danda
                elif '|' in line and hemistich == 0 and anustubh == True and proseflag == False:
                    vsnum += 1
                    # main process to put in stuff
                    uvacaflag = 0
                    pada = "ab"
                    indent = 0
                    outputline = putin_text_line(line, chapter, vsnum, pada, indent, uvacaflag)
                    outputline = re.sub('\|', ' |', outputline)
                    # the next single danda is not a first single danda
                    hemistich = 1 
                # check if this is a non-anuṣṭubh first line
                elif '|' not in line and hemistich == 0 and anustubh == False:
                    # no indent
                    vsnum += 1
                    # main process to put in stuff
                    uvacaflag = 0
                    pada = "a"
                    indent = 0
                    outputline = putin_text_line(line, chapter, vsnum, pada, indent, uvacaflag)
                    hemistich = 1
                # check if this is a non-anuṣṭubh third line
                elif '|' not in line and hemistich == 2 and anustubh == False:
                    # no indent
                    # main process to put in stuff
                    uvacaflag = 0
                    pada = "c"
                    indent = 0
                    outputline = putin_text_line(line, chapter, vsnum, pada, indent, uvacaflag)
                    hemistich = hemistich + 1
                # if this is a first single danda but it is not anuṣṭubh, don't increase verse number; it's pāda b
                elif '|' in line and anustubh == False and proseflag == False:
                    outputline = "\n" + line
                    # main process to put in stuff
                    uvacaflag = 0
                    pada = "b"
                    indent = 1
                    outputline = putin_text_line(line, chapter, vsnum, pada, indent, uvacaflag)
                    outputline = re.sub('\|', ' |', outputline)
                    hemistich = hemistich + 1 
                # if it's a three-line anuṣṭubh, two ||s mean pāda ef
                elif '||' in line and hemistich == 2 and anustubh == True:
                    outputline = re.sub('\|\|', ' ||' + chap_and_vsnum, line)
                    # main process to put in stuff
                    uvacaflag = 0
                    pada = "ef"
                    indent = 0
                    outputline = putin_text_line(outputline, chapter, vsnum, pada, indent, uvacaflag)
                    hemistich = 0 
                # if it's a three-line anuṣṭubh, one | means pāda cd when it's hemistich 1
                elif '|' in line and hemistich == 1 and anustubh == True:
                    # main process to put in stuff
                    uvacaflag = 0
                    pada = "cd"
                    indent = 0
                    outputline = putin_text_line(line, chapter, vsnum, pada, indent, uvacaflag)
                    outputline = re.sub('\|', ' |', outputline)
                    hemistich = 2 
                else:
                    outputline = line 
                outputline = re.sub('{-}', "-", outputline)
                outputline = re.sub('{ }', " ", outputline)
                if '<COLOPHON>' in outputline:
                    pada = 'colophon'
                    outputline = re.sub('<COLOPHON>', "\n<colophon>|| ", 
                                putin_text_line(outputline, chapter, vsnum, pada, indent, uvacaflag))
                    outputline = re.sub('</COLOPHON>', " ||</colophon>", outputline)                   
                # b and d lines non-anuṣṭubh verses with indentation
                if '&#160;&#160;&#160;&#160' in outputline: 
                    outputline = re.sub(textClosingTag + '.*', 
                                '</RMTEXT>\n<DNTEXT>&#160;&#160;&#160;&#160;' + maintextdn + 
                                ' </DNTEXT></TEXT>\n<apparatuswrap>', outputline)
                else:
                    outputline = re.sub(textClosingTag + '.*', '</RMTEXT>\n<DNTEXT>' + uvacaflag * '<uvaca>' +  
                            maintextdn + uvacaflag * ' </uvaca>' + ' </DNTEXT></TEXT>\n<apparatuswrap>', outputline)
                if '</COLOPHON>' in line:
                    outputline = re.sub('</DNTEXT>', " ॥</DNTEXT>", outputline)
                outputline = re.sub('Ó', "oṃ", outputline)
                #outputline = re.sub('<uvaca>', '', outputline)
                #outputline = re.sub('</uvaca>', '', outputline)
                outputline = re.sub('<ja>', ' ', outputline)
                outputline = re.sub('</ja>', ' ', outputline)
                #outputline = re.sub('<crux>', '†', outputline)
                #outputline = re.sub('</crux>', '†', outputline)
                outputline = re.sub('\\\\-', '', outputline)
                outputline = re.sub('<mainwrap>', '<div class="wrap-main">', outputline)
                outputline = re.sub('</mainwrap>', '</div>', outputline)
                outputline = re.sub('<apparatuswrap>', vspace + '\n\n<div class="wrap-content" onclick="hideFunction(\'app' + str(chapter) + '.' + str(vsnum+uvacaflag) + pada + '\')" id="app' + str(chapter) + '.' + str(vsnum+uvacaflag) + pada + '">', outputline)
                outputline = re.sub('</apparatuswrap>', '</div>', outputline)
                # prose
                if proseflag == True:
                    outputline = re.sub(textOpenTag, '<TEXTPROSE>\n<RMTEXT>', outputline)
                    outputline = re.sub(textClosingTag, '</TEXTPROSE>', outputline)
                print(outputline)

            # dealing with the apparatus
            if appOpenTag in line or appflag == True:
                appflag = True
                if appClosingTag in line:
                    appflag = False
                outputline = re.sub('{ }', " ", line)
                # matching the search pattern itself
                outputline = re.sub('(?P<group>\\\\v[a-z]*)', '<VSNUMPADA>\\1</VSNUMPADA>', outputline)  
                outputline = re.sub('\\\\vo', str(vsnum+uvacaflag), outputline)
                outputline = re.sub('\\\\v', str(vsnum+uvacaflag), outputline)
                outputline = re.sub(appOpenTag, '', outputline)
                outputline = re.sub(appClosingTag, '<br/>', outputline)
                outputline = re.sub('\\\\csa ', 'ā', outputline)
                outputline = re.sub('\\\\csi ', 'i', outputline)
                outputline = xml_substitutions.xml_substitutions(outputline)

                dnOutputLine = re.sub('{ }', "", line)
                dnOutputLine = re.sub('</LEM>', ' </LEM>', dnOutputLine)
                dnOutputLine = re.sub('\\\\-', '', dnOutputLine)                
                dnOutputLine = toDevanagariExceptTagsAndCommands.main(re.sub('{ }', "", dnOutputLine))
                # matching the search pattern itself
                dnOutputLine = re.sub('(?P<group>\\\\v[a-z]*)', '<VSNUMPADA>\\1:</VSNUMPADA>', dnOutputLine)
                dnOutputLine = re.sub('\\\\vo', str(vsnum+uvacaflag), dnOutputLine)
                dnOutputLine = re.sub('\\\\v', toDevanagariExceptTagsAndCommands.main(str(vsnum+uvacaflag)), dnOutputLine)
                dnOutputLine = re.sub(appOpenTag, '', dnOutputLine)
                dnOutputLine = re.sub(appClosingTag, '<br/>', dnOutputLine)
                dnOutputLine = xml_substitutions.xml_substitutions(dnOutputLine)

                print('<RMAPP>' + outputline + '</RMAPP>' + '<DNAPP>' + dnOutputLine + '</DNAPP>')

            if paralOpenTag in line or paralflag == True:
                paralflag = True
                if paralClosingTag in line:
                    paralflag = False
                outputline = re.sub('{ }', " ", line)
                outputline = re.sub(' *\\\\vo', str(vsnum+uvacaflag), outputline)
                outputline = re.sub(paralOpenTag + ' *\\\\v', "<PARAL>" + str(vsnum+uvacaflag), outputline)
                outputline = xml_substitutions.xml_substitutions(outputline)
                if paralOpenTag in line:
                    print('<hr width="50%" size="1" align="left" color="#cc8800"/>')
                print(outputline)
            if '<LACUNA>' in line or lacunaflag == True:
                lacunaflag = True
                if '</LACUNA>' in line:
                    lacunaflag = False
                outputline = re.sub('{ }', " ", line)
                outputline = re.sub('<LACUNA> *\\\\vo', "<LACUNA>" + str(vsnum+uvacaflag), outputline)
                outputline = re.sub('<LACUNA> *\\\\v', "<LACUNA>" + str(vsnum+uvacaflag), outputline)
                outputline = xml_substitutions.xml_substitutions(outputline)
                if '<LACUNA>' in line:
                    print('<hr width="50%" size="1" align="left" color="#cc8800"/>')
                print(outputline)
            '''
            if '<PVAR>' in line or pvarflag == True:
                pvarflag = True
                if '</PVAR>' in line:
                    pvarflag = False
                outputline = re.sub('{ }', " ", line)
                outputline = re.sub('<PVAR>\\\\vo', "<PVAR>", outputline)
                outputline = re.sub('<PVAR>\\\\v', "<PVAR>", outputline)
                outputline = xml_substitutions.xml_substitutions(outputline)
                print(outputline)
            '''    
            if '<TRCHAPTER>' in line:
                trflag = True
                outputline = re.sub('<!-- <TRCHAPTER>', '<br/><br/><br/><trnslchapter>', line)
                outputline = re.sub('</TRCHAPTER> -->', '</trnslchapter>', outputline)
                outputline = xml_substitutions.xml_substitutions(outputline)
                if '</TRCHAPTER>' in line:
                    trflag = False
                    collected_tr = collected_tr  + outputline
                else:
                    collected_tr = collected_tr + outputline

            if '<TRSUBCHAPTER>' in line:
                trflag = True
                outputline = re.sub('<TRSUBCHAPTER>', '<br/><br/><trnslsubchapter>', line)
                outputline = re.sub('</TRSUBCHAPTER>', '</trnslsubchapter>', outputline)
                outputline = xml_substitutions.xml_substitutions(outputline)
                if '</TRSUBCHAPTER>' in line:
                    trflag = False
                    collected_tr = collected_tr  + outputline
                else:
                    collected_tr = collected_tr + outputline

            if '<TRSUBSUBCHAPTER>' in line:
                trflag = True
                outputline = re.sub('<TRSUBSUBCHAPTER>', '<br/><br/><trnslsubsubchapter>', line)
                outputline = re.sub('</TRSUBSUBCHAPTER>', '</trnslsubsubchapter>', outputline)
                outputline = xml_substitutions.xml_substitutions(outputline)
                if '</TRSUBSUBCHAPTER>' in line:
                    trflag = False
                    collected_tr = collected_tr  + outputline
                else:
                    collected_tr = collected_tr + outputline


            if '<TRCOLOPHON>' in line:
                trflag = True
                outputline = re.sub('<TRCOLOPHON>', '<br/><br/><trnslcolophon id="tr' + str(chapter) + '.' + str(vsnum) + 'colophon">', line)
                outputline = re.sub('</TRCOLOPHON>', '</trnslcolophon>', outputline)
                outputline = xml_substitutions.xml_substitutions(outputline)
                if '</TRCOLOPHON>' in line:
                    trflag = False
                    collected_tr = collected_tr  + outputline + "<br/><br/><br/><br/>"
                else:
                    collected_tr = collected_tr + outputline
                    


            # Dealing with the translation, actually just collecting it
            if '<TR>' in line or trflag == True:
                trflag = True
                # &#39 is a single quote, needed because of a bug...?
                strng = "sktvrs" + str(chapter) +  "." + str(vsnum+uvacaflag)
                outputline = re.sub("<?!?-?-? ?<TR>", "\n<trnsl class=\"trnsl" + str(chapter) +  '.' + str(vsnum+uvacaflag) + '" ' + "onclick=\"showSkt(&#39" + strng + "&#39)\">", line)
                outputline = re.sub('</TR> ?-?-?>?.*', '</trnsl>', outputline)
                if '<TR>' in line and (prev_vsnum != vsnum and uvacaflag != 1):
                    collected_tr = collected_tr + "\n<br/><br/>\n" + '<span class="vsnum" id="tr' + str(chapter) + '.' + str(vsnum) + '">' + "|" + str(chapter) + "." + str(vsnum) + "| </span>"
                if '<TR>' in line and uvacaflag == 1:
                    collected_tr = collected_tr + "<br/><br/>"
                if '</TR>' in line:
                    prev_vsnum = vsnum
                    trflag = False
                    collected_tr = collected_tr  + outputline
                    # handling the sign |F| meaning 'and the following verse'; output e.g. --|1.8| after |1.7|
                    collected_tr = re.sub('\|F\|', '-- |' + '<span class=\"vsnum\">' + str(chapter) + "." + str(vsnum+1) + "</span>" + "| ", collected_tr)
                    collected_tr = xml_substitutions.xml_substitutions(collected_tr)
                    collected_tr = re.sub("`", "‘", collected_tr)
                    collected_tr = re.sub("'", "’", collected_tr)
                else:
                    collected_tr = collected_tr + outputline
                    
                    

            # Dealing with notes, actually just collecting them
            if noteOpenTag in line or noteflag == True:
                currentnotenum = str(chapter) + "." + str(vsnum)
                noteflag = True
                outputline = xml_substitutions.xml_substitutions(line)
                outputline = re.sub("`", "‘", outputline)
                outputline = re.sub("'", "’", outputline)
                if noteOpenTag in line and lastnotenum != currentnotenum:
                    collected_notes = collected_notes + "<br/><br/>" + "|" + '<vsnum id="note' + str(chapter) + "." + str(vsnum) + '">' + str(chapter) + "." + str(vsnum) + "</vsnum>" + "| "
                    lastnotenum = currentnotenum
                if noteClosingTag in line:
                    noteflag = False
                    collected_notes = collected_notes  + outputline
                else:
                    collected_notes = collected_notes + outputline



            # Dealing with headers
            if '<SUBSUBCHAPTER>' in line or '<SUBCHAPTER>' in line or '<CHAPTER>' in line or '<TITLE>' in line:
                # checking <CHAPTER> etc. levels in line
                level = ''
                for l in levelOpenTags:
                    if l in line:
                        level = levelOpenTags[l]
                # the spaces also make sure that final consonants will
                # will come out properly in Devanagari
                outputline = re.sub('<.?TITLE>', " ", line)
                outputline = re.sub('<.?TITLE>', " ", line)
                outputline = re.sub('<CHAPTER>', "[ ", outputline)
                outputline = re.sub('</CHAPTER>', " ]", outputline)                
                outputline = re.sub('<SUBCHAPTER>', "[ ", outputline)
                outputline = re.sub('</SUBCHAPTER>', " ]", outputline)
                outputline = re.sub('<SUBSUBCHAPTER>', "[ ", outputline)
                outputline = re.sub('</SUBSUBCHAPTER>', " ]", outputline)
                # turn it into Devanāgarī
                textdn = toDevanagariExceptTagsAndCommands.main(re.sub('{ }', '', outputline.lower())) 
                outputline = re.sub('{ }', " ", outputline)
                if firstTEXT == False:
                   print('\n</div>\n</div>')
                print("<RMTEXT>" + "<" + level + ">\n" + outputline +
                        "</" + level + "></RMTEXT>\n<DNTEXT><" +
                        level + ">\n" + textdn + "</" + level +"></DNTEXT>")
                firstTEXT = True


    # close Sanskrit text box
    print("</div></div><br/><br/><br/><br/></div>\n")   
    



         
    # print translation box
    print('''<div class="translation" id="translation">
             <br/>
             <select id="trthemes" style="background-color:#fff7e6">
               <option value="default">Choose Colour Theme</option>
               <option value="contrast">Contrasted</option>
               <option value="light">Light</option>
               <option value="gray">Gray</option>
             </select>
             <script>
                $("#trthemes").change(function() {
                    trtexts = document.getElementsByTagName("trnsl");
                    if ($(this).val() === "contrast") { 
                         $(".translation").css("background-color", "black");
                         for (t = 0; t < trtexts.length; t++) { 
                             trtexts[t].style.color =  "white";
                             }
                     }
                    if ($(this).val() === "light") {
                         $(".translation").css("background-color", "white");
                         for (t = 0; t < trtexts.length; t++) {
                            trtexts[t].style.color =  "black";
                           } 
                       }       
                    if ($(this).val() === "gray") {
                       $(".translation").css("background-color", "black");
                       for (t = 0; t < trtexts.length; t++) { 
                            trtexts[t].style.color =  "gray";
                         } 
                      }
                    });
             </script>
            <br/><br/><br/><br/>
            <h2>Translation</h2>
            ''')
    print(collected_tr)
    print("\n<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/></div>\n") 
    
           
    # print notes box
    print('<div class="notes" id="notes">\n<h2>Notes</h2>\n')
    print(collected_notes)
    print("\n<br/>\n<br/></div>\n")        
    
    
    # print mss box
    print('<div class="msimage" id="mssimages">\n<h2>Sources</h2>\n')
    #open_mssdata_file = open("/home/csaba/indology/dharma_project/vrsa_edition/vss_mss_data.html", "r")
    #for l in open_mssdata_file:
    #    print(l[:-1], end=" ")        
    print("\n<br/>\n</div>\n</body></html>")        
    #openfile.close()

