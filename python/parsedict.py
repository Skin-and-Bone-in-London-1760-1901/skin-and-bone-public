#!/usr/bin/python3

import re
import csv
import json

def findEntsRels(classified, description):

    ents = []
    rels = []
    bsidx = None
    inidx_start = None
    inidx_last = None

    #print('classified:')
    #print(classified)

    #chunki = 0;
    injidx = None;

    #for chunk in chunks:
    #    terms = getChunkTerms(chunk, classified, [], [])
        #print('terms:')
        #print(terms)
        

    for term in classified:

        #print()
        #print(term['words'])

        realword = ''

        for word in term['words']:
            realword = realword + '*' + description[word[1]:word[2]] + '*'

        loidx = term['words'][0][1]
        hiidx = term['words'][-1][2]

        #print(realword.ljust(40) + codeTypeSplit(term).ljust(4) + term['classification'].ljust(40) + '=' + term['regularised'].ljust(40), end='')

        #if 'subjects' in term:
        #    print(' +' + '|'.join(term['subjects']).ljust(30), end='')
  

        #if term['classification'] == 'single capital letter':

            # store up single capital letters

        #    if inidx_start == None:

        #        inidx_start = loidx

        #    inidx_last = hiidx


        #if term['regularised'] == 'full stop' and inidx_start != None:

        #    inidx_last = hiidx


        #if term['classification'] != 'single capital letter' and term['regularised'] != 'full stop':

        #    if inidx_start != None:

                # Spacy doesn't like TATTOOINITIALS
                #ents.append((inidx_start, inidx_last + 1, 'TATTOOINITIALS'));

         #       inidx_start = None
         #       inidx_last = None

        if term['classification'] == 'injury':

            injidx = len(ents)
            ents.append((loidx, hiidx, 'INJURY'));
            

        if term['classification'] == 'injury postscript':

            # injidx = len(ents) # Because this a postscript we do not set it as the current injury to be copied forward.
            injidx = None # In fact we cancel any current injury being copied forward
            # Let's find the index of most recent bodylocation ent so that we can postscript this injury to it
            bodyentidx = None
            for entidx, ent in reversed(list(enumerate(ents))):
                if ent[2] == 'BODYLOCATION':
                    bodyentidx = entidx
                    break

            if bodyentidx != None:

                #print('candidate: ' + str((len(ents) - 1)))
                #print('bodyentidx: ' + str(bodyentidx))
                # Now we need to delete any rels already linked to this bodylocation ent because they are wrong
                for relidx, rel in reversed(list(enumerate(rels))):
                    if rel[1] == bodyentidx:
                        #print('I think rel ' + str(relidx) + ' is wrong')
                        rels.pop(relidx)
                        break
                # Instead we need to delete the previous rel if it exists because it is probably wrong.
                #if len(rels) > 0:
                #    rels.pop()
                # And attach this injury to the previous bodylocation.
                rels.append((len(ents), bodyentidx, 'INJURYBODY'))
                ents.append((loidx, hiidx, 'INJURY'));

            else:

                # Perhaps we can link the injury to the most recent cause
                causeentidx = None
                for entidx, ent in reversed(list(enumerate(ents))):
                    if ent[2] == 'CAUSE':
                        causeentidx = entidx
                        break

                if causeentidx != None:

                    #print('candidate: ' + str((len(ents) - 1)))
                    #print('bodyentidx: ' + str(bodyentidx))
                    # Now we need to delete any rels already linked to this bodylocation ent because they are wrong
                    for relidx, rel in reversed(list(enumerate(rels))):
                        if rel[1] == causeentidx:
                            #print('I think rel ' + str(relidx) + ' is wrong')
                            rels.pop(relidx)
                            break
                    # Instead we need to delete the previous rel if it exists because it is probably wrong.
                    #if len(rels) > 0:
                    #    rels.pop()
                    # And attach this injury to the previous bodylocation.
                    rels.append((len(ents), causeentidx, 'INJURYCAUSE'))
                    ents.append((loidx, hiidx, 'INJURY'));

                else:

                    # If we do not have a recent body or cause entity, let's at least append this to the output as an injury ent
                    ents.append((loidx, hiidx, 'INJURY'));


        if (term['classification'] == 'mark' or
            term['classification'] == 'design' or
            term['classification'] == 'tattoo mark' or
            term['classification'] == 'single capital letter'):

            injidx = None

        #if term['classification'] == 'written words':

        #    ents.append((loidx, hiidx, 'TATTOOWORDS'));

        #if term['classification'] == 'all caps' or term['classification'] == 'given name male' or term['classification'] == 'given name female':

        #    ents.append((loidx, hiidx, 'TATTOOWORDS'));

        #if term['classification'] == 'design':

        #    ents.append((loidx, hiidx, 'DESIGN'));

        #if term['classification'] == 'tattoo mark':

        #    ents.append((loidx, hiidx, 'TATTOOMARK'));

        #if term['classification'] == 'mark':

        #    ents.append((loidx, hiidx, 'MARK'));
 
        if term['classification'] == 'hanging body specifier':

            ents.append((loidx, hiidx, 'HANGINGBODYSPECIFIER'));


        if term['classification'] == 'body':

            if bsidx != None:

                if injidx != None:
                    rels.append((injidx, len(ents), 'INJURYBODY'))
                ents.append((bsidx, hiidx, 'BODYLOCATION'));


            else:

                if injidx != None:
                    rels.append((injidx, len(ents), 'INJURYBODY'))
                ents.append((loidx, hiidx, 'BODYLOCATION'));

        if term['classification'] == 'body specifier':

            # store up body specifiers

            if bsidx == None:

                bsidx = loidx


        if term['classification'] == 'cause':

            if injidx != None:
                rels.append((injidx, len(ents), 'INJURYCAUSE'))
            ents.append((loidx, hiidx, 'CAUSE'));

        else:

            bsidx = None;

        #print()
    #chunki += 1;

    return ents, rels

