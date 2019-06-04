# Technical information
## Transcriptome Assembly
### Data pre-processing
```shell
wget ftp://ftp-trace.ncbi.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR346/SRR3467068/SRR3467068.sra

fastq-dump -I --split-files SRR3467068.sra  

fastqc ~/0_row_data/SRR3467068_1.fastq

fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files -Z  SRR3467068.sra|head -n20000000000 | gzip > SRR3467068.interleaved.fastq.gz

gunzip -c SRR3467068.interleaved.fastq.gz | \
  paste - - - - - - - - | \
  tee >(cut -f 1-4 | tr '\t' '\n' | gzip > SRR3467068_1.fastq.gz) | \
  cut -f 5-8 | tr '\t' '\n' | gzip -c > SRR3467068_2.fastq.gz
  
```
### Trinity assembling
```sh
./Trinity --seqType fq --max_memory 32G --left /media/main/sandbox/irina_IB/0_row_data/E_verr/SRR3467068_1.fastq.gz  --right /media/main/sandbox/irina_IB/0_row_data/E_verr/SRR3467068_2.fastq.gz --CPU 6 --min_contig_length 100 --output /media/main/sandbox/irina_IB/0_row_data/E_verr/trinity_out5_SRR68
--bypass_java_version_check
```

### BUSCO
```sh
python /media/secondary/apps/busco/scripts/run_BUSCO.py --in /media/main/sandbox/irina_IB/1_quality/E_verr/T_out_SRR68_100.fasta -o B_SRR68_100 -m tran -f -l /media/main/databases/arthropoda_odb9/ --cpu 6

python /media/secondary/apps/busco/scripts/generate_plot.py -wd BUSCO_summaries/
```
### Annotation by Diamond
```sh
/media/secondary/apps/diamond_old blastx --threads 6 --db /media/main/databases/nrd.dmnd --out /media/main/sandbox/irina_IB/1_quality/E_verr/D_out_SRR68_100 --sensitive --query /media/main/sandbox/irina_IB/1_quality/E_verr/T_out_SRR68_100.fasta --max-target-seqs 1 --taxonmap /media/main/databases/prot.accession2taxid.gz -f 6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore staxids stitle salltitles
```
### TransDecoder for protein prediction
```sh
TransDecoder.LongOrfs -t T_out_SRR68_100.fasta -m 30

TransDecoder.Predict -t T_out_SRR68_100.fasta
```
## Crustin analysis

Crustin analysis was performed using BLAST NCBI and local blastp. Alignment was carried out in the program seaview (algorithm ClustalW). The classification tree was built by PhyML method. 

## Prediction pipeline code

You can get information about the code through a personal request