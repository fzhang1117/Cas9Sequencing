#! /bin/sh

pattern=$1
pattern_indel=$2
length=$3
Q=$4
cd ./fastq

gunzip *

for seq in $(ls *fq | sed 's/.fq//g')
do
	echo $seq
	#fastx_quality_stats -i $seq.fq -o ../out/summary_$seq.txt -Q 33
    fastq_quality_converter -n -Q 33 -i ${seq}.fq -o ../fq_trans/${seq}_trans.fq
	python ../pattern_extract.py ../fq_trans/${seq}_trans.fq ../fl_result/extract/${seq}.extract.txt ../fl_result/indel/${seq}_indel.txt $pattern $pattern_indel $Q > ../log/${seq}_log.txt
	python ../result_stat.py ../fl_result/extract/${seq}.extract.txt $length ../edit_site.txt ../fl_result/summary/${seq}_seqscan.txt ../fl_result/summary/${seq}_productsum.txt
	awk '{a[$1]++}END{for(i in a){print i, a[i] | "sort -r -n -k 2"}}' ../fl_result/extract/${seq}.extract.txt > ../fl_result/count/${seq}_count.txt
done

