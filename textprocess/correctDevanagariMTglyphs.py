import re
'''
Corrects problems with conjuncts in the font DevanagariMT
'''

def main(line, useFont):
    if useFont == "DevanagariMT":
        changes = [["ङ्कृ", '\\\\glyindex"ngakadeva"\\\\glyindex"rvocalicvowelsigndeepdeva" '],
                ["ङ्क्ष",  '\\\\glyindex"ngakassadeva" '],
                #[("द्गु", '\\\\glyindex"dagadeva"\\\\rotatebox{20}{\\\\kern.068em\\\\glyindex"uvowelsignrightdeva" }\\\\kern-.16em '],
                ["द्गु", '\\\\gly270\\\\raisebox{0.6ex}{\\\\kern.18em\\\\gly431\\\\kern-.18em}'],
                ["ङ्क्ते", '\\\\glyindex"ngakatadeva"\\\\glyindex"evowelsignleftdeva" {}'],
                ["ङ्क्त", '\\\\glyindex"ngakatadeva" '],
                ["द्द्वि", '\\\\glyindex"ivowelsignnarrowdeva\\\\glyindex"dadavadeva" '],
                ["द्द्व", '\\\\glyindex"dadavadeva" '],
                ["द्व्र", '\\\\glyindex"davadeva"\\\\raisebox{0.2em}{\\\\glyindex"rastemdeepdeva"\\\\kern-.3em} '],
                ["ङ्क", '\\\\glyindex"ngakadeva" '],
                ["ङ्ग", '\\\\glyindex"ngagadeva" '],
                ["ङ्घ्य", '\\\\glyindex"ngaghadeva"\\\\glyindex"yapostformlowdeva" '],
                ["ङ्घ्रि", '\\\\glyindex"ivowelsignnarrowdeva"\\\\glyindex"ngaghadeva"\\\\glyindex"rastemdeepdeva" '],
                ["ङ्ख", '\\\\glyindex"ngakhadeva" '],
                ["त्त्र", '\\\\glyindex"taprehalfdeva"\\\\glyindex"taradeva" ']
                ]
    elif useFont == "Arial":
         changes = [["ङ्कृ", '\\\\glyindex"ngakadeva"\\\\glyindex"rvocalicvowelsigndeepdeva" '],
                ["ङ्क्ष",  '\\\\glyindex"ngakassadeva" '],
                #[("द्गु", '\\\\glyindex"dagadeva"\\\\rotatebox{20}{\\\\kern.068em\\\\glyindex"uvowelsignrightdeva" }\\\\kern-.16em '],
                ["द्गु", '\\\\gly270\\\\raisebox{0.6ex}{\\\\kern.18em\\\\gly431\\\\kern-.18em}'],
                ["ङ्क्ते", '\\\\glyindex"ngakatadeva"\\\\glyindex"evowelsignleftdeva" {}'],
                ["ङ्क्त", '\\\\glyindex"ngakatadeva" '],
                ["द्द्वि", '\\\\glyindex"ivowelsignnarrowdeva\\\\glyindex"dadavadeva" '],
                ["द्द्व", '\\\\glyindex"dadavadeva" '],
                ["द्व्र", '\\\\glyindex"davadeva"\\\\raisebox{0.2em}{\\\\glyindex"rastemdeepdeva"\\\\kern-.3em} '],
                ["ङ्क", '\\\\glyindex"ngakadeva" '],
                ["ङ्ग", '\\\\glyindex"ngagadeva" '],
                ["ङ्घ्य", '\\\\glyindex"ngaghadeva"\\\\glyindex"yapostformlowdeva" '],
                ["ङ्घ्रि", '\\\\glyindex"ivowelsignnarrowdeva"\\\\glyindex"ngaghadeva"\\\\glyindex"rastemdeepdeva" '],
                ["ङ्ख", '\\\\glyindex"ngakhadeva" '],
                ["त्त्र", '\\\\glyindex"taprehalfdeva"\\\\glyindex"taradeva" ']
                ]
    else:
        return line

    for ch in changes:
            line = re.sub(ch[0], ch[1], line)
    return line
