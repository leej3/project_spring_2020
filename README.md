# Final Project
## BIOF 309 Spring 2020
**Author:** Ramita Karra
**Last edited:** 04-23-2020

## Project Description
This aim of this project is to produce a script that will process raw tab-delimited output returned from the ExpansionHunter-Targeted software tool, used for making sequence-graph-based predictions of repeat lengths for known genetic repeat loci. The ultimate goal is to clean, compile, and process data for many different loci into a summary table, and to provide visualizations pertinent to the functional relevance of this data (i.e. number of samples containing repeat numbers above the pathogenic threshold for each gene).  

More information on ExpansionHunter can be found [here](https://academic.oup.com/bioinformatics/article/35/22/4754/5499079). 

### Required Input
The raw data consists of a directory of all .txt files returned by ExpansionHunter-Targeted for multiple genes from a sample set.
### Project Details:
- Exploratory data analysis
- Input data from separate text files and merge into a single master dataframe based on sample ID
- Create dictionary for each gene, containing pathogenic repeat threshold values
- Determine summary statistics for each gene (total number of samples, samples with pathogenic range repeats)
- Create visualization to better understand data