# Given the accession numbers are line by line stored in 'idList.txt' 
# And you have genbank records in the file of file.genbank
# e.g. ACCESSION AB000106
# ORGANISM Sphingomonas sp. Bacteria; Proteobacteria; Alphaproteobacteria;Sphingomonadales; Sphingomonadaceae; Sphingomonas.
# Assuming you have BioPython installed, one possible solution:
# Sizhong, 2015-8-16



from Bio import SeqIO

# Read accession numbers and put into a list

accession_numbers = [line.strip() for line in open('idList.txt')]

# Iterate over each genbank record.
fh = open('file.genbank') 

with open('output.txt','w') as f:
    for record in SeqIO.parse(fh,'genbank'):
        acc = record.annotations['accessions'][0] # annotation is dict
        organism = record.annotations['organism']
        taxonomy = (";").join(record.annotations['taxonomy'])
        if acc in accession_numbers:
            f.write('%s\t%s\t%s\n' %(acc, organism, taxonomy))
        else:
            pass

# close handle
fh.close()
