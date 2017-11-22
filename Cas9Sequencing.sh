#! /bin/sh

cd ./fastq

gunzip *

for seq in $(ls *fq | sed 's/.fq//g')
do
	echo $seq
	#fastx_quality_stats -i $seq.fq -o ../out/summary_$seq.txt -Q 33
	python ../pattern_extract.py $seq.fq ../fl_result/extract/${seq}.extract.txt ../fl_result/amazing/${seq}_amazing.txt "GACCTT[ATCG]{24}TTTTGG" > ../log/${seq}_log.txt
	python ../result_stat.py ../fl_result/extract/${seq}.extract.txt 36 ../fl_result/summary/${seq}_summary.txt
	awk '{a[$1]++}END{for(i in a){print i, a[i] | "sort -r -n -k 2"}}' ../fl_result/extract/${seq}.extract.txt > ../fl_result/count/${seq}_count.txt
done

