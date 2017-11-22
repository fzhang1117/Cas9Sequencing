## locus_search.py ##
## Search and summary aim locus ##
## Zhang Fei ##
## 2017-11-22 ##

import sys

fh_extract = open(sys.argv[1], 'r')

def seq_dic_build(fh):
    dic = {}
    for line in fh:
        line = line.strip('\n')
        line = line.split(' ')
        if dic.get(line[0]) is None:
            dic[line[0]] = line[1]
