## vcf_extract.py ##
## extract Ref: T - Alt: C and Ref: A - Alt: G ##
## zhang fei <zhangfei-123@foxmail.com> ##
## 2019-12-18 ##

import re

fl_clinvar = ".\data\clinvar_20191202.vcf"

res_clinvar_filter = [['ID', 'CHROM', 'POS', 'REF', 'ALT', 'INFO']]
res_clinvar_filter_bed = []
with open(fl_clinvar, 'r') as fh_clinvar:
    for line in fh_clinvar:
        if line[0] != "#":
            line = line.strip('\r\n').split('\t')
            ID, chrom, pos, ref, alt, info = line[2], line[0], line[1], line[3], line[4], line[7]
            if (ref == 'T' and alt == 'C') or (ref == 'A' and alt == 'G'):
                res_clinvar_filter.append([ID, chrom, pos, ref, alt, info])
                res_clinvar_filter_bed.append([chrom, str(int(pos) - 31), str(int(pos) + 30), ID])
    print(len(res_clinvar_filter))

with open(".\\res\clinvar_20191202_filter.txt", 'w') as fh_output:
    res_clinvar_filter = ['\t'.join(i) for i in res_clinvar_filter]
    fh_output.write('\n'.join(res_clinvar_filter))

with open(".\\res\clinvar_20191202_filter.bed", 'w') as fh_output:
    res_clinvar_filter_bed = ['\t'.join(i) for i in res_clinvar_filter_bed]
    fh_output.write('\n'.join(res_clinvar_filter_bed))
