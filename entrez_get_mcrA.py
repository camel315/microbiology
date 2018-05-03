#!/usr/bin/env python

#sript to query and download mcrA sequences according to accession numers by using Entrez
#Sizhong Yang, 2015-2-26

"""retriez the mcrA genes sequence by Entrez for a series of accession numbers.
DEPENDENCIES:
Biopython
"""
import sys
import re
import time
from Bio import Entrez, SeqIO
from Bio.SeqRecord import SeqRecord


Entrez.email = "your_email"


accnos = open("your_accession_list_file","r")

feats = ["methyl coenzyme m reductase alpha subunit","methyl-coenzyme m reductase alpha subunit",\
         "methyl coenzyme m reductase subunit alpha","methyl-coenzyme m reductase subunit alpha","mcra"\
         "methyl-coenzyme m reductase i subunit a",\
         "methyl-coenzyme m reductase i subunit alpha"]

note = {"methyl coenzyme m reductase alpha subunit","methyl-coenzyme m reductase alpha subunit",\
         "methyl coenzyme m reductase subunit alpha","methyl-coenzyme m reductase subunit alpha","mcra"\
         "methyl-coenzyme m reductase i subunit a",\
         "methyl-coenzyme m reductase i subunit alpha"}


with open("retrieved_mcrA.fasta", "a") as hd_out:
    for n, name in enumerate(accnos):
        queryterm = name.strip("\n") 
        hd1 = Entrez.esearch(db = "nucleotide", term = queryterm)
        rd1 = Entrez.read(hd1)
        hd1.close()
        #print(rd1["IdList"])
        hd2 = Entrez.efetch("nucleotide", id = rd1["IdList"], rettype="gb", retmode="text")
        gbank = SeqIO.read(hd2,"gb")
        hd2.close()
        #print("gbank is in %s format with %i features" % (type(gbank),len(gbank.features)))
        for feature in gbank.features:            
            mcrA = []
            if feature.type == "CDS":
                if "product" in feature.qualifiers:
                    if feature.qualifiers["product"][0].lower().replace(",","") in feats:
                        #[0] get first element of list, to lower case, and replace function to remove any comma
                        print("Product label is %s" % feature.qualifiers["product"][0].lower())
                        seq = feature.extract(gbank.seq)
                        print("Sequence length is %i" % len(seq))
                        newrecord = SeqRecord(seq, id = gbank.id, description = gbank.description)
                        mcrA.append(newrecord)
                        SeqIO.write(mcrA, hd_out, "fasta")
                        continue
                if "gene" in feature.qualifiers:
                    if feature.qualifiers["gene"][0].lower().replace(",","") in ("mcra","mrta","mcr","mrt"):
                        #print ("Indexing qualifiers with "gene" as key and %s as \
value" % (feature.qualifiers["gene"][0].lower()))
                        seq = feature.extract(gbank.seq)
                        print("Sequence length is %i" % len(seq))
                        newrecord = SeqRecord(seq, id = gbank.id, description = gbank.description)
                        mcrA.append(newrecord)
                        SeqIO.write(mcrA, hd_out, "fasta")
                        continue
                if "note" in feature.qualifiers:
                    if feature.qualifiers["note"][0].lower().replace(",","") in note:
                        print ("Indexing qualifiers with "note" as key and %s as \
value" % (feature.qualifiers["note"][0].lower()))
                        seq = feature.extract(gbank.seq)
                        print("Sequence length is %i" % len(seq))
                        newrecord = SeqRecord(seq, id = gbank.id, description = gbank.description)
                        mcrA.append(newrecord)
                        SeqIO.write(mcrA, hd_out, "fasta")
 
accnos.close()    
