# Antimicrobial peptide prediction in non-model species based on transcriptome data.

## Project description

Lake Baikal hosts a unique deep-water freshwater fauna, which includes various representatives species living in a wide range of environmental conditions, from the littoral zone to the maximum depths. The main diet of deep-sea representatives is carrion with a specific saprotrophic microbiota. Thus, the deep-sea crustaceans are assumed to have a variety of protection mechanisms against pathogens, including antimicrobial peptides.

Antimicrobial peptides (AMPs) are a common name for several groups of peptides produced by the organisms sharing the ability to inhibit the development of microorganisms. At the moment, about 11,000 AMP of either animal and plant origin are known. Most AMP groups are not phylogenetically related and have different mechanisms of action, which makes identifying their similarities an uneasy task. In most cases, AMP are charged cationic polymers up to 100 aa (average 40-50) with a tendency to aggregation in vivo but stable in the external environment.

RNA-seq data can be used to generate proteome prediction, and thus they can also be used to search for AMPs. [Kim et al., 2016][7] developed a pipeline to search for AMP in cockroach transcripts. However, the specifics of our data and the expansion of the zone of interest also to the cryptic AMPS require its improvement.

## Goals and objectives

Aim:

Prediction and characterization of the spectrum of antimicrobial peptides (AMP) in deep-sea amphipods in comparison with littoral ones.

Tasks: 

1) Compare the repertoires and expression levels of AMPs in two species, *Ommatogammarus flavus* and *Eulimnogammarus verrucosus*
2) Find known AMP and characterize them
3) Find unknown AMP 
    * Develop a search algoritm for peptides with potential antimicrobial properties based on  transcriptome data
    * Implement the algorithm as a single pipeline

## Data

We used raw transctiptome data from [Naumenko et al., 2017][5]

[5]: https://www.ncbi.nlm.nih.gov/pubmed/27859915

[*Ommatogammarus flavus*][1]

[*Eulimnogammarus verrucosus*][2]

[*Poekilogammarus pictoides*][3]

[*Micruropus parvulus*][4]

[1]: https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=run_browser&run=SRR3467086
[2]: https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=SRR3467068
[3]: https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=SRR3467101
[4]: https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=SRR3467081

## Methods

### Data pre-processing
Transcriptome assembly was performed using Trinity (version 2.8.4) with default parameters (except -min_len, which was equal to 100). The assembly quality was estimated by the BUSCO program (version 1.2) with the *arthropoda_db9* database. The obtained nucleotide contigs were translated into protein sequences using the  TransDecoder program (version 5.5.0) with default parameters. Further analysis was performed using protein sequences.

### Known AMP analysis
To search for known AMP, we performed a blastp search on the database [db_AMP][6] with default parameters (except --sensitive and --max-target-seqs 1). The contigs, annotated as "crustin", were selected for further individual analysis. The crustin classification tree was constructed (PhyML) and visualized with R (package grep v 2.8.4).

To search for homologous sequences of crustins within the published amphipod transcriptomes, we conducted a blast-search of the initial nucleotide sequences found in the TSA database (taxon = amphipoda).

[6]: http://140.138.77.240/~dbamp/introduction.php

### Pipeline development

The developed pipeline is based on this article [Kim et al., 2016][7]

[7]: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0155304


1. The initial protein sequences are cut into chunks of 50 amino acids with a 5-aa sliding window (cut_fasta.py)
2. The physico-chemical properties of the predicted peptides are calculated with PEPSTAT (EMBOSS:6.6.0.0). 
3. Aggregation properties and probable secondary structures are predicted with Tango (version 2.3 ) and [AGGRESCAN][9].
4. Prediction of antimicrobial properties is performed with the [CAMP][8] database (random forest) and the AMPA program (version 19.01.0.5050). 
5. PEST motifs in the predicted peptides are identified with the Epestfind script (EMBOSS:6.6.0.0).

![](https://github.com/IrinaBabkina/Antimicrobial_peptide/blob/production/Result/Pipeline_eng.png?raw=true)

[8]: http://www.camp.bicnirrh.res.in/index.php
[9]: http://bioinf.uab.es/aggrescan/

## Результаты

During the work 4 transcriptomes of gammarids from different phylogenetic branches were assembled. Two of them, according to BUSCO, were of excellent quality (red arrows), and two were of medium quality (blue arrows).

![](https://github.com/IrinaBabkina/Antimicrobial_peptide/blob/production/Result/Transcriptome_assembly.png?raw=true)

### Crustins

At the moment there is no published information about the crustins of amphipods. In transcripts of 2 species, *Ommatogammarus flavus* and *Eulimnogammarus verrucosus*, 4 groups of proteins similar in structure to Decapoda crustins were found. In the other two 2 species, *Poekilogammarus pictoides* and *Micruropus parvulus*, we managed to find only 3 crustin groups. However, the lack of the 4th group is the result of assemble errors of the transcriptome of specific representatives, and not the property of the particular genera, since the search in TSA revealed homologous group E sequences among other representatives of these branches of gammarus. 

![](https://github.com/IrinaBabkina/Antimicrobial_peptide/blob/production/Result/Crustin_tree.png?raw=true)

### Predicted AMP

Pipeline testing was conducted on the data of the transcriptome *Ommatogammarus flavus*.

For the 916 predicted peptides returned by the pipeline, we performed independent validation of their antimicrobial properties with the algorithms of the db_AMP database, which was not used in our pipeline. As a result, 91% of "peptides" was evaluated by the algorithm as antimicrobial, which indicates a good quality of selection. 

![](https://github.com/IrinaBabkina/Antimicrobial_peptide/blob/production/Result/Reduction_data_eng.png?raw=true)

## Summary

1) We found sequences similar to the crustin family of AMP. 
2) In the transcripts from different phylogenetic branches of the gammarids we studied, we were able to identify 4 stable groups of crustins. There is also preliminary information on the presence of crustins among other species.
3) We developed and partially implemented a pipeline to search for AMP in transcriptome data.

 