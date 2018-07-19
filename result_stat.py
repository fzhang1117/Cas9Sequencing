## result_stat.py ##
## Summary locus freq at each site and freq of edit product ##
## Zhang Fei ##
## 2017-11-16 ##

import sys

#fh_seq = open(sys.argv[1], 'r')
#seq_length = sys.argv[2]
#fh_out = open(sys.argv[3], 'a')

fl_seq = sys.argv[1]
seq_length = sys.argv[2]
fl_edit_site = sys.argv[3]
fl_out_site = sys.argv[4]
fl_out_product = sys.argv[5]

with open(fl_seq, 'r') as fh_seq:
    seq_info = []
    for line in fh_seq:
        seq_info.append(line.strip('\n'))

def frq_by_locus(seq_length, seq_info):
    result = []
    for i in range(0, int(seq_length)):
        dic = {'A':0, 'T':0, 'C':0, 'G':0, 'N':0}
        result.append(dic)
    for line in seq_info:
        i = 0
        for nuc in line:
            if result[i].get(nuc) is not None:
                result[i][nuc] += 1
            i += 1
    return result

def frq_edit_product(fl_edit_site, seq_info):
    with open(fl_edit_site, 'r') as fh_edit_site:
        loci_pattern = []
        loci_pam = []
        for line in fh_edit_site:
            line = line.strip('\r\n').split('\t')
            loci_pattern.append(int(line[0]))
            loci_pam.append(line[1])
    dic_edit_product = {}
    for line in seq_info:
        key_temp = [list(line)[i] for i in loci_pattern]
        key = '-'.join([key_temp[i] + '(' + loci_pam[i] + ')' for i in range(0, len(key_temp))])
        if dic_edit_product.get(key) is None:
            dic_edit_product[key] = 1
        else:
            dic_edit_product[key] += 1
    return dic_edit_product

result = frq_by_locus(seq_length, seq_info)
output_frq_locus = ['\t'.join(['locus', 'A', 'T', 'C', 'G', 'N'])]
dic_edit_product = frq_edit_product(fl_edit_site, seq_info)
result_edit_product = sorted(dic_edit_product.items(), key = lambda item:item[1], reverse = True)

i = 1
for line in result:
    entry = [str(i), str(line['A']), str(line['T']), str(line['C']), str(line['G']), str(line['N'])]
    output_frq_locus.append('\t'.join(entry))
    i += 1

with open(fl_out_site, 'w') as fh_out_site:
    fh_out_site.write('\n'.join(output_frq_locus))

with open(fl_out_product, 'w') as fh_out_product:
    output_product = [i[0] + '\t' + str(i[1]) for i in result_edit_product]
    fh_out_product.write('\n'.join(output_product))
