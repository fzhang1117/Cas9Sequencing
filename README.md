# Cas9Sequencing for handle Cas9 DNA sequencing data
This is the Analysis pipeline of Article 'Engineering of high-precision base editors for site-specific single nucleotide replacement'

## pre perpare ##
Before run the pipeline, you should prepare such things below:
**1. put all your sequencing data in dir ./fastq first, end by .fq.gz or .fq**

**2. design a recogine pattern (Regular expression to extract edit region) and an indel detect pattern (Regular expression to detect indel)**

**2.1 Regular expression to extract edit region:**

for example, the template seq is:
```
NTGAGCACTGCGGAAGTGAGGGGAGCAGTAAATAGTGATCTTTGTAATTTTCTGCAAAATCCCTATCGCTGTCTCGGGTTTTTCGATTCAGAGGACCTT---CCCCCCCCCATGTTCCGAGATCGG---TTTTGGTGGTTAGAAGGCCGGAGGAAC
```
The seq CCCC*CGG are edit region, consider inserts are not intersted, so the pattern can be written as

```
CCTT[ATCG]{24}TTT
```

The flanking region could not be too short (may cause mislead to extract wrong seq) or too long (may out of the sequencing region), in our experience, 3 or 4 nucleotide is okay

**2.2 Regular expression to extract detect indel**

In this step, for the edit region has no given length, we recognize a long flanking region to ignore mislead, in this case, the pattern can be written as

```
AGAGGACCTT.*TTTTG
```

**3. design the edit site want to detect**

You should set up a new text file named as 'edit_site.txt' first. This file should contain two column, the first column is the locus relative to the Recoginze pattern and start as 0. The second column is the locus relative to PAM(NGG) and define the locus of 'N' in 'NGG' as 0.

## run the pipeline ##
Just type the comman below
```shell
sh Cas9Sequencing.sh <recogine pattern> <indel detect pattern> <length of recoginze pattern> <quanlity to file>
```
Take a coffee and comeback to see the result

## output ##
All the result are saved in the dir ./fl_result

**./fl_result/count/**: edit products and their count number

**./fl_result/extract/**: all the sequences could be extract by recoginze pattern

**./fl_result/indel/**: idel sequences

**./fl_result/summary/**:

```
*_seqscan.txt: counts of differenty types of nulceotide of each sites in edit region
*_productsum.txt: products and their counts of given edit sites
```




