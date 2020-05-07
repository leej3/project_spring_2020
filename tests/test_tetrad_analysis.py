import pytest
from tetrad_analysis import dataframe_functions
import pandas as pd
import numpy as np
from pathlib import Path

SAMPLE_XLSX = Path(__file__) / "data" / "python_test_list.xlsx"
  SAMPLE_DF_TAIL = pd.DataFrame(
         data={
             "Plate": [1,1,1],
             "Tetrad":[12,12,12],
             "spore":["12B","12C","12D"],
             "viability":[1,1,1],
             "NAT": [0,1,0],
             "HYG": [0,1,0],
             "URA": [0,1,0],
             }
     )
    
    
def test_read_excel_file():
    
    '''
    This is to test whether read_excel_file() actually reads the file and returns in the correct format
    '''
    
    expected_tail = SAMPLE_DF_TAIL.set_index("Plate")
    
    result = dataframe_functions.read_excel_file(SAMPLE_XLSX)
    assert result.tail(3) == expected_tail, 'fail1'
    

def test_sort_and_filter_by_col():
  
  '''This tests whether sort_and_filter_by_col() filters variables by col (antibiotics) and isolates the positive values
  '''
    
    #For sorting input by col
    
    expected_df = dataframe_functions.read_excel_file(SAMPLE_XLSX)
    expected_df_sorted = dataframe_functions_in.sort_values([col], ascending = False)
    
    #test for isolating positive values:
    
    expected_pos_vals = expected_df_sorted[expected_df_sorted[col]>0]
    expected_df_filtered = pd.DataFrame(expected_pos_vals)
    
    result = dataframe_functions.sort_and_filter_by_col(expected_df_in, col)
    assert result == expected_df_filtered, 'fail2'
                  


def test_combine_antibiotics():
    
    '''
    this tests whether combine_antibiotics() combines the new databases into one library
    '''
    
    expected_df = dataframe_functions.read_excel_file(SAMPLE_XLSX)
    
    expected_all_positive = {}
    for marker in markers:
        expected_marker = dataframe_functions.sort_and_filter_by_col(marker)
        expected_all_positive[marker + '_plus'] = expected_marker
    return expected_all_positive
    
    result = dataframe_functions.test_combine_antibiotics(expected_df_in,markers)
    
    assert result == expected_all_positive, 'fail3'
    
    
    
    

def test_write_marker_dict_to_disk():
    
    '''
    tests whether write_marker_dict_to_disk() creates a new excel document where each dataframe from the library occupies its own sheet.
    '''
    
    writer = pd.ExcelWriter(file_out, engine='xlsxwriter')
    for sheet_name in markers.keys():
        markers[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
    expected_result = writer.save()
    
    result = write_marker_dict_to_disk(marker,file_out)
    
    assert result == expected_result, 'fail4'

    
    
    

def test_antibiotic_analysis():
    
    '''
    tests whether antibiotic_analysis() sorts and filters the data for each marker before uploading the document
    '''
    
    expected_df = dataframe_functions.read_excel_file(SAMPLE_XLSX)
    
    expected_df_tetrad = read_excel_file(file_in)
    expected_output_dict = combine_antibiotics(expected_df_tetrad, markers)
    expected_result = writer_marker_dict_to_disk(expected_output_dict,file_out)
    
    result = dataFrame_functions.test_antibiotic_analysis(file_in, file_out="Antibiotic_markers.xlsx",markers=['NAT','HYG','URA'])
    
    assert result == expected_result, 'fail5'
    


    
