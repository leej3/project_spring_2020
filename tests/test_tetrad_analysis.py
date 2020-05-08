import pytest
from tetrad_analysis import dataframe_functions as ddf
import pandas as pd
import numpy as np
from pathlib import Path
import os.path


SAMPLE_XLSX = Path(__file__).parent / "data"/"python_test_list.xlsx"
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
COL = "URA"
    
def test_read_excel_file():
    
    expected_tail = SAMPLE_DF_TAIL.set_index("Plate")
    
    result = ddf.read_excel_file(SAMPLE_XLSX)
    
    assert result.tail(3) == expected_tail
    

def test_sort_and_filter_by_col():
    
    #For sorting input by col
    
    expected_df = ddf.read_excel_file(SAMPLE_XLSX)
    expected_df_sorted = expected_df.sort_values(["URA"], ascending = False)
    
    #test for isolating positive values:
    
    expected_pos_vals = expected_df_sorted[expected_df_sorted[COL]>0]
    expected_df_filtered = pd.DataFrame(expected_pos_vals)
    
    result = ddf.sort_and_filter_by_col(expected_df,"URA")
    
    assert result == expected_df_filtered
    
    
    
    
                  


def test_combine_antibiotics():
    
    expected_df = ddf.read_excel_file(SAMPLE_XLSX)
    markers = ['NAT','HYG','URA']
    expected_all_positive = {}
    for marker in markers:
        expected_marker = ddf.sort_and_filter_by_col(expected_df,marker)
        expected_all_positive[marker + '_plus'] = expected_marker
    return expected_all_positive
    
    result = ddf.test_combine_antibiotics(expected_df,markers)
    
    assert result == expected_all_positive
    
    
    
    

def test_write_marker_dict_to_disk():
    file_out = "test.xlsx"
    marker = "URA"
    writer = pd.ExcelWriter(file_out, engine='xlsxwriter')
    
    anti_bs = { "a": pd.DataFrame({ "Plate": [1,1,1], "Tetrad":[12,12,12],})}
    for sheet_name in anti_bs.keys():
        anti_bs[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
    expected_result = writer.save()
    
    result = ddf.write_marker_dict_to_disk(anti_bs,file_out)
    
    assert result == expected_result

    
    
    

def test_antibiotic_analysis():
    file_out = "test.xlsx"
    markers = ['NAT','HYG','URA']
    expected_df = ddf.read_excel_file(SAMPLE_XLSX)
    
    expected_df_tetrad = ddf.read_excel_file(SAMPLE_XLSX)
    expected_output_dict = ddf.combine_antibiotics(expected_df_tetrad, markers)
    expected_result = ddf.write_marker_dict_to_disk(expected_output_dict,file_out)
    
    result = ddf.antibiotic_analysis(SAMPLE_XLSX,file_out="Antibiotic_markers.xlsx",markers=markers)
    
    assert result == expected_result
    


    