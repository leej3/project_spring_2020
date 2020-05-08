
# EHT_RDK
## Package Description
This package processes raw tab-delimited output returned from the ExpansionHunter-Targeted software tool, used for making sequence-graph-based predictions of repeat lengths for known genetic repeat loci. It cleans, compiles, and processes data for many different loci into a summary table, and provides visualizations pertinent to the functional relevance of this data (i.e. number of samples containing repeat numbers above the pathogenic threshold for each gene). <br>

More information on ExpansionHunter can be found [here](https://academic.oup.com/bioinformatics/article/35/22/4754/5499079). 
<br>
## Package modules
Modules included with this package are:
- input_files
- process_gene_dfs
- further_analyses <br>

## Module descriptions
The modules are meant to be implemented in a step-wise manner, in order to:
- **input_files**: input raw files from the user-provided directory
- **process_gene_dfs**: clean and process files by creating a gene dictionary containing pertinent info (chr, position) and merge gene repeat dataframes using sample IDs as an index
- **further_analyses**: create a summary table listing all genes and number of samples above the pathogenic range (with option to export), create a barchart visualization of this data (with option to export)
