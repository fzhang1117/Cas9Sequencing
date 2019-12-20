## clinvar_editor_search.py ##
## zhang fei <zhangfei-123@foxmail.com> ##
## 2019-12-18 ##

from itertools import islice
import re

def func_seq_complement(seq):
    seq = seq.upper()
    seq = seq[::-1]
    seq = seq.replace('A', 't')
    seq = seq.replace('C', 'g')
    seq = seq.replace('G', 'c')
    seq = seq.replace('T', 'a')
    seq = seq.upper()
    return seq

## BE3 window, -17: -13, length = 5, NGG, greedy
## for example: func_general_greedy_editor_search_NGG(seq, -13, -17)
def func_general_greedy_editor_search_NGG(seq, start, end):
    mutant_locus = 30
    start_NGG = [m.start() for m in re.finditer(r'(?=([ATCG]GG))', seq)]
    window_start = [i - (-end) for i in start_NGG]
    window_end = [i - (-start) for i in start_NGG]
    for i, j in zip(window_start, window_end):
        if i >= 0 and j >= 0:
            if mutant_locus >= i and mutant_locus <= j:
                seq_window = seq[i: j + 1]
                Tcount_window = seq_window.count('T')
                if Tcount_window == 1:
                    return('precise edit')
            else:
                continue
        else:
            continue
    return('not precise edit')

def func_out_editor_search(seq):
    mutant_locus = 30
    locus_search_1 = [m.start() for m in re.finditer(r'(?=(T[ATCG]{17}[ATCG]G))', seq)]
    locus_search_2 = [m.start() for m in re.finditer(r'(?=([ACG]T[ATCG]{16}[ATCG]G))', seq)]
    locus_search_3 = [m.start() for m in re.finditer(r'(?=(T[ACG]{2}[ATCG]{16}[ATCG]G))', seq)]
    if locus_search_1.count(mutant_locus) == 1:
        return('precise edit')
    elif locus_search_2.count(mutant_locus) == 1:
        return('precise edit')
    elif locus_search_3.count(mutant_locus) == 1:
        return('precise edit')
    else:
        return('not precise edit')

fl_clinvar_vcf = ".\\res\clinvar_20191202_filter.txt"
fl_clinvar_fasta = ".\\res\clinvar_20191202_filter.fasta"

dic_clinvar = {}
with open(fl_clinvar_vcf, 'r') as fh_clinvar_vcf:
    for line in islice(fh_clinvar_vcf, 1, None):
        line = line.strip('\n').split('\t')
        ID = line[0]
        dic_clinvar[ID] = line

with open(fl_clinvar_fasta, 'r') as fh_clinvar_fasta:
    identitor, fasta = '', ''
    for line in fh_clinvar_fasta:
        line = line.strip('\n')
        if line[0] == '>':
            identitor = line[1:]
        else:
            if line[30] == 'T':
                dic_clinvar[identitor] = dic_clinvar[identitor] + [line]
            else:
                dic_clinvar[identitor] = dic_clinvar[identitor] + [func_seq_complement(line)]
print(dic_clinvar['256794'])

res = [['ID', 'CHROM', 'POS', 'REF', 'ALT', 'CLNSIG', 'our_editor', 'BE3', 'nCDA1_BE3', 'cCDA1_BE3', 'A3A_BE3', 'INFO', 'flanking_seq']]
for key in dic_clinvar.keys():
    seq = dic_clinvar[key][6]
    info = dic_clinvar[key][5]
    #print(info)
    clnsig = info.split('CLNSIG=')
    if len(clnsig) > 1:
        clnsig = clnsig[1].split(';')[0]
    else:
        clnsig = ''
    edit_BE3 = func_general_greedy_editor_search_NGG(seq, -13, -17)
    edit_nCDA1_BE3 = func_general_greedy_editor_search_NGG(seq, -14, -20)
    edit_cCDA1_BE3 = func_general_greedy_editor_search_NGG(seq, -16, -19)
    edit_A3A_BE3 = func_general_greedy_editor_search_NGG(seq, -15, -16)
    edit_our_editor = func_out_editor_search(seq)
    res.append(dic_clinvar[key][0: 5] + [clnsig, edit_our_editor, edit_BE3, edit_nCDA1_BE3, edit_cCDA1_BE3, edit_A3A_BE3, dic_clinvar[key][5], dic_clinvar[key][6]])

with open(".\\res\\result.txt", 'w') as fh_output:
    res = ['\t'.join(i) for i in res]
    fh_output.write('\n'.join(res))
