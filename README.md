# Cas9Sequencing for handle Cas9 DNA sequencing data

This program is a short pipeline in handle Cas9 DNA sequencing data

You should put your fastq data in dir ./fastq first, end by .fq.gz or .fq

Then type:
```shell
sh Cas9Sequencing.sh <regular pattern>
```
Here the regular pattern is the pattern we want to find in the seq

for example, the template seq is:
```
NTGAGCACTGCGGAAGTGAGGGGAGCAGTAAATAGTGATCTTTGTAATTTTCTGCAAAATCCCTATCGCTGTCTCGGGTTTTTCGATTCAGAGGACCTT---CCCCCCCCCATGTTCCGAGATCGG---TTTTGGTGGTTAGAAGGCCGGAGGAAC
```
The seq CCCC*CGG are edit region, consider inserts are not intersted, so the pattern can be written as

```
CCTT[ATCG]{24}TTT
```
