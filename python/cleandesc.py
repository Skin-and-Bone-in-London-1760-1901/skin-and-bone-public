#!/usr/bin/python3

import re

# This function cleans a description, making it suitable to be passed to parsedict, getspacytokens and makeprodigy.

def cleandesc(description):

    # replace weird funky quotes
    description = description.replace('“', '"') 
    description = description.replace('”', '"')
    description = description.replace('’', "'")
    description = description.replace('„', '"')
    description = description.replace("''", '"')
    # try to replace single quotes which are definitely not apostrophes with double quotes
    description = re.sub(r"([ ,\.ABCDEFGHIJKLMNOPQRSUVWXYZ])'([ ,\.ABCDEFGHIJKLMNOPQRUVWXYZ])", r'\1"\2', description)

    # what do dashes do for us? Nothing
    description = description.replace('-', ' ')
    # regularise the appearance of F. S. so we can pick it up and discard it during classification
    description = description.replace('F. S.', 'F.S.')
    #description = description.replace('T. S.', 'T.S.')
    #description = description.replace('T. L.', 'T.L.')
    description = description.replace('F. C.', 'F.C.')
    # remove the meaningless abbreviations from the start of the description
    if description.startswith('F.S.') or description.startswith('F.C.'):
        description = description[4:]
    # strip leading and following whitespace
    description = description.strip()
    # fix very specific OCR errors
    #if subrecordid == 'rhc48132':
    #    description = description.replace('two . birds', 'two birds')
    # remove the weird angle brackets and brackets
    description = description.replace('<[X:', '')
    description = description.replace('<[U:', '')
    description = description.replace('<[R:', '')
    description = description.replace('<[', '')
    description = description.replace(']>', '')
    # regularise left and right abbreviations
    description = re.sub(r"([ \",;]|^)l\.?([ ,;\"]|$)", r"\1left\2", description)
    description = re.sub(r"([ \",;]|^)r\.?([ ,;\"]|$)", r"\1right\2", description)
    description = re.sub(r"([ \",;]|^)lt\.?([ ,;\"]|$)", r"\1left\2", description)
    description = re.sub(r"([ \",;]|^)It\.?([ ,;\"]|$)", r"\1left\2", description)
    description = re.sub(r"([ \",;]|^)rt\.?([ ,;\"]|$)", r"\1right\2", description)
    description = re.sub(r"([ \",;]|^)Rt\.?([ ,;\"]|$)", r"\1right\2", description)
    # regularise scar abbreviations
    description = re.sub(r"([ \",;]|^)sc\.?([ ,;\"]|$)", r"\1scar\2", description)
    description = re.sub(r"([ \",;]|^)scs\.?([ ,;\"]|$)", r"\1scars\2", description)
    # regularise dot abbreviations
    description = re.sub(r"([ \",;]|^)d\.?([ ,;\"]|$)", r"\1dot\2", description)
    # regularise ampersands
    description = re.sub(r"([ \",;]|^)&([ ,;\"]|$)", r"\1and\2", description)
    # replace dashes with spaces. Bold I know.
    description = description.replace("—", " ")
    description = description.replace("-", " ")
    # make description always end with a full stop
    if len(description) > 0:
        if description.endswith(','):
            description = description[:-1] + '. '
        elif not description.endswith('.'):
            description = description + '. '
 
    return description 

