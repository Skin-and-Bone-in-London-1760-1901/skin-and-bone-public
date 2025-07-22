#!/usr/bin/python3

# This function creates a very minimal json of the relationships for the dp_desc file.

def makedigest(description, ents, rels):

    injury = False
    digest = []

    linked_ents = [];

    if rels:
        for head, child, label in rels:

            if head != None and child != None:    

                relation = []

                headent = ents[head]
                childent = ents[child]

                relation.append(description[headent[0]:headent[1]])
                relation.append(description[childent[0]:childent[1]])
                relation.append(label)

                linked_ents.append(headent)
                linked_ents.append(childent)

                digest.append(relation)

    # Let's make sure we process any unlinked ents
    if ents:

        for ent in ents:

            if ent[2] == 'INJURY':

                injury = True

                if ent not in linked_ents:

                    relation = []
                    relation.append(description[ent[0]:ent[1]])
                    relation.append('INJURY')
                    digest.append(relation)

            if ent[2] == 'CAUSE':

                if ent not in linked_ents:

                    relation = []
                    relation.append(description[ent[0]:ent[1]])
                    relation.append('CAUSE')
                    digest.append(relation)

            if ent[2] == 'BODYLOCATION':

                if ent not in linked_ents:

                    relation = []
                    relation.append(description[ent[0]:ent[1]])
                    relation.append('BODYLOCATION')
                    digest.append(relation)

    return injury, digest

