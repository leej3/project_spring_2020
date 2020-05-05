import pandas as pd

def create_gene_dict(df_list):
    
    """This function creates a dictionary with keys as genes, subdictionaries as key:value pairs for "chr", 
    "pos". It uses a list of dataframes passed in as an input parameter..""" 
    
    gene_dict = {}

    for df in df_list:
        # Get gene name
        gene = df.columns[3]

        # Get chromosome
        chr_num = df.iloc[0,1]
        chr_num = chr_num.replace("chr","",1) # Remove "chr" prefix

        # Get gene position
        pos = df.iloc[0,2]

        # Edit dictionary
        gene_dict.update( {gene : {"chr":chr_num, "pos":pos}} )
    
    return(gene_dict)
    
def merge_dfs(old_df_list):
    """This function merges the list of dataframes passed in as an input parameter, by first re-indexing the 
    dataframes by SampleID, and then merging based on SampleID""" 
    
    # Change sampleID to index in dfs
    df_reindex_list = []

    for df in old_df_list:
        column_names = list(df.columns)
        temp_reindex_df = df.set_index(df['SampleID'])
        temp_reindex_df = temp_reindex_df[column_names[1:]]
        df_reindex_list.append(temp_reindex_df)

    # Create a list of dfs to merge
    to_merge = []

    for df in df_reindex_list:
        column_names = list(df.columns)
        temp_df = df[column_names[2]]
        to_merge.append(temp_df) 

    # Merge dfs on sampleID to create master df of all gene max repeat lengths
    # Use 'outer' join to keep all samples, including those that do not contain information for all genes
    master_df = pd.concat(to_merge, axis = 1, join='outer', sort=False)
    
    return(master_df)
