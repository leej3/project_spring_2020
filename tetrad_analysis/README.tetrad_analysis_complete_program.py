import pandas as pd
import numpy as np


**names of documents can change due to the names of the documents that the user uses.  The names present are applied to the documents that I used for this code**

def pd.read_excel(r'/Users/harveycas/Documents/FAES/Python class/python_test_list.xlsx')
    '''
    This function is to call in an excel document from your computer for this program.  Make sure that the path to the excel
    document is correct and the "r'" is necessary for the code to work
    '''



#this is needed in order to remove the automatic numbering column that is on the left

df_index = df.set_index('Plate')
print(df_index)





def df_index.sort_values(['NAT'], ascending=False)
    NAT_positive = df_index[df_index['NAT'] > 0]
    '''
    This is a code that sorts all of the NAT values in the document.  It sorts the positive (which is represented by a 1)
    from the negative (which is marked by a 0)  
    '''




def dfNAT = pd.DataFrame(NAT_positive)
    dfNAT.to_excel("NAT_positive_python_fp.xlsx")
    '''
    This is required to create a new dataframe using the sorted data. The second line of code converts the data into
    an excel document that will end up on your computer's library
    '''





def sort_by_HYG = df_index.sort_values(['HYG'], ascending=False)
    HYG_positive = df_index[df_index['HYG'] > 0]

    '''
    This is a code that sorts all of the HYG values in the document.  It sorts the positive (which is represented by a 1)
    from the negative (which is marked by a 0) 
    '''
    
    

def dfNAT = pd.DataFrame(HYG_positive)
    dfNAT.to_excel("HYG_positive_python_fp.xlsx")
    '''
    This is required to create a new dataframe using the sorted data. The second line of code converts the data into
    an excel document that will end up on your computer's library
    '''




def sort_by_URA = df_index.sort_values(['URA'], ascending=False)
    URA_positive = df_index[df_index['URA'] > 0]
    '''
    This is a code that sorts all of the URA values in the document.  It sorts the positive (which is represented by a 1)
    from the negative (which is marked by a 0) 
    '''
    
    
def dfNAT = pd.DataFrame(URA_positive)
    dfNAT.to_excel("URA_positive_python_fp.xlsx")

    '''
    This is required to create a new dataframe using the sorted data. The second line of code converts the data into
    an excel document that will end up on your computer's library
    '''




def all_positive = {'NAT_plus': NAT_positive, 'HYG_plus': HYG_positive, 'URA_plus': URA_positive}
    
    '''
    This code combines the three new dataframes created above into one dataframe
    '''


def writer = pd.ExcelWriter('Antibiotic_markers.xlsx', engine='xlsxwriter')
    
    '''
    This converts this  'all_positive' dataframe into a new excel document called 'Antibiotic_markers'  
    '''

def for sheet_name in all_positive.keys():
    all_positive[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
    
    '''
    This organizes the three previous dataframes ('NAT_plus', 'HYG_plus', and 'URA_plus') as their own sheet in the 
    new major excel document 'Antibiotic_markers'
    '''
    
def writer.save()
    '''
    This code saves the new major excel document onto your computer
    '''


