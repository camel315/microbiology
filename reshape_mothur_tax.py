## script to reshape taxonomy info of OTU table (i.e. create.database by Mothur)
## Sizhong, 2016-04-25

import re

hin = open("xx.txt",'r')

hout = open('xx_reshaped.txt','w')

with hout as f:
    for line in hin:
        line = re.sub(r"\(\d+\)", "", line) # remove numeric values in parenthesis
        lst = re.sub(r";", "\t", line) # replace semiclone with tab (for taxonomy)
        f.write("%s" % lst)
    

hin.close()
hout.close()
