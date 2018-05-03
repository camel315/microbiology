# -*- coding: utf-8 -*-
# script to sort fasta file by sequence length
# Sizhong, 2014-12-10

from Bio import SeqIO

#Get the lengths and ids, and sort on length

hin = open("your.fasta", "rU")

len_plus_ids = sorted((len(rec), rec.id) for rec in SeqIO.parse(hin,"fasta"))

ids = reversed([id for (length, id) in len_plus_ids])
print(type(ids))
del len_plus_ids # remve this from memory
record_index = SeqIO.index("ls_orchid.fasta", "fasta")

# write out sorted fasta

handle = open("sorted_your.fasta", "w")
for i in ids:
    handle.write('%s\n' % record_index.get_raw(i))

handle.close()
hin.close()



