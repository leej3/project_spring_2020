import pandas as pd
import numpy as np
import ast
from pandas import ExcelWriter
from pandas import ExcelFile


#define excel document for code
        
#reading the excel file that includes all of the tetrad data
df = pd.read_excel('python_test_list.xlsx')
    
    
    
#delete the automatically generated column on the left-hand side
df_index = df.set_index('Plate')



def sort_NAT():
    '''This will allow for you to select for spores in tetrads that test positive for NAT and place them in their own excel document'''
   
    
    #separate the positive spores from the negative spores
    df_index.sort_values(['NAT'], ascending=False)
    NAT_positive = df_index[df_index['NAT'] > 0]

             
        
    #now take the positive ones and put them into their own excel document
    dfNAT = pd.DataFrame(NAT_positive)
    dfNAT.to_excel("NAT_positive_python_fp.xlsx")
      


        
#**run this new command to see if it works---if not then a new excel document won't be created and saved on your computer**
sort_NAT()
        
        
        
    

def sort_HYG():
    '''this will allow for you to select for spores in tetrads that test positive for HYG and place them in their own excel document'''

    #separate the positive spores from the negative spores
    sort_by_HYG = df_index.sort_values(['HYG'], ascending=False)
    HYG_positive = df_index[df_index['HYG'] > 0]
    

    #now take only the positive ones and place them in their own excel document
    dfNAT = pd.DataFrame(HYG_positive)
    dfNAT.to_excel("HYG_positive_python_fp.xlsx")
       
        
        
#**run this new command to see if it works---if not then a new excel document won't be created and saved on your computer**
sort_HYG()
        
        
        

def sort_URA():
    '''this will allow for you to select for spores in tetrads that test positiev for URA and place them in their own excel document'''

    #separate the positive spores from the negative spores
    sort_by_URA = df_index.sort_values(['URA'], ascending=False)
    URA_positive = df_index[df_index['URA'] > 0]
    

    #now take only the positive ones and place them in their own document
    dfNAT = pd.DataFrame(URA_positive)
    dfNAT.to_excel("URA_positive_python_fp.xlsx")

       
#**run this new command to see if it works---if not then a new excel document won't be created and saved on your computer**
sort_URA()
   
    
    

    
    

def combine_antibiotics():
    '''this will take the three marker documents that you made and place them in one major excel document where each marker is one sheet of the document'''
    
    
    #bring back variables needed to compress the newly formed excel documents into one concise excel document
    NAT_positive = df_index[df_index['NAT'] > 0]
    HYG_positive = df_index[df_index['HYG'] > 0]
    URA_positive = df_index[df_index['URA'] > 0]
    
    #create one dataframe containing all of the positive markers
    all_positive = {'NAT_plus': NAT_positive, 'HYG_plus': HYG_positive, 'URA_plus': URA_positive}
    
    #turn this new combined dataframe into an excel document
    writer = pd.ExcelWriter('Antibiotic_markers.xlsx', engine='xlsxwriter')
    
    for sheet_name in all_positive.keys():
        all_positive[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
    
    
    
#**run this new command to see if it works---if not then a new excel document won't be created and saved on your computer**
combine_antibiotics()
    

print("finished")
    
   


