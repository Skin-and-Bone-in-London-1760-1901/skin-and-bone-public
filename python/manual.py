
import json

manuals = {}

# read the manual annotations from the dhi-annotator exported file:
with open('../dhi-annotator/data/output/skinandbone.jsonl', 'r') as json_file:
    json_list = list(json_file)


def spans_to_tuples(spans):
    tuples = []
    for span in spans:
        tuples.append((span['start'], span['end'], span['label']))
    return tuples


def rels_to_tuples(rels):
    tuples = []
    for rel in rels:
        tuples.append((rel['head'], rel['child'], rel['label']))
    return tuples


for json_str in json_list:
    anno = json.loads(json_str)

    # We need to alter the structure of the spans and rels to tuples
    manuals[anno['uid']] = { 'ents': spans_to_tuples(anno['spans']), 'rels': rels_to_tuples(anno['rels']) }


def manual(descid):
    if descid in manuals:
        #print('hit')
        anno = manuals[descid]
        return anno['ents'], anno['rels']
    else:
        return False, False
