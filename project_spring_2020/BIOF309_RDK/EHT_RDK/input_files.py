
import os
import glob
import pandas as pd

def create_input_list(directory_name):
    file_list = []

    # Check to make sure that only '.txt' files are being appended to list
    for filename in os.listdir(directory_name):
        if filename.endswith('.txt'):
            file_list.append(filename)
        else:
            print('Found non .txt file in directory: ' + filename)
            
    return(file_list)

def create_dataframe_list(file_list, dir_name):
    """This function creates a list of dataframes from the passed input list containing filenames. The 
    'SampleID','chr',and 'pos' columns are retained from the original dataframe, and a new column is created
    for the maximum repeats on either allele (column heading is the gene name).""" 

    df_list = []

    try:

        for filename in file_list:
        
            # Get gene name
            if filename.startswith("ExpansionHunterTargeted.ftd"):
                gene = filename.replace("ExpansionHunterTargeted.ftd.","", 1)
                if gene.endswith(".txt"):
                    gene = gene.replace(".txt","",1)
                else:
                    print("filename does not contain suffix")
                    return(NotImplemented)
            else:
                print("filename does not contain prefix")
                return(NotImplemented)
        
            # Import and format df
            df_temp = pd.read_csv(os.path.join(dir_name, filename), sep='\t')
            df_temp.rename(columns={ df_temp.columns[6]: "allele1" }, inplace = True)
            df_temp.rename(columns={ df_temp.columns[7]: "allele2" }, inplace = True)
            df_temp['min'] = df_temp[['allele1','allele2']].min(axis=1)
            df_temp[gene] = df_temp[['allele1','allele2']].max(axis=1)
            df_temp = df_temp[['SampleID','chr','pos',gene]]
            df_list.append(df_temp)
            
        return(df_list)

    except TypeError as detail :
        msg = "Unable to read specified dataframes from provided directory.\
               Please doublecheck file list and directory name."
        raise TypeError(detail.__str__() + "\n" +  msg)
