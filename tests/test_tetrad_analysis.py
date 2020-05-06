import pytest
from tetrad_analysis import dataframe_functions.py
import pandas
import numpy
    

def test_NAT_df_index_sort_values():
    #assert column = ['NAT']
    assert ascending == False
    assert df_index[df_index['NAT'] > 0] == 1
    
#makes sure that you are getting the positive clones and not the negative ones (ones with 0)    
                    

def test_HYG_df_index_sort_values():
    #assert column = ['HYG']
    assert ascending == False
    assert df_index[df_index['HYG'] > 0] == 1
 
#makes sure that you are getting the positive clones and not the negative ones (ones with 0)                
                    
                    
def test_URA_df_index_sort_values():
    #assert column = ['URA']
    assert ascending == False
    assert df_index[df_index['URA'] > 0] == 1
                    
                    
#makes sure that you are getting the positive clones and not the negative ones (ones with 0)  