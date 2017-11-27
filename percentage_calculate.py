# percentage_calculate.py ##
## Zhang Fei ##
## 2017-11-27 ##

from __future__ import division
from itertools import islice
import sys

mode = sys.argv[1]

fh_length = open("./fl_result/fq_length.txt", 'r')

def length_dic_build(fh):
    dic = {}
    for line in fh:
        line = line.strip('\n')
        line = ' '.join(line.split())
        line = line.split(' ')
        if dic.get(line[1]) is None:
            dic[line[1]] = int(line[0]) / 4
    fh.close()
    return dic

length_dic = length_dic_build(fh_length)

for line in length_dic.keys():
    fl_base = line.strip('\n')
    fl_base = fl_base.strip('.fq')
    ## calculate ATCGN percentage in each position
    fl_summary = './fl_result/summary/' + fl_base + '_summary.txt'
    fh_summary = open(fl_summary, 'r')
    fh_summary_out = open('./fl_result/result/summary/' + fl_base + '_summary.txt', 'a')
    title_summary = ['locus', 'A.num', 'T.num', 'C.num', 'G.num', 'T.num', 'in total',  'A.per', 'T.per', 'C.per', 'G.per', 'N.per']
    fh_summary_out.writelines('\t'.join(title_summary))
    fh_summary_out.writelines('\n')
    for line2 in islice(fh_summary, 1, None):
        line2 = line2.strip('\n')
        line2 = line2.split('\t')
        A_num = int(line2[1]) / length_dic[line]
        T_num = int(line2[2]) / length_dic[line]
        C_num = int(line2[3]) / length_dic[line]
        G_num = int(line2[4]) / length_dic[line]
        N_num = int(line2[5]) / length_dic[line]
        output = line2 + [str(length_dic[line])] + [str(A_num), str(T_num), str(C_num), str(G_num), str(N_num)]
        fh_summary_out.writelines('\t'.join(output))
        fh_summary_out.writelines('\n')
    fh_summary_out.close()
    fh_summary.close()
    
    ## calculate Sequence perpentage
    fl_count = './fl_result/count/' + fl_base + '_count.txt'
    fh_count = open(fl_count, 'r')
    fl_count_out = './fl_result/result/count/' + fl_base + '_summary.txt'
    fh_count_out = open(fl_count_out, 'a')
    if mode == 'deep':
        for line3 in fh_count:
            line3 = line3.strip('\n')
            line3 = line3.split(' ')
            line3_per = int(line3[1]) / length_dic[line]
            output = line3 + [str(line3_per)]
            fh_count_out.writelines('\t'.join(output))
            fh_count_out.writelines('\n')
    elif mode == 'C4C6':
        dic_c4c6 = {'CC': 0, 'CT': 0, 'TC': 0, 'TT':0}
        for line3 in fh_count:
            line3 = line3.strip('\n')
            line3 = line3.split(' ')
            pattern = line3[0][7] + line3[0][9]
            if dic_c4c6.get(pattern) is not None:
                dic_c4c6[pattern] = dic_c4c6[pattern] + int(line3[1])
        dic_out = sorted(dic_c4c6.iteritems(), key = lambda d: d[0])
        for item in dic_out:
            fh_count_out.writelines('\t'.join([str(item[0]), str(item[1])]))
            fh_count_out.writelines('\n')
    elif mode == 'C4C5':
        dic_c4c5 = {'CC': 0, 'CT': 0, 'TC': 0, 'TT': 0}
        for line3 in fh_count:
            line3 = line3.strip('\n')
            line3 = line3.split(' ')
            pattern = line3[0][7] + line3[0][8]
            if dic_c4c5.get(pattern) is not None:
                dic_c4c5[pattern] = dic_c4c5[pattern] + int(line3[1])
        dic_out = sorted(dic_c4c5.iteritems(), key = lambda d: d[0])
        for item in dic_out:
            fh_count_out.writelines('\t'.join([str(item[0]), str(item[1])]))
            fh_count_out.writelines('\n')
    elif mode == 'C6C7C8':
        dic_c6c7c8 = {'CCC': 0, 'CCT' : 0, 'CTC': 0, 'CTT': 0, 'TCC': 0, 'TCT': 0, 'TTC': 0, 'TTT': 0}
        for line3 in fh_count:
            line3 = line3.strip('\n')
            line3 = line3.split(' ')
            pattern = line3[0][9] + line3[0][10] + line3[0][11]
            if dic_c6c7c8.get(pattern) is not None:
                dic_c6c7c8[pattern] = dic_c6c7c8[pattern] + int(line3[1])
        dic_out = sorted(dic_c6c7c8.iteritems(), key = lambda d: d[0])
        for item in dic_out:
            fh_count_out.writelines('\t'.join([str(item[0]), str(item[1])]))
            fh_count_out.writelines('\n')
    elif mode == 'C5C6':
        dic_c5c6 = {'CC': 0, 'CT': 0, 'TC': 0, 'TT': 0}
        for line3 in fh_count:
            line3 = line3.strip('\n')
            line3 = line3.split(' ')
            pattern = line3[0][8] + line3[0][9]
            if dic_c5c6.get(pattern) is not None:
                dic_c5c6[pattern] = dic_c5c6[pattern] + int(line3[1])
        dic_out = sorted(dic_c5c6.iteritems(), key = lambda d: d[0])
        for item in dic_out:
            fh_count_out.writelines('\t'.join([str(item[0]), str(item[1])]))
            fh_count_out.writelines('\n')
    elif mode == '19C':
        dic_19c = {}
        for line3 in fh_count:
            line3 = line3.strip('\n')
            line3 = line3.split(' ')
            seq_19c = line3[0][4: 22]
            print seq_19c
            if dic_19c.get(seq_19c) is None:
                dic_19c[seq_19c] = int(line3[1])
            else:
                dic_19c[seq_19c] += int(line3[1])
        dic_out = sorted(dic_19c.iteritems(), key = lambda d: d[0])
        for item in dic_out:
            fh_count_out.writelines('\t'.join([str(item[0]), str(item[1])]))
            fh_count_out.writelines('\n')
    fh_count_out.close()
    fh_count.close()
