## python script to get organims names from organism names from genbank file
## Sizhong Yang, 2015-3-17

## Part 1, Example to get organism names from genbank file

from Bio import SeqIO

fh = open('example.gb','r')
wr = open("hit_sp_names.txt","w")
for gb_record in SeqIO.parse(fh,'genbank'):
    acc = gb_record.annotations['accessions'][0]
    organism = gb_record.annotations['organism']
    tax_line = ("; ").join(gb_record.annotations['taxonomy'])
    wr.write(organism+"\n")
fh.close()
wr.close()


## Part 2, Example to get accession number for fasta file headline

from Bio import SeqIO

with open("accs.txt","a") as f:
    for i in SeqIO.parse(open("your.fasta","rU"), "fasta"):
        head = i.id
        f.write("%s\n" % head)

f.close()
