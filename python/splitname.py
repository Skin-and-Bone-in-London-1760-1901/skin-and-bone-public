#!/usr/bin/python3

import re

def splitname(name):

    # Remove contents of parenthesis
    pname = re.sub("\(.*?\)", "", name)

    pname = pname.strip()

    names = pname.split()

    if ('alias ' in pname):
        #print()
        #print('ALIAS')
        #print(name)
        pname = pname.split('alias ', 1)[0]
        #print(pname)
        return splitname(pname)

    elif (' or ' in pname):
        #print()
        #print('OR')
        #print(name)
        pname = pname.split(' or ', 1)[0]
        #print(pname)
        return splitname(pname)

    elif ('& Child' in pname):
        #print()
        #print('& CHILD')
        #print(name)
        pname = pname.split('& Child', 1)[0]
        #print(pname)
        return splitname(pname)

    elif (len(names) == 2):

        return names[0], names[1]

    elif (len(names) == 3):

        # We assume a middle name or initial has been given
        return ' '.join(names[:-1]), names[-1]

    elif (len(names) > 3):

        # We assume extra detail has been given
        # so we assume the given name and surname are at least the first two words
        #print()
        #print('EXTRA DETAIL')
        #print(names[0], names[1])
        return names[0], names[1]

    elif (len(names) == 1):

        # We only have a single word
        # so we return it for both given and surname
        return names[0], names[0]

    else:
        print()
        print(name)
        print(pname)
        print('UNKNOWN PROBLEM')
        return name, name
    

