import pandas as pd
import numpy as np
import ast
from pandas import ExcelWriter
from pandas import ExcelFile


<<<<<<< HEAD
#define excel document for code
 
def read_excel_file(filepath): 
    
    '''
    Reading the excel file and returns a dataframe
    '''
    df = pd.read_excel(filepath)
    df_index = df.set_index('Plate')
    return df_index


=======
'''Define a new dataframe (df) as being the excel document of choice with tetrad data'''
        
#reading the excel file that includes all of the tetrad data
df = pd.read_excel('python_test_list.xlsx')
    
#delete the automatically generated column on the left-hand side
df_index = df.set_index('Plate')
>>>>>>> d12550ee4eb1e2969c979ebe93d6661f7d8adff4


'''potential error may arise:if the variable df is not established before running the code below, then you will get no outcome'''







def sort_and_filter_by_col(df_in,col):
    '''This will sort by the input argument col and filter for positive values'''
   
    
    #separate the positive spores from the negative spores
    df_sorted = df_in.sort_values([col], ascending = False)
    pos_vals = df_sorted[df_sorted[col] > 0]

        
    #now take the positive ones and put them into their own excel document
    df_filtered = pd.DataFrame(pos_vals)
    return df_filtered
        
<<<<<<< HEAD
=======
#**run this new command to see if it works---if not then a new excel document with the name "NAT_positive" won't be created and saved on your computer**
sort_NAT()
>>>>>>> d12550ee4eb1e2969c979ebe93d6661f7d8adff4
        
        

    
<<<<<<< HEAD
    

def combine_antibiotics(df_in,markers):
=======

    #now take only the positive ones and place them in their own excel document
    dfNAT = pd.DataFrame(HYG_positive)
    dfNAT.to_excel("HYG_positive_python_fp.xlsx")
       
        
        
#**run this new command to see if it works---if not then a new excel document named "HYG positive" won't be created and saved on your computer**
sort_HYG()
        
        
        

def sort_URA():
    '''this will allow for you to select for spores in tetrads that test positiev for URA and place them in their own excel document'''

    #separate the positive spores from the negative spores
    sort_by_URA = df_index.sort_values(['URA'], ascending=False)
    URA_positive = df_index[df_index['URA'] > 0]
    

    #now take only the positive ones and place them in their own document
    dfNAT = pd.DataFrame(URA_positive)
    dfNAT.to_excel("URA_positive_python_fp.xlsx")

       
#**run this new command to see if it works---if not then a new excel document named "URA positive" won't be created and saved on your computer**
sort_URA()
>>>>>>> d12550ee4eb1e2969c979ebe93d6661f7d8adff4
   
    '''
    This will read an excel file, and for each marker provided will sort and
     filter for positive values. Returns a dictionary where each value is a 
     dataframe for a marker
     '''

    
    #create one dataframe containing all of the positive markers
    all_positive = {}
    for marker in markers:
        df_marker = sort_and_filter_by_col(marker)
        all_positive[marker + '_plus'] = df_marker
    
    return all_positive



def write_marker_dict_to_disk(marker,file_out):
    """
     Given a dict of dataframes, writes out an excel file in which each 
     dataframe occupies its own sheet
     """
    
    #turn the dataframes stored in a dict into an excel document
    writer = pd.ExcelWriter(file_out, engine='xlsxwriter')
    
    for sheet_name in markers.keys():
        markers[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
    
    
    
<<<<<<< HEAD
=======
#**run this new command to see if it works---if not then a new excel document named "Antibiotic_markers" won't be created and saved on your computer**
combine_antibiotics()
>>>>>>> d12550ee4eb1e2969c979ebe93d6661f7d8adff4
    
    
    
def antibiotic_analysis(file_in,file_out="Antibiotic_markers.xlsx",markers=['NAT','HYG','URA']):
     """
     Reads file_in, and for each marker performs a sort and filter before 
     writing the results to file_out. Each marker occupies its own sheet
     """
     df_tetrad = read_excel_file(file_in)
     output_dict = combine_antibiotics(df_tetrad,markers)
     write_marker_dict_to_disk(output_dict,file_out)

   


