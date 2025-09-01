'''
veltview.py
'''

import re


def velthview(line):
    '''
    Input is a line in IAST, output is a version in Velthuis
    '''
    subdict = {
        "ā": "aa",
        "'": ".a",
        "ī": "ii",
        "ū": "uu",
        "ṛ": ".r",
        "r̥": ".r",
        "ṝ": ".R",
        "\\\d{\\\=r}": ".R",
        "ḷ": ".l",
        "l̥": ".l",
        "ḹ": ".L",
        "\\\d{\\\=l}": ".L",
        "ṅ": '"n',
        "ñ": "~n",
        "ṭ": ".t",
        "ḍ": ".d",
        "ṇ": ".n",
        "ś": '"s',
        "ṣ": ".s",
        "ṃ": ".m",
        "ṁ": ".m",
        "ḥ": ".h",
        "Ó": ".o",
        "°": "@",
    }
    for change in subdict:
        line = re.sub(change, subdict[change], line)
    return line
