import pandas as pd
import numpy as np
import ast
from pandas import ExcelWriter
from pandas import ExcelFile

#reading the excel file that includes all of the tetrad data
df = pd.read_excel('python_test_list.xlsx')


def open_tetrad(excel):
    """cleaning a specific document from your computer"""
        
    #delete the automatically generated column on the left-hand side
    df_index = df.set_index(first_column)
    df_index = df.set_index('Plate')
    print(df_index)


def sort_NAT(excel):
    '''This will allow for you to select for spores in tetrads that test positive for NAT and place them in their own excel document'''
   
    
    #separate the positive spores from the negative spores
    df_index.sort_values(['NAT'], ascending=False)
    NAT_positive = df_index[df_index['NAT'] > 0]
    print(NAT_positive)
        
        
        
    #now take the positive ones and put them into their own excel document
    dfNAT = pd.DataFrame(NAT_positive)
    dfNAT.to_excel("NAT_positive_python_fp.xlsx")
    
        
    


def sort_HYG():
    '''this will allow for you to select for spores in tetrads that test positive for HYG and place them in their own excel document'''

    #separate the positive spores from the negative spores
    sort_by_HYG = df_index.sort_values(['HYG'], ascending=False)
    HYG_positive = df_index[df_index['HYG'] > 0]
    print(HYG_positive)

    #now take only the positive ones and place them in their own excel document
    dfNAT = pd.DataFrame(HYG_positive)
    dfNAT.to_excel("HYG_positive_python_fp.xlsx")


        
        

def sort_URA():
    '''this will allow for you to select for spores in tetrads that test positiev for URA and place them in their own excel document'''

    #separate the positive spores from the negative spores
    sort_by_URA = df_index.sort_values(['URA'], ascending=False)
    URA_positive = df_index[df_index['URA'] > 0]
    print(URA_positive)

    #now take only the positive ones and place them in their own document
    dfNAT = pd.DataFrame(URA_positive)
    dfNAT.to_excel("URA_positive_python_fp.xlsx")


def combine_antibiotics():
    '''this will take the three marker documents that you made and place them in one major excel document where each marker is one sheet of the document'''

    #create one dataframe containing all of the positive markers
    all_positive = {'NAT_plus': NAT_positive, 'HYG_plus': HYG_positive, 'URA_plus': URA_positive}
    
    #turn this new combined dataframe into an excel document
    writer = pd.ExcelWriter('Antibiotic_markers.xlsx', engine='xlsxwriter')
    
    for sheet_name in all_positive.keys():
        all_positive[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
    
   


