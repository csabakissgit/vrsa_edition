"""
Input is an edition of, e.g., Sanskrit text in Shivadharma/CsabaScript style
(see: http://einzig.hu/modest_proposal.pdf ).  Output is text to be piped
into file.html. In a browser, with the necessary css and
Javascript files, displays and edition.

To clean up the results, open the html file in vim
    and say:
%s/<div class=\"wrap-content.*\n*<\/div>//g
"""


import re

# from datetime import date
# today = date.today()

from textprocess import xml_substitutions
# from textprocess import line_to_dn
from textprocess import txt_output_line
from textprocess import toDevanagariExceptTagsAndCommands
from textprocess import drag


def putin_text_line(line, chapter, vsnum, pada, indent, uvacaflag):
    """
    Puts all the required html stuff into the main text
    """
    uvaca_or_not = "<uvaca>" * uvacaflag
    ind = "&#160;&#160;&#160;&#160;" * indent
    return re.sub(
        TEXT_OPEN_TAG,
        '<TEXT id="'
        + str(chapter)
        + "."
        + str(vsnum + uvacaflag)
        + pada
        + '" class="sktvrs'
        + str(chapter)
        + "."
        + str(vsnum + uvacaflag)
        + '"'
        +
        #'" ondblclick="showApparatus(\'app' + str(chapter) + '.' +
        #                   str(vsnum+ uvacaflag)  + pada + '\'); showNote(\'' +
        #                  'note' + str(chapter) + '.' + str(vsnum+uvacaflag) + '\')" '  +
        ">\n<RMTEXT>" + uvaca_or_not + ind,
        line,
    )


def dharma_transliteration(line):
    """
    Transforms letters below to Dharma Project conventions.
    """
    line = re.sub("ṃ", "ṁ", line)
    line = re.sub("ṛ", "r̥", line)
    line = re.sub("ṝ", "r̥̄", line)
    line = re.sub("ḷ", "l̥", line)
    line = re.sub("Ṃ", "Ṁ", line)
    line = re.sub("Ṛ", "R̥", line)
    line = re.sub("Ṝ", "R̥̄", line)
    line = re.sub("Ḷ", "L̥", line)
    return line


def produce_dn_version(line, textflag, proseflag, chapter, vsnum):
    """
    Stripping line within TEXT_OPEN_TAG and TEXT_CLOSING_TAG
    mainly to produce the Devanāgarī version
    """
    maintextdn = re.sub("{ }", "", line)
    maintextdn = txt_output_line.txt_output_line(maintextdn, textflag)
    maintextdn = re.sub("<MNTR>", "", maintextdn)
    maintextdn = re.sub("</MNTR>", "", maintextdn)
    maintextdn = re.sub("<mainwrap>", "", maintextdn)
    maintextdn = re.sub("</mainwrap>", "", maintextdn)
    maintextdn = re.sub("<div>", "", maintextdn)
    maintextdn = re.sub("</div>", "", maintextdn)
    maintextdn = re.sub("{-}", "", maintextdn)
    if proseflag is False:
        maintextdn = re.sub(
            "\|\|.*",
            ' ॥<span  class="vsnum">' + str(chapter) + ":" + str(vsnum) + "</span>",
            maintextdn,
        )
    else:
        maintextdn = re.sub("\|\|", " ॥", maintextdn)
    maintextdn = re.sub("\|", " ।", maintextdn)
    # <crux> has been turned into †, now turning back to <crux>
    # </crux> has been turned into ‡, now turning back to </crux>
    maintextdn = re.sub("†", "<crux>", maintextdn)
    maintextdn = re.sub("‡", "</crux>", maintextdn)
    maintextdn = re.sub("\n", "", maintextdn)
    # producing a Devanāgarī version of the line:
    return toDevanagariExceptTagsAndCommands.main(maintextdn)


# define your own tags
TEXT_OPEN_TAG = "<TEXT>"
TEXT_CLOSING_TAG = "</TEXT>"
APP_OPEN_TAG = "<APP>"
APP_CLOSING_TAG = "</APP>"
PARAL_OPEN_TAG = "<PARAL>"
PARAL_CLOSING_TAG = "</PARAL>"
NOTE_OPEN_TAG = "<NOTE>"
NOTE_CLOSING_TAG = "</NOTE>"
level_open_tags = {
    "<TITLE>": "h1",
    "<CHAPTER>": "chapter",
    "<SUBCHAPTER>": "subchapter",
    "<SUBSUBCHAPTER>": "subsubchapter",
}
level_closing_tags = {
    "</TITLE>": "h1",
    "</CHAPTER>": "chapter",
    "</SUBCHAPTER>": "subchapter",
    "</SUBSUBCHAPTER>": "subsubchapter",
}


