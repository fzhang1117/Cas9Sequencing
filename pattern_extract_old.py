## pattern_extract.py ##
## extract the pattern from .fastq file ##
## Zhang Fei ##
## 2017-11-16 ##

import sys, re

fh_fastq = open(sys.argv[1], 'r')
fh_out_right = open(sys.argv[2], 'w')
fh_out_amazing = open(sys.argv[3], 'w')
pattern = sys.argv[4]

def Seq_complement(seq):
    seq = seq.upper()
    seq = seq[::-1]
    seq = seq.replace('A', 't')
    seq = seq.replace('C', 'g')
    seq = seq.replace('G', 'c')
    seq = seq.replace('T', 'a')
    seq = seq.upper()
    return seq


def fastq2seq(fh_fastq):
    seq_out = []
    seq_out2 = []
    i = 1
    j = 1
    for line in fh_fastq:
        line = line.strip('\r\n')
        index = i % 4
        if index == 2:
            seq = line
            m = re.findall(pattern, seq)
            if len(m) == 0:
                seq2 = Seq_complement(seq)
                m = re.findall(pattern, seq2)
                if len(m) == 0:
                    print "the line ", i, " seems sequencing wrong, the seq is ", seq
                    seq_out2.append(seq)
                    j += 1
                else:
                    seq_out.append(m[0])
            else:
                seq_out.append(m[0])
        i += 1
    print "in total ", j, " sequences seem sequencing wrong"
    return (seq_out, seq_out2)

result = fastq2seq(fh_fastq)
seq_right = result[0]
seq_amazing = result[1]

fh_out_right.write('\n'.join(seq_right))
fh_out_amazing.write('\n'.join(seq_amazing))
