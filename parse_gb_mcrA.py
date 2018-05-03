#!/usr/bin/env python
"""find the corresponding 16S rRNA sequence in a genbank file for functional (mcrA) genes sequence.
DEPENDENCIES:
Biopython
"""

# load required packages

import sys
import re
from Bio import Entrez, SeqIO
from Bio.SeqRecord import SeqRecord
Entrez.email = "your.email"


## mcrA have multiple descriptions

feats = ['methyl coenzyme m reductase alpha subunit','methyl-coenzyme m reductase alpha subunit',\
         'methyl coenzyme m reductase subunit alpha','methyl-coenzyme m reductase subunit alpha','mcra'\
         'methyl-coenzyme m reductase i subunit a',\
         'methyl-coenzyme m reductase i subunit alpha']

note = {'methyl coenzyme m reductase alpha subunit','methyl-coenzyme m reductase alpha subunit',\
         'methyl coenzyme m reductase subunit alpha','methyl-coenzyme m reductase subunit alpha','mcra'\
         'methyl-coenzyme m reductase i subunit a',\
         'methyl-coenzyme m reductase i subunit alpha'}

# handle of 16S genbank files

hdin = open('LJKK01.1.gb', 'rU')
 
with open('parsed_mcrA.fasta', 'a') as hd_out:
    for rec in SeqIO.parse(hdin,'gb'):
        #print(len(rec))
        featss = set()
        for feat in rec.features:
            featss.add(feat.type)
            if feat.type == "CDS":
                if "product" in feat.qualifiers:
                    print(feat.qualifiers['product'][0].lower())
                    if feat.qualifiers['product'][0].lower().replace(",","") in feats:
                        print('Product label is %s' % feat.qualifiers['product'][0].lower())
                        seq = feat.extract(rec.seq)
                        print('Sequence length is %i' % len(seq))
                        newrecord = SeqRecord(seq, id = rec.id, description = rec.description)
                        mcrA.append(newrecord)
                        SeqIO.write(mcrA, hd_out, "fasta")
                    else:
                        print ("Not found the gene you are seaerching for")
                    print ("="*30)
                    continue
                if "gene" in feat.qualifiers:
                    if feat.qualifiers['gene'][0].lower().replace(",","") in ('mcra','mrta','mcr','mrt'):
                        print ("Indexing qualifiers with 'gene' as key and %s as \
value" % (feat.qualifiers['gene'][0].lower()))
                        seq = feature.extract(rec.seq)
                        print('Sequence length is %i' % len(seq))
                        newrecord = SeqRecord(seq, id = rec.id, description = rec.description)
                        mcrA.append(newrecord)
                        SeqIO.write(mcrA, hd_out, "fasta")
                        print ("~"*20)
                        continue
                if "note" in feat.qualifiers:
                    if feat.qualifiers['note'][0].lower().replace(",","") in note:
                        print ("Indexing qualifiers with 'note' as key and %s as \
value" % (feat.qualifiers['note'][0].lower()))
                        seq = feature.extract(rec.seq)
                        print('Sequence length is %i' % len(seq))
                        newrecord = SeqRecord(seq, id = rec.id, description = rec.description)
                        mcrA.append(newrecord)
                        SeqIO.write(mcrA, hd_out, "fasta")
                        print ("+"*25)
    print(featss)

        
hdin.close()
                        


    