def prettyEntsRels(ents, rels, description):

    print()
    print(description)
    print()

    #for ent in ents:
    #    print(str(ent) + '**' + description[ent[0]:ent[1]] + '**')
    #print() 

    if (rels):

        for rel in rels:
            injuryent = ents[rel[0]]
            bodyent = ents[rel[1]]
            print(str(rel) + str(injuryent) + '**' + description[injuryent[0]:injuryent[1]] + '**' + ' --> ' + str(bodyent) + '**' + description[bodyent[0]:bodyent[1]] + '**')


def prettyEnts(ents, description):
    if ents:
        for ent in ents:
            print(str(ent) + '**' + description[ent[0]:ent[1]] + '**')

def hasInjury(classified):
    for term in classified:
        if term['classification'] == 'injury': return True
        if term['classification'] == 'injury postscript': return True
    return False

def hasCause(classified):
    for term in classified:
        if term['classification'] == 'cause': return True
    return False

def prettyClassified(classified):
    for term in classified:
        print(term)
        #print(' '.join(term['words']).ljust(40) + codeTypeSplit(term).ljust(4) + term['classification'].ljust(40) + '=' + term['regularised'].ljust(40), end='')
        #if 'subjects' in term:
        #    print(' +' + '|'.join(term['subjects']).ljust(30), end='')
        #print()

#print("loading terms")

terms = []
terms_encountered = {}

