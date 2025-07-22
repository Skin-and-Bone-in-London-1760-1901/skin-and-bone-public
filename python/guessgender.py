#!/usr/bin/python3

import csv

givens = {}
expansions = {}

# read the givens from from gender.tsv
with open('data/lookups/gender.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        givens[row[0]] = row[1]

# read the expansions from from expansions.tsv
with open('data/lookups/expansions.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        if len(row) > 1:
            expansions[row[0]] = row[1]

def guessgender(given):

    key = given.lower().strip()

    if ' ' in key:
        key = key.split()[0]

    if key in expansions:

        key = expansions[key]

    if key in givens:

        return givens[key]

    else:

        pass
        #print('failed to guess gender: ***' + given + '***' + key + '***')
        #exit(1)

        return 'u'

