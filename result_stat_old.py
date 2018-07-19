## result_stat.py ##
## Summary locus freq at each site ##
## Zhang Fei ##
## 2017-11-16 ##

import sys

fh_seq = open(sys.argv[1], 'r')
seq_length = sys.argv[2]
fh_out = open(sys.argv[3], 'a')

def frq_by_locus(seq_length, fh_seq):
    result = []
    for i in range(0, int(seq_length)):
        dic = {'A':0, 'T':0, 'C':0, 'G':0, 'N':0}
        result.append(dic)
    seq_right = fh_seq.read()
    seq_right = seq_right.strip('\n')
    seq_right = seq_right.split('\n')
    fh_seq.close()
    for line in seq_right:
        i = 0
        for nuc in line:
            if result[i].get(nuc) is not None:
                result[i][nuc] += 1
            i += 1
    return result

result = frq_by_locus(seq_length, fh_seq)
fh_out.writelines('\t'.join(['locus', 'A', 'T', 'C', 'G', 'N']))
fh_out.writelines('\n')

i = 1
for line in result:
    output = [str(i), str(line['A']), str(line['T']), str(line['C']), str(line['G']), str(line['N'])]
    fh_out.writelines('\t'.join(output))
    fh_out.writelines('\n')
    i += 1
fh_out.close()
