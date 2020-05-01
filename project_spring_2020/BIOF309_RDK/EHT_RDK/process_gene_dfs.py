
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
