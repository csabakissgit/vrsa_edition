import re
from textprocess import devanagari_characters

stoppers = [" ", "\n", "°", "<", "\\", "("]

tagFlagOn = False
commandFlagOn = False
englishFlagOn = False


def checkIfTagOrCommand(char):
    global tagFlagOn
    global commandFlagOn
    global englishFlagOn
    if char == '<':
      tagFlagOn = True
    elif char == '>':
      tagFlagOn = False
    elif char == '\\':
      commandFlagOn = True
    elif char == ' ':
      commandFlagOn = False   
    elif char == 'Ł':
      englishFlagOn = True   
    elif char == '$':
      englishFlagOn = False   
    return (tagFlagOn, commandFlagOn, englishFlagOn)

def main(line):
    line = re.sub("{ }", "", line)

    #for future use
    newar = False
    if newar == False:
        dic, vowels, consonants = devanagari_characters.devanagari_characters()
    else:
        dic, vowels, consonants = devanagari_characters.newar_characters()

    def preprocessing(inputline,vowels,consonants):
            # trick : "|" becomes " |" to handle final virama
            preprocessingChars = [('ai', '\uE019'), ('au', '\uE01B'), ('ā', '\uE003'), ('i', '\uE005'), ('ī', '\uE007'),  ('u', '\uE009'),
                                  ('ū', '\uE00B'), ('ṛ', '\uE00D'), ('ṝ', '\uE00F'), ('ḷ', '\uE011'), ('ḹ', '\uE013'),
                                  ('e', '\uE015'), ('o', '\uE017'), ('ṃ', '\uE01D'), ('ḥ', '\uE01F'),
                                  ('kh', '\uE021'), ('gh', '\uE023'), ('ch', '\uE025'), ('jh', '\uE027'),
                                  ('ṭh', '\uE029'), ('ḍh', '\uE02B'), ('th', '\uE02D'), ('dh', '\uE02F'),
                                  ('ph', '\uE031'), ('bh', '\uE033'),
                                  ('\|', ' |'), ('\| \|', '||'), (",", " ,"), ('a', '\uE001')]

            # to handle final virama if there is no danda
            inputline = inputline + "  "

            # turning double characters such as 'ai' and 'gh' into single special characters (plus all vowels to handle initial vowels):
            for p in preprocessingChars:
                    inputline = re.sub(p[0], p[1], inputline)


            '''
            # spaces, sandhi
            # list of characters separated
            s = list(inputline)
            i = 0
            # C + V should be written as conjunct 
            while i < len(s)-2:
                    if s[i] in consonants and s[i+1] == "\uE000" and s[i+2] in vowels:
                            s[i+1] = ''	
                            assert False
                    elif s[i] in consonants and s[i+1] == ' ' and s[i+2] in consonants:
                            s[i+1] = ' '
                            assert False
                    i += 1
            # put them back together
            "".join(s)
            '''

            return inputline

    # turning some Roman characters back from the Dharma compliant forms for Devanāgarī conversion:
    line = re.sub("ṁ", "ṃ", line)
    # first ṝ, then ṛ, to avoid a bug
    line = re.sub("r̥̄", "ṝ", line)
    line = re.sub("r̥", "ṛ", line)
    line = re.sub("l̥", "ḷ", line)
    # crux in main line
    line = re.sub("<crux>", "†", line)
    line = re.sub("</crux>", "†", line)
    line = re.sub('\\\\csi', 'ि', line)    
    # 'ि

    line = preprocessing(line,vowels,consonants)
    conj = False
    lineout = ''
    # putting the Devanagari characters together
    i = 0
    while i < len(line):
            #print(lineout, conj, line[i], i, line[i] in consonants, )
            tagFlagOn, commandFlagOn, englishFlagOn = checkIfTagOrCommand(line[i])
            if tagFlagOn == True or commandFlagOn == True or englishFlagOn == True:
                    lineout = lineout + line[i]
                    i += 1
                    continue
            # init vowel
            if conj == False and line[i] in vowels:
                    # if it is initial, increment PUA char by one 
                    lineout = lineout + chr(ord(line[i])+1)
            # last consonant, put in virāma
            elif i < len(line)-2 and line[i] in consonants and line[i+1] in stoppers:
                    if conj == True:
                        lineout = lineout + "\uE020" + line[i] + "\uE020 "
                    else:
                        lineout = lineout + line[i] + "\uE020"
            # syllable initial consonant, nothing special to do
            elif conj == False and line[i] in consonants:
                    conj = True
                    lineout = lineout + line[i]
            # half consonant: put in a virāma
            elif conj == True and line[i] in consonants:
                    lineout = lineout + "\uE020" + line[i]
            # non-initial vowel: nothing special to do
            elif conj == True and line[i] in vowels:
                    conj = False
                    if line[i] != '\uE001': # inherent 'a' is ignored in Devanāgarī
                        lineout = lineout + line[i]
            # anything else:
            else:
                    #print(letter, end='')
                    lineout = lineout + line[i]
                    conj = False
            i += 1

    returnLine = ""
    for character in lineout:
            found = False
            tagFlagOn, commandFlagOn, englishFlagOn = checkIfTagOrCommand(character)
            if tagFlagOn == True or commandFlagOn == True or englishFlagOn == True:
                    returnLine = returnLine + character
                    continue         
            #check if it is a Devanāgarī character
            for d in dic:
                if character == d[0] and tagFlagOn == False and commandFlagOn == False:
                    if character != '\uE001': # if it is inherent 'a' then do nothing
                        returnLine = returnLine + d[1]
                    '''
                    if d[0] in vowels:
                            returnLine = returnLine + '\\-'
                    '''
                    found = True
                    break
            # if not in list of Devanāgarī characters:
            if found == False:
                    returnLine = returnLine + character
    returnLine = re.sub('\uE001', 'a', returnLine)    
    returnLine = re.sub('\uE003', 'ā', returnLine)    
    returnLine = re.sub('\uE005', 'i', returnLine)    
    returnLine = re.sub('\uE007', 'ī', returnLine)    
    returnLine = re.sub('\uE009', 'u', returnLine)    
    returnLine = re.sub('\uE00B', 'ū', returnLine)    
    leturnLine = re.sub('\uE00D', 'ṛ', returnLine)    
    returnLine = re.sub('\uE00F', 'ṝ', returnLine)    
    returnLine = re.sub('\uE011', 'ḷ', returnLine)    
    returnLine = re.sub('\uE013', 'ḹ', returnLine)    
    returnLine = re.sub('\uE015', 'e', returnLine)    
    returnLine = re.sub('\uE017', 'o', returnLine)    
    returnLine = re.sub('\uE019', 'ai', returnLine)    
    returnLine = re.sub('\uE01B', 'au', returnLine)    
    returnLine = re.sub('\uE01D', 'ṃ', returnLine)    
    returnLine = re.sub('\uE01F', 'ḥ', returnLine)    
    returnLine = re.sub('\uE021', 'kh', returnLine)    
    returnLine = re.sub('\uE023', 'gh', returnLine)    
    returnLine = re.sub('\uE025', 'ch', returnLine)    
    returnLine = re.sub('\uE027', 'jh', returnLine)    
    returnLine = re.sub('\uE029', 'ṭh', returnLine)    
    returnLine = re.sub('\uE02B', 'ḍh', returnLine)    
    returnLine = re.sub('\uE02D', 'th', returnLine)    
    returnLine = re.sub('\uE02F', 'dh', returnLine)    
    returnLine = re.sub('\uE031', 'ph', returnLine)    
    returnLine = re.sub('\uE033', 'bh', returnLine)    
    returnLine = re.sub(' ,', ',', returnLine)
    returnLine = re.sub(' ;', ';', returnLine)

    # to fix a bug in the font AdishilaDev:
    returnLine = re.sub('रृ', '\\\\char"0930\\\\char"094D\\\\char"090B', returnLine)
    # to fix a bug in the font AdishilaDev, raise ॰
    #returnLine = re.sub('°', '\\\\raise.15em\\\\hbox{॰}', returnLine)
    return returnLine

