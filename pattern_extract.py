## pattern_extract.py ##
## extract the pattern from .fastq file ##
## Zhang Fei ##
## 2017-11-16 ##

import sys, re

#fh_fastq = open(sys.argv[1], 'r')
#fh_out_right = open(sys.argv[2], 'w')
#fh_out_amazing = open(sys.argv[3], 'w')
#pattern = sys.argv[4]

fl_fastq = sys.argv[1]
fl_out_right = sys.argv[2]
fl_out_indel = sys.argv[3]
pattern = sys.argv[4]
pattern_indel = sys.argv[5]
Q = int(sys.argv[6])

def Seq_complement(seq):
    seq = seq.upper()
    seq = seq[::-1]
    seq = seq.replace('A', 't')
    seq = seq.replace('C', 'g')
    seq = seq.replace('G', 'c')
    seq = seq.replace('T', 'a')
    seq = seq.upper()
    return seq

def fastq_filter(fl_fastq, Q):
    seq_temp, seq_list, i, j = [0, 0], [], 1, 1
    with open(fl_fastq, 'r') as fh_fastq:
        for line in fh_fastq:
            line = line.strip('\r\n')
            index = i % 4
            i += 1
            if index == 2:
                seq_temp[0] = list(line)
            elif index == 0:
                #print line
                seq_temp[1] = line.split(' ')
                seq_temp[1] = [int(j) for j in seq_temp[1]]
                seq_final = ['N' if seq_temp[1][j] < Q else seq_temp[0][j] for j in range(0, len(seq_temp[1]))]
                #print seq_final
                #print seq_temp
                seq_final = ''.join(seq_final)
                seq_list.append(seq_final)
                seq_temp = [0, 0]
    return seq_list

def pattern_extract(seq_list):
    seq_out, seq_out2, i, j = [], [], 1, 1
    for line in seq_list:
        seq = line
        m = re.findall(pattern, seq)
        if len(m) == 0:
            seq2 = Seq_complement(seq)
            m2 = re.findall(pattern, seq2)
            if len(m2) == 0:
                #print "the line ", i, " seems sequencing wrong, the seq is ", seq
                seq_out2.append(seq)
                j += 1
            else:
                seq_out.append(m2[0])
        else:
            seq_out.append(m[0])
        i += 1
        #print "in total ", j, " sequences seem sequencing wrong."
    return (seq_out, seq_out2)

def indel_detect(seq_amazing, pattern_indel):
    seq_out, i = [], 0
    for seq in seq_amazing:
        m = re.findall(pattern_indel, seq)
        if len(m) != 0:
            i += 1
            seq_out.append(m[0])
        else:
            seq2 = Seq_complement(seq)
            m2 = re.findall(pattern_indel, seq2)
            if len(m2) != 0:
                i += 1
                seq_out.append(m2[0])
    print "indel reads num: ", i
    print "noise reads num: ", len(seq_amazing) - i
    return seq_out

seq_list = fastq_filter(fl_fastq, Q)
result = pattern_extract(seq_list)
seq_right = result[0]
seq_amazing = result[1]
print "total reads: ", len(seq_right) + len(seq_amazing)

seq_indel = indel_detect(seq_amazing, pattern_indel)

with open(fl_out_right, 'w') as fh_out_right:
    fh_out_right.write('\n'.join(seq_right))
with open(fl_out_indel, 'w') as fh_out_indel:
    fh_out_indel.write('\n'.join(seq_indel))
