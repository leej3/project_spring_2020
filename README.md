#  project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)

Aidan O'Brien 

My project will focus on integrating GWAS results with epigenetic datasets. 

Our lab works on the finemapping of genomic regions identified through Genome-Wide Association Studies (GWAS) which are significantly associated with Pancreatic Cancer. Due to high corrleation between identified variants,the most significant variant is rarely the actual functional variant. Most variants localise to non-coding regions of the genome and are thought to control expression of proximal genes though enhancer-promoter interactions. To aid this fine-mapping process, our lab have generated large-scale epigenomic datasets, allowing us to identify regions of open chromatin, and regions associated with certain histone modifications such as H3K27ac. Variants which fall in such regions are much more likely to be functionally involved, and are good candidates for follow-up experiments. 

Statistical fine-mappping approaches have been developed to shortlist variants from GWAS summary statistics. Some methods, such as PAINTOR, integrate epigenomic datasets into their statistical model. However, this methods only marginally improve the posterior probability of causality for SNPs localising to putative regulatory regions. They are also hindered by an assumption of only one causal variant per locus.

Other methods, such as SuSiE, DAPG and FINEMAP implement a model wherein 'credible sets' of variants are derived. Within each 95% credible set, there is a approximate 95% confidence of containing at least one non-zero effect variable. This project aims to easily integrate SNPs contained within credible sets with the epigenomic datasets generated within our lab. 

Code will be written which takes a list of paths to standardised peak files produced from genome wide chip-seq and accessible chromatin assays which will then be intersected with the location of the SNPs in question. From this, a matrix will be outputted with a 0 assigned to SNPs which do not co-localise to epigentic peak, and a 1 to those which do. 

From this, it will become apparent which SNPs are functionally enriched and will then be priorised for functional followup.

In the code directory, we have all that is needed to output our matrix. 

Running the following command should produce an example matrix;

python annotation.plot.py locus_file, ann_paths_file, output, xlab)

  where;
    locus_file contains the SNPs that we are looking at in a space delimited text file, headers should
    be 'Chr', 'pos' and 'RSID'. 
    
    ann_paths_file contains directories to epigenetic bed files, in this case we are looking at ATAC
    seq peaks (open chromatin) and super-enhancer peaks (high H3K27ac). SNPs which fall in both are 
    quite likely to be functionally implicated. 
    
    output is a string to define the output files
    
    xlab is a string to plot some details on the final plot, in this case 'Chr5p15.33 Credible SNPs'
    will suffice. 
    
