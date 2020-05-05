
import pandas as pd

def create_summary_df(genes_of_interest, pathogenic_bounds, gene_dict, master_df, export=False):
    """This function creates a summary table of the number of pathogenic samples for each of the genes of interest.
    It accepts a list of genes of interest, a list of the pathogenic bounds for those genes, the previously
    generated gene dictionary, and the master dataframe of all genes and repeat info as input parameters. It
    exports the dataframe if the input parameter 'export' is specified as 'True' by the user."""

    # Add pathogenic range for 10 desired genes to dictionary
    for gene in genes_of_interest:
        gene_dict[gene].update( {"pathogenic_bound":pathogenic_bounds[genes_of_interest.index(gene)]} )

    # Count number of samples with repeats greater than or equal to pathogenic_bound
    # Append to dictionary
    for gene in genes_of_interest:
        path_count = len(master_df[master_df[gene] >= gene_dict[gene]['pathogenic_bound']])
        gene_dict[gene].update( {"pathogenic_count":path_count} )
        
    # Create new gene dictionary for desired genes only
    new_gene_dict = { gene_key: gene_dict[gene_key] for gene_key in genes_of_interest }

    # Create dataframe for desired genes using new_gene_dict dictionary
    summary_df = pd.DataFrame.from_dict(new_gene_dict, orient='index')
    summary_df.columns = ['Chromosome','Position','Pathogenic Bound','Number of Pathogenic Samples']
    summary_df.index.name = 'Gene'
    
    # Export summary dataframe
    if export==True:
        summary_df.to_csv('Pathoenic_Repeat_Data_Summary', index=True)
        
    return(summary_df)

def plot_pathogenic(summary_df, export=False):
    
    """This function plots the summary pathogenic repeat counts using the summary_df input parameter"""
    
    import matplotlib.pyplot as plt
    
    # Plot pathogenic samples for each gene of interest
    summary_df['Number of Pathogenic Samples'].plot(kind='bar')
    plt.minorticks_on()
    plt.title('Summary of Pathogenic Repeat Data')
    plt.xlabel('Genes')
    plt.ylabel('Number of Pathogenic Samples')

    plt.show()
    
    # Save plot to file 
    if export==True:
        plt.savefig('Pathogenic_Repeat_Data_Summary_Plot.png')