def html_scroll(filename):
    """
    Main function to produce the edition line by line
    """
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
    # pvarflag = False
    # uvacaflag is 0 or 1; used to increment vsnum temporarily when reaching an uvaca line
    uvacaflag = 0
    trflag = False
    noteflag = False
    onflag = False
    first_text_tag = True
    # note = ''
    collected_tr = ""
    collected_notes = ""
    # indent verse line?
    indent = 0
    lastnotenum = "0.0"
    currentnotenum = "0.0"
    pada = ""

    # header
    print(
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
       <meta http-equiv="content-type" content="text/html; charset=UTF-8">
       <rt id="realtitle"></rt>
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <link rel="stylesheet" href="css/style_scroll.css">
       <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
       <script src="js/jquery.min.js"></script>
       <script defer src="js/csaba_edition_scripts.js"></script>
    </head>
       <body style="background-image: url('img/background.jpg'); background-size: 100% 100%; background-repeat: no-repeat; background-attachment: fixed;" onload="closeapp();">
          <div class="text" id="sanskrittext">
           <div id="sanskrittextdragarea" onclick="putareaforward('sanskrittext')">
          <br/>
        """
    )

    # [Version of ' + str(today) + ']
    # color selector
    # print('''<select id="themes"  style="background-color:#fff7e6">
    #          <option value="default">Choose Colour Theme</option>
    #          <option value="contrast">Contrasted</option>
    #          <option value="light">Light</option>
    #          <option value="gray">Gray</option>
    #         </select>
    #       <script>
    #       $("select").change(function() {
    #                if ($(this).val() === "contrast") {
    #                    doContrastedColorTheme();
    #                    }
    #                if ($(this).val() === "gray") {
    #                    doGrayColorTheme();
    #                    }
    #                if ($(this).val() === "light") {
    #                    doLightColorTheme();
    #                    }
    #                })
    #                </script>
    #               ''')
    # instructions box
    print(
        """<div class="header">
        &nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp;&nbsp;
    <div class="wrap-main">
     <span class="instr" onclick="showApparatus(\'instructions\')">
        Click on this line for instructions on how to use this online edition
     </span>
     <div class="wrap-content" onclick="hideFunction(\'instructions\')" id="instructions">
     <span class="instr">
        • You can drag the three windows with your mouse, and you can resize them
        </span>
        <span class="instr">
        • Press keys \'s\', \'t\', and \'n\' to toggle the Sanskrit text, the translation and the notes, respectively (the last one popping up will take the foreground, potentially overlapping the others);
        press \'o\' to open/close all apparatus entries;
        press \'d\' to toggle Roman/Devanāgarī
     </span>
     <span class="instr">
         • You can also use these buttons for the same:
     </span>
     <span class="instr">
          &nbsp;&nbsp;&nbsp;&nbsp;
          <button onclick="togglearea('translation')" id="showtextandtranslation">Toggle Translation</button>
     </span>
     <span class="instr">
          &nbsp;&nbsp;&nbsp;&nbsp;
          <button onclick="togglearea('notes')" id="txttrnotes">Toggle Notes</button>
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
          • Double click on Sanskrit line to display apparatus and
            highlight translation of verse (if translation is visible)
     </span>
     <span class="instr">
          • Single click on Sanskrit line to
            scroll to relevant note, if any, and if notes are being displayed
     </span>
     <span class="instr">
          • Click inside apparatus box to close it
     </span>
     <span class="instr">
          • Double click on translation to toggle highlighting on relevant Sanskrit verse
     </span>
     <span class="instr">
          • Hovering over a siglum in the apparatus that has the ∑ sign will show the underlying MSS sigla
     </span>
     <span class="instr">
          • If your browser has problems rendering the Devanāgarī font,
          change your browser\'s default font (e.g. to \'Noto Sans Devanagari\' on Ubuntu)
     </span>
     </div>
     </div>
     </div>
     <br/>
     """
    )

    with open(filename, "r", encoding="utf-8") as openfile:
        for line in openfile:
            # line = dharma_transliteration(line)
            line = re.sub("^\**", "", line)
            if "<START/>" in line:
                onflag = True
                continue
            if "<STOP/>" in line:
                onflag = False
                continue
            if onflag is True:
                if "<NOTANUSTUBH/>" in line:
                    anustubh = False
                    proseflag = False
                    hemistich = 0
                    continue
                if "<ANUSTUBH/>" in line:
                    anustubh = True
                    proseflag = False
                    continue
                if "<PROSE>" in line:
                    proseflag = True
                    anustubh = False
                    continue
                if "</PROSE>" in line:
                    proseflag = False
                    anustubh = False
                    continue
                if "<SETVSNUM" in line:
                    outputline = re.sub('.*<SETVSNUM="', "", line)
                    outputline = re.sub('".*', "", outputline)
                    vsnum = int(outputline) - 1
                    continue
                if '<startchapter-n="' in line:
                    outputline = re.sub('.*<startchapter-n="', "", line)
                    outputline = re.sub('".*', "", outputline)
                    chapter = int(outputline)
                    vsnum = 0
                    if first_text_tag is False:
                        print("\n</div>\n</div>\n<br/><br/><br/><!-- NEWCHAPTER -->")
                    else:
                        print("<!-- NEWCHAPTER -->")
                    first_text_tag = True
                    continue

                if TEXT_OPEN_TAG in line:
                    if first_text_tag is False:
                        # close div and start new wrap for verse + apparatus
                        line = re.sub(
                            TEXT_OPEN_TAG,
                            "\n</div>\n</div>\n\n<mainwrap>\n<TEXT>",
                            line,
                        )
                    else:
                        line = re.sub(TEXT_OPEN_TAG, "\n<mainwrap>\n<TEXT>", line)
                        first_text_tag = False
                # if it is the main text:
                if TEXT_OPEN_TAG in line or textflag is True:
                    textflag = True
                    # deleting TeX-style \- (`can break line here')
                    line = re.sub("\\\\-", "", line)
                    # change wrong ' for avagraha
                    line = re.sub("’", "'", line)

                    # make a Devanāgarī version of the line
                    maintextdn = produce_dn_version(
                        line, textflag, proseflag, chapter, vsnum
                    )
                    maintextdn = re.sub(
                        '\\\\char"0930\\\\char"094D\\\\char"090B', "रृ", maintextdn
                    )

                    uvacaflag = 0
                    if TEXT_CLOSING_TAG in line:
                        textflag = False
                    # check if this is the end of a verse
                    if "||" in line and proseflag is False:
                        chap_and_vsnum = (
                            '<span class="vsnum">'
                            + str(chapter)
                            + "."
                            + str(vsnum)
                            + "</span>||"
                        )
                        # We need a little extra vertical space between verses
                        # (amount controlled in the css file)
                        vspace = "<spaceaftersloka/>"
                    else:
                        chap_and_vsnum = ""
                        vspace = ""
                    if (
                        "||" in line
                        and anustubh is True
                        and hemistich == 1
                        and proseflag is False
                    ):
                        outputline = re.sub("\|\|", " ||" + chap_and_vsnum, line)
                        # main process to put in stuff
                        pada = "cd"
                        indent = 0
                        outputline = putin_text_line(
                            outputline, chapter, vsnum, pada, indent, uvacaflag
                        )
                        hemistich = 0
                    elif "||" in line and anustubh is False and proseflag is False:
                        outputline = re.sub("\|\|", " ||" + chap_and_vsnum, line)
                        outputline = "\n" + outputline + "\n"
                        # main process to put in stuff
                        pada = "d"
                        indent = 1
                        outputline = putin_text_line(
                            outputline, chapter, vsnum, pada, indent, uvacaflag
                        )
                        hemistich = 0
                    # special danda: it does not increase verse number, e.g. after devy uvāca
                    elif "|*" in line:
                        # main process to put in stuff
                        uvacaflag = 1
                        pada = "uvaca"
                        indent = 0
                        outputline = re.sub("\|\*", " | ", line)
                        outputline = putin_text_line(
                            outputline, chapter, vsnum, pada, indent, uvacaflag
                        )
                        outputline = re.sub(
                            TEXT_CLOSING_TAG, "</uvaca></TEXT>", outputline
                        )
                        hemistich = 0
                    # with anuṣṭubh, a danda increases verse number if it is the first single danda
                    elif (
                        "|" in line
                        and hemistich == 0
                        and anustubh is True
                        and proseflag is False
                    ):
                        vsnum += 1
                        # main process to put in stuff
                        uvacaflag = 0
                        pada = "ab"
                        indent = 0
                        outputline = putin_text_line(
                            line, chapter, vsnum, pada, indent, uvacaflag
                        )
                        outputline = re.sub("\|", " |", outputline)
                        # the next single danda is not a first single danda
                        hemistich = 1
                    # check if this is a non-anuṣṭubh first line
                    elif "|" not in line and hemistich == 0 and anustubh is False:
                        # no indent
                        vsnum += 1
                        # main process to put in stuff
                        uvacaflag = 0
                        pada = "a"
                        indent = 0
                        outputline = putin_text_line(
                            line, chapter, vsnum, pada, indent, uvacaflag
                        )
                        hemistich = 1
                    # check if this is a non-anuṣṭubh third line
                    elif "|" not in line and hemistich == 2 and anustubh is False:
                        # no indent
                        # main process to put in stuff
                        uvacaflag = 0
                        pada = "c"
                        indent = 0
                        outputline = putin_text_line(
                            line, chapter, vsnum, pada, indent, uvacaflag
                        )
                        hemistich = hemistich + 1
                    # if this is a first single danda but it is not anuṣṭubh,
                    # don't increase verse number; it's pāda b
                    elif "|" in line and anustubh is False and proseflag is False:
                        outputline = "\n" + line
                        # main process to put in stuff
                        uvacaflag = 0
                        pada = "b"
                        indent = 1
                        outputline = putin_text_line(
                            line, chapter, vsnum, pada, indent, uvacaflag
                        )
                        outputline = re.sub("\|", " |", outputline)
                        hemistich = hemistich + 1
                    # if it's a three-line anuṣṭubh, two ||s mean pāda ef
                    elif "||" in line and hemistich == 2 and anustubh is True:
                        outputline = re.sub("\|\|", " ||" + chap_and_vsnum, line)
                        # main process to put in stuff
                        uvacaflag = 0
                        pada = "ef"
                        indent = 0
                        outputline = putin_text_line(
                            outputline, chapter, vsnum, pada, indent, uvacaflag
                        )
                        hemistich = 0
                    # if it's a three-line anuṣṭubh, one | means pāda cd when it's hemistich 1
                    elif "|" in line and hemistich == 1 and anustubh is True:
                        # main process to put in stuff
                        uvacaflag = 0
                        pada = "cd"
                        indent = 0
                        outputline = putin_text_line(
                            line, chapter, vsnum, pada, indent, uvacaflag
                        )
                        outputline = re.sub("\|", " |", outputline)
                        hemistich = 2
                    else:
                        outputline = line
                    outputline = re.sub("{-}", "-", outputline)
                    outputline = re.sub("{ }", " ", outputline)
                    if "<COLOPHON>" in outputline:
                        pada = "colophon"
                        outputline = re.sub(
                            "<COLOPHON>",
                            "\n<colophon>|| ",
                            putin_text_line(
                                outputline, chapter, vsnum, pada, indent, uvacaflag
                            ),
                        )
                        outputline = re.sub("</COLOPHON>", " ||</colophon>", outputline)
                    # b and d lines non-anuṣṭubh verses with indentation
                    if "&#160;&#160;&#160;&#160" in outputline:
                        outputline = re.sub(
                            TEXT_CLOSING_TAG + ".*",
                            "</RMTEXT>\n<DNTEXT>&#160;&#160;&#160;&#160;"
                            + maintextdn
                            + " </DNTEXT></TEXT>\n<apparatuswrap>",
                            outputline,
                        )
                    else:
                        outputline = re.sub(
                            TEXT_CLOSING_TAG + ".*",
                            "</RMTEXT>\n<DNTEXT>"
                            + uvacaflag * "<uvaca>"
                            + maintextdn
                            + uvacaflag * " </uvaca>"
                            + " </DNTEXT></TEXT>\n<apparatuswrap>",
                            outputline,
                        )
                    if "</COLOPHON>" in line:
                        outputline = re.sub("</DNTEXT>", " ॥</DNTEXT>", outputline)
                    outputline = re.sub("Ó", "oṃ", outputline)
                    # outputline = re.sub('<uvaca>', '', outputline)
                    # outputline = re.sub('</uvaca>', '', outputline)
                    outputline = re.sub("<ja>", " ", outputline)
                    outputline = re.sub("</ja>", " ", outputline)
                    # outputline = re.sub('<crux>', '†', outputline)
                    # outputline = re.sub('</crux>', '†', outputline)
                    outputline = re.sub("\\\\-", "", outputline)
                    outputline = re.sub(
                        "<mainwrap>", '<div class="wrap-main">', outputline
                    )
                    outputline = re.sub("</mainwrap>", "</div>", outputline)
                    outputline = re.sub(
                        "<apparatuswrap>",
                        vspace
                        + '\n\n<div class="wrap-content" id="app'
                        + str(chapter)
                        + "."
                        + str(vsnum + uvacaflag)
                        + pada
                        + '">',
                        outputline,
                    )
                    outputline = re.sub("</apparatuswrap>", "</div>", outputline)
                    # prose
                    if proseflag is True:
                        outputline = re.sub(
                            TEXT_OPEN_TAG, "<TEXTPROSE>\n<RMTEXT>", outputline
                        )
                        outputline = re.sub(
                            TEXT_CLOSING_TAG, "</TEXTPROSE>", outputline
                        )
                    print(outputline)

                # dealing with the apparatus
                if APP_OPEN_TAG in line or appflag is True:
                    appflag = True
                    if APP_CLOSING_TAG in line:
                        appflag = False
                    outputline = re.sub("{ }", " ", line)
                    # matching the search pattern itself
                    outputline = re.sub(
                        "(?P<group>\\\\v[a-z]*)",
                        "<VSNUMPADA>\\1</VSNUMPADA>",
                        outputline,
                    )
                    outputline = re.sub("\\\\vo", str(vsnum + uvacaflag), outputline)
                    outputline = re.sub("\\\\v", str(vsnum + uvacaflag), outputline)
                    outputline = re.sub(APP_OPEN_TAG, "", outputline)
                    outputline = re.sub(APP_CLOSING_TAG, "<br/>", outputline)
                    outputline = re.sub("\\\\csa ", "ā", outputline)
                    outputline = re.sub("\\\\csi ", "i", outputline)
                    outputline = re.sub("<hideNepMss>", '<div class="tooltip">\\\\mssN<span class="tooltiptext">', outputline)
                    outputline = re.sub("</hideNepMss>", "</span></div>", outputline)
                    outputline = re.sub("<hideSouthMss>", '<div class="tooltip">\\\\mssS<span class="tooltiptext">', outputline)
                    outputline = re.sub("</hideSouthMss>", "</span></div>", outputline)
                    if 'mssALL' in outputline:
                        outputline = re.sub('mssALL', '<div class="tooltip">\\\\mssALL<span class="tooltiptext">', outputline)
                        outputline = re.sub(';', "</span></div>;", outputline)

                    outputline = xml_substitutions.xml_substitutions(outputline)

                    dn_output_line = re.sub("{ }", "", line)
                    dn_output_line = re.sub("</LEM>", " </LEM>", dn_output_line)
                    dn_output_line = re.sub("<hideNepMss>", '<div class="tooltip">\\\\mssN<span class="tooltiptext">', dn_output_line)
                    dn_output_line = re.sub("</hideNepMss>", "</span></div>", dn_output_line)
                    dn_output_line = re.sub("<hideSouthMss>", '<div class="tooltip">\\\\mssS<span class="tooltiptext">', dn_output_line)
                    dn_output_line = re.sub("</hideSouthMss>", "</span></div>", dn_output_line)
                    dn_output_line = re.sub("\\\\-", "", dn_output_line)
                    dn_output_line = toDevanagariExceptTagsAndCommands.main(
                        re.sub("{ }", "", dn_output_line)
                    )
                    # matching the search pattern itself
                    dn_output_line = re.sub(
                        "(?P<group>\\\\v[a-z]*)",
                        "<VSNUMPADA>\\1:</VSNUMPADA>",
                        dn_output_line,
                    )
                    dn_output_line = re.sub(
                        "\\\\vo", str(vsnum + uvacaflag), dn_output_line
                    )
                    dn_output_line = re.sub(
                        "\\\\v",
                        toDevanagariExceptTagsAndCommands.main(str(vsnum + uvacaflag)),
                        dn_output_line,
                    )
                    dn_output_line = re.sub(APP_OPEN_TAG, "", dn_output_line)
                    dn_output_line = re.sub(APP_CLOSING_TAG, "<br/>", dn_output_line)
                    dn_output_line = xml_substitutions.xml_substitutions(dn_output_line)

                    print(
                        "<RMAPP>"
                        + outputline
                        + "</RMAPP>"
                        + "<DNAPP>"
                        + dn_output_line
                        + "</DNAPP>"
                    )

                if PARAL_OPEN_TAG in line or paralflag is True:
                    paralflag = True
                    if PARAL_CLOSING_TAG in line:
                        paralflag = False
                    outputline = re.sub("{ }", " ", line)
                    outputline = re.sub(" *\\\\vo", str(vsnum + uvacaflag), outputline)
                    outputline = re.sub(
                        PARAL_OPEN_TAG + " *\\\\v",
                        "<PARAL>" + str(vsnum + uvacaflag),
                        outputline,
                    )
                    outputline = xml_substitutions.xml_substitutions(outputline)
                    if PARAL_OPEN_TAG in line:
                        print('<hr width="50%" size="1" align="left" color="#cc8800"/>')
                    print(outputline)
                if "<LACUNA>" in line or lacunaflag is True:
                    lacunaflag = True
                    if "</LACUNA>" in line:
                        lacunaflag = False
                    outputline = re.sub("{ }", " ", line)
                    outputline = re.sub(
                        "<LACUNA> *\\\\vo",
                        "<LACUNA>" + str(vsnum + uvacaflag),
                        outputline,
                    )
                    outputline = re.sub(
                        "<LACUNA> *\\\\v",
                        "<LACUNA>" + str(vsnum + uvacaflag),
                        outputline,
                    )
                    outputline = xml_substitutions.xml_substitutions(outputline)
                    if "<LACUNA>" in line:
                        print('<hr width="50%" size="1" align="left" color="#cc8800"/>')
                    print(outputline)
                # if '<PVAR>' in line or pvarflag is True:
                #    pvarflag = True
                #    if '</PVAR>' in line:
                #        pvarflag = False
                #    outputline = re.sub('{ }', " ", line)
                #    outputline = re.sub('<PVAR>\\\\vo', "<PVAR>", outputline)
                #    outputline = re.sub('<PVAR>\\\\v', "<PVAR>", outputline)
                #    outputline = xml_substitutions.xml_substitutions(outputline)
                #    print(outputline)
                if "<TRCHAPTER>" in line:
                    trflag = True
                    outputline = re.sub(
                        "<!-- <TRCHAPTER>", "<br/><br/><br/><trnslchapter>", line
                    )
                    outputline = re.sub(
                        "</TRCHAPTER> -->", "</trnslchapter>", outputline
                    )
                    outputline = xml_substitutions.xml_substitutions(outputline)
                    if "</TRCHAPTER>" in line:
                        trflag = False
                        collected_tr = collected_tr + outputline
                    else:
                        collected_tr = collected_tr + outputline

                if "<TRSUBCHAPTER>" in line:
                    trflag = True
                    outputline = re.sub(
                        "<TRSUBCHAPTER>", "<br/><br/><trnslsubchapter>", line
                    )
                    outputline = re.sub(
                        "</TRSUBCHAPTER>", "</trnslsubchapter>", outputline
                    )
                    outputline = xml_substitutions.xml_substitutions(outputline)
                    if "</TRSUBCHAPTER>" in line:
                        trflag = False
                        collected_tr = collected_tr + outputline
                    else:
                        collected_tr = collected_tr + outputline

                if "<TRSUBSUBCHAPTER>" in line:
                    trflag = True
                    outputline = re.sub(
                        "<TRSUBSUBCHAPTER>", "<br/><br/><trnslsubsubchapter>", line
                    )
                    outputline = re.sub(
                        "</TRSUBSUBCHAPTER>", "</trnslsubsubchapter>", outputline
                    )
                    outputline = xml_substitutions.xml_substitutions(outputline)
                    if "</TRSUBSUBCHAPTER>" in line:
                        trflag = False
                        collected_tr = collected_tr + outputline
                    else:
                        collected_tr = collected_tr + outputline

                if "<TRCOLOPHON>" in line:
                    trflag = True
                    outputline = re.sub(
                        "<TRCOLOPHON>",
                        '<br/><br/><trnslcolophon id="tr'
                        + str(chapter)
                        + "."
                        + str(vsnum)
                        + 'colophon">',
                        line,
                    )
                    outputline = re.sub("</TRCOLOPHON>", "</trnslcolophon>", outputline)
                    outputline = xml_substitutions.xml_substitutions(outputline)
                    if "</TRCOLOPHON>" in line:
                        trflag = False
                        collected_tr = (
                            collected_tr + outputline + "<br/><br/><br/><br/>"
                        )
                    else:
                        collected_tr = collected_tr + outputline

                # Dealing with the translation, actually just collecting it
                if "<TR>" in line or trflag is True:
                    trflag = True
                    # &#39 is a single quote, needed because of a bug...?
                    strng = "sktvrs" + str(chapter) + "." + str(vsnum + uvacaflag)
                    outputline = re.sub(
                        "<?!?-?-? ?<TR>",
                        '\n<trnsl class="trnsl'
                        + str(chapter)
                        + "."
                        + str(vsnum + uvacaflag)
                        + '" '
                        + 'ondblclick="showSkt(&#39'
                        + strng
                        + '&#39)">',
                        line,
                    )
                    outputline = re.sub("</TR> ?-?-?>?.*", "</trnsl>", outputline)
                    outputline = re.sub("---", "—", outputline)
                    if "<TR>" in line and (prev_vsnum != vsnum and uvacaflag != 1):
                        collected_tr = (
                            collected_tr
                            + "\n<br/><br/>\n"
                            + '<span class="vsnum" id="tr'
                            + str(chapter)
                            + "."
                            + str(vsnum)
                            + '">'
                            + "|"
                            + str(chapter)
                            + "."
                            + str(vsnum)
                            + "| </span>"
                        )
                    if "<TR>" in line and uvacaflag == 1:
                        collected_tr = collected_tr + "<br/><br/>"
                    if "</TR>" in line:
                        prev_vsnum = vsnum
                        trflag = False
                        collected_tr = collected_tr + outputline
                        # handling the sign |F| meaning 'and the following verse';
                        # output e.g. --|1.8| after |1.7|
                        collected_tr = re.sub(
                            "\|F\|",
                            "-- |"
                            + '<span class="vsnum">'
                            + str(chapter)
                            + "."
                            + str(vsnum + 1)
                            + "</span>"
                            + "| ",
                            collected_tr,
                        )
                        collected_tr = xml_substitutions.xml_substitutions(collected_tr)
                        collected_tr = re.sub("`", "‘", collected_tr)
                        collected_tr = re.sub("'", "’", collected_tr)
                    else:
                        collected_tr = collected_tr + outputline

                # Dealing with notes, actually just collecting them
                if NOTE_OPEN_TAG in line or noteflag is True:
                    currentnotenum = str(chapter) + "." + str(vsnum)
                    noteflag = True
                    outputline = xml_substitutions.xml_substitutions(line)
                    outputline = re.sub("`", "‘", outputline)
                    outputline = re.sub("'", "’", outputline)
                    if NOTE_OPEN_TAG in line and lastnotenum != currentnotenum:
                        collected_notes = (
                            collected_notes
                            + "<br/><br/>\n"
                            + "|"
                            + '<vsnum id="note'
                            + str(chapter)
                            + "."
                            + str(vsnum)
                            + '">'
                            + str(chapter)
                            + "."
                            + str(vsnum)
                            + "</vsnum>"
                            + "| \n"
                        )
                        lastnotenum = currentnotenum
                    if NOTE_CLOSING_TAG in line:
                        noteflag = False
                        collected_notes = collected_notes + outputline
                    else:
                        collected_notes = collected_notes + outputline

                # Dealing with headers
                if (
                    "<SUBSUBCHAPTER>" in line
                    or "<SUBCHAPTER>" in line
                    or "<CHAPTER>" in line
                    or "<TITLE>" in line
                ):
                    # checking <CHAPTER> etc. levels in line
                    level = ""
                    for lop in level_open_tags:
                        if lop in line:
                            level = level_open_tags[lop]
                    # the spaces also make sure that final consonants will
                    # will come out properly in Devanagari
                    outputline = re.sub("<.?TITLE>", " ", line)
                    outputline = re.sub("<.?TITLE>", " ", line)
                    outputline = re.sub("<CHAPTER>", "[ ", outputline)
                    outputline = re.sub("</CHAPTER>", " ]", outputline)
                    outputline = re.sub("<SUBCHAPTER>", "[ ", outputline)
                    outputline = re.sub("</SUBCHAPTER>", " ]", outputline)
                    outputline = re.sub("<SUBSUBCHAPTER>", "[ ", outputline)
                    outputline = re.sub("</SUBSUBCHAPTER>", " ]", outputline)
                    # turn it into Devanāgarī
                    textdn = toDevanagariExceptTagsAndCommands.main(
                        re.sub("{ }", "", outputline.lower())
                    )
                    # to convert rṛ back; it was converted for EB Garamond bug by a Devanāgarī module
                    textdn = re.sub(
                        '\\\\char"0930\\\\char"094D\\\\char"090B', "रृ", textdn
                    )
                    outputline = re.sub("{ }", " ", outputline)
                    if first_text_tag is False:
                        print("\n</div>\n</div>")
                    print(
                        "<RMTEXT>"
                        + "<"
                        + level
                        + ">\n"
                        + outputline
                        + "</"
                        + level
                        + "></RMTEXT>\n<DNTEXT><"
                        + level
                        + ">\n"
                        + textdn
                        + "</"
                        + level
                        + "></DNTEXT>"
                    )
                    first_text_tag = True

    # close Sanskrit text box, last </div> closes the sanskrittextdragarea
    print("</div></div><br/><br/><br/><br/></div></div>")

    # print translation box
    print(
        """<div class="translation" id="translation">
             <div id="translationdragarea" onclick="putareaforward('translation')">
             <br/>
             """
    )
    #         <select id="trthemes" style="background-color:#fff7e6">
    #           <option value="default">Choose Colour Theme</option>
    #           <option value="contrast">Contrasted</option>
    #           <option value="light">Light</option>
    #           <option value="gray">Gray</option>
    #         </select>
    #         <script>
    #            $("#trthemes").change(function() {
    #                trtexts = document.getElementsByTagName("trnsl");
    #                if ($(this).val() === "contrast") {
    #                     $(".translation").css("background-color", "black");
    #                     for (t = 0; t < trtexts.length; t++) {
    #                         trtexts[t].style.color =  "white";
    #                         }
    #                }
    #                if ($(this).val() === "light") {
    #                     $(".translation").css("background-color", "white");
    #                     for (t = 0; t < trtexts.length; t++) {
    #                        trtexts[t].style.color =  "black";
    #                       }
    #                   }
    #                if ($(this).val() === "gray") {
    #                   $(".translation").css("background-color", "black");
    #                   for (t = 0; t < trtexts.length; t++) {
    #                        trtexts[t].style.color =  "gray";
    #                     }
    #                  }
    #                });
    #         </script>
    #        <br/><br/><br/><br/>
    print("<h2>Translation</h2>")
    print(collected_tr)
    # last but one </div> closes the drag translationdragarea div
    print("\n<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/></div></div>")

    # print notes box
    print('<div class="notes" id="notes">')
    print(
        '<div id="notesdragarea" onclick="putareaforward(\'notes\')"><br/>\n<h2>Notes</h2>\n'
    )
    print(collected_notes)
    # first </div> closes the drag notesdragarea div
    print("\n<br/>\n<br/></div></div>\n")

    # print mss box
    # print('<div class="msimage" id="mssimages">\n<h2>Sources</h2>\n')
    # MSS images for VSS:
    # open_mssdata_file = open("/home/csaba/indology/dharma_project/vrsa_edition/mssimages.html", "r")
    # MSS images for SDhS10:
    with open(
        "/home/csaba/indology/dharma_project/sdhs10/mssimages.html",
        "r",
        encoding="utf-8",
    ) as open_mssdata_file:
        for data_line in open_mssdata_file:
            print(data_line)
    drag.insert_drag_js()
    print("\n</body>\n</html>")
    openfile.close()