# read the terms from from terms.tsv
with open('data/lookups/terms.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    commented = False
    for idx, row in enumerate(reader):
        if idx > 1: # skip out the header rows
            if len(row) == 0:
                pass # blank row
            elif len(row) == 1:
                if row[0] == '/*':
                    commented = True
                if row[0] == '*/':
                    commented = False
            elif commented:
                pass
            elif row[0].startswith('##'):
                pass
            elif len(row) == 3 or len(row) == 4 or len(row) == 5:
                if len(row[0]) > 0:
                    term = {}
                    try:
                        term['words'] = json.loads(row[0])
                    except ValueError:
                        print('json not valid at line ' + str(idx + 1))
                        exit(1)
                    if str(term['words']) in terms_encountered:
                        print('repeated words at line ' + str(idx + 1) + ' : "' + str(term['words']) + '" (' + str(row) + ') . Original at line ' + str(terms_encountered[str(term["words"])]) + '. ')
                        exit(1)
                    terms_encountered[str(term['words'])] = str(idx + 1)
                    term['words'] = [i.lower() for i in term['words']]
                    regularised = row[1]
                    if regularised == '':
                        regularised = ' '.join(term['words'])
                    term['regularised'] = regularised
                    term['classification'] = row[2]
                    if (len(row) == 4 or len(row) == 5) and len(row[3]) > 1:
                        term['subjects'] = row[3].split(' ')
                    terms.append(term)
            else:
                print('wrong number of columns at line ' + str(idx + 1) + "(" + str(len(row)) + ")")
                exit(1)

# sort the terms so those with more words are evaluated first
list.sort(terms, key=lambda x : len(x['words']), reverse=True)

#print("loading given names")

givens = {}

# read the givens from from gender.tsv
with open('data/lookups/gender.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        givens[row[0]] = row[1]

split = [',', ';', '"', '(', ')', '<', '>', '[', ']', ':', '-', '.']

def wordsplit(s):
  l = []
  b = ''
  for idx, c in enumerate(s):
    if c == ' ':
      if len(b) > 0:
        l.append((b, idx - len(b), idx))
      b = ''
    elif c in split:
      if len(b) > 0:
        l.append((b, idx - len(b), idx))
      l.append((c, idx - len(c), idx))
      b = ''
    else:
      b = b + c
  if len(b) > 0:
    l.append((b, idx - len(b), idx))
  return l

def classify(line):
    classified = []
    line_idx = 0
    while line_idx < len(line):
        word = line[line_idx][0]
        unknown = True
        for term_idx, term in enumerate(terms):
            if len(term["words"]) <= (len(line) - line_idx): # avoid out of range errors

                extract = line[line_idx:(line_idx + len(term["words"]))]

                # The current regularising we do is to convert to lower case.
                # Any classification which needs case needs to be done before this stage.
                # The terms file must not contain upper case.

                extract_regularised = [i[0].lower() for i in extract]

                if extract_regularised == term["words"]:
                    classified_term = { "words": extract, 'regularised': term['regularised'], 'classification': term['classification']}
                    if 'subjects' in term:
                        classified_term['subjects'] = term['subjects']
                    classified.append(classified_term)
                    unknown = False
                    line_idx += len(term["words"]) - 1
                    break

        if unknown:
            if len(word) > 1 and re.match('^[A-Z]+$', word):
                classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'all caps', 'subjects': ['namesinitials']})
                unknown = False
            #elif re.match('^[A-HJ-Z]$', word) and word != 'A':
            elif re.match('^[A-Z]$', word):
                classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'single capital letter', 'subjects': ['namesinitials']})
                unknown = False
            elif re.match('^[0-9][0-9]$', word):
                classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'two digit number'})
                unknown = False
            elif re.match('^[0-9][0-9][0-9]$', word):
                classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'three digit number'})
                unknown = False
            elif re.match('^[0-9][0-9][0-9][0-9]$', word):
                year = int(word)
                if year > 1750 and year < 1950:
                    classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'year', 'subjects': ['year']})
                else:
                    classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'four digit number'})
                unknown = False
            elif word.lower() in givens:
                if givens[word.lower()] == 'm':
                    classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'given name male', 'subjects': ['namesinitials']})
                else:
                    classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'given name female', 'subjects': ['namesinitials']})
                unknown = False
            elif len(classified) > 0 and classified[len(classified) - 1]['classification'].startswith('given name'):
                classified.append({ "words": [line[line_idx]], 'regularised': word, 'classification': 'possible surname', 'subjects': ['namesinitials']})
                unknown = False

        if unknown:
            classified.append({ 'words': [line[line_idx]], 'regularised': 'unknown', 'classification': 'unknown'})
        line_idx += 1
    return classified

# This function creates a set of entities and relationships from a cleaned text description
# using a dictionary and some simple logic.
# The dictionary file is data/lookups/terms.tsv

def parsedict(description):
   
    line = wordsplit(description) # split the words in the description into a list
    classified = classify(line)

    #if description == 'gun shot wounds.':
    #    print(description)
    #    print(classified)
    #    exit(1)

    if hasInjury(classified) or hasCause(classified):

        #prettyClassified(classified)
        ents, rels = findEntsRels(classified, description)
        #prettyEntsRels(ents, rels, description)

        return ents, rels

    return None, None

