import pandas as pd
import numpy as np
import ast
from pandas import ExcelWriter
from pandas import ExcelFile



def read_excel_file(filepath):
    """
    Reads an excel file and returns a dataframe
    """
    df = pd.read_excel(filepath)
    df_index = df.set_index('Plate')
    return df_index
    

def sort_and_filter_by_col(df_in,col):
    """
    This will sort by the input argument col and filter for positive values
    """
   
    #separate the positive spores from the negative spores
    df_sorted = df_in.sort_values([col], ascending=False)
    pos_vals = df_sorted[df_sorted[col] > 0]

    #now take the positive ones and put them into their own excel document
    df_filtered = pd.DataFrame(pos_vals)
    return df_filtered

    

def combine_antibiotics(df_in,markers):
    """
    This will read an excel file, and for each marker provided will sort and
    filter for positive values. Returns a dictionary where each value is a 
    dataframe for a marker
    """
    
    all_positive = {}
    for marker in markers:
        df_marker = sort_and_filter_by_col(marker)
        all_positive[marker + '_plus'] = df_marker
    
    return all_positive
    

def write_marker_dict_to_disk(markers,file_out):
    """
    Given a dict of dataframes, writes out an excel file in which each 
    dataframe occupies its own sheet
    """
    #turn the dataframes stored in a dict into an excel document
    writer = pd.ExcelWriter(file_out, engine='xlsxwriter')
    
    for sheet_name in markers.keys():
        markers[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()
    

def antibiotic_analysis(file_in,file_out="Antibiotic_markers.xlsx",markers=['NAT','HYG','URA']):
    """
    Reads file_in, and for each marker performs a sort and filter before 
    writing the results to file_out. Each marker occupies its own sheet
    """
    df_tetrad = read_excel_file(file_in)
    output_dict = combine_antibiotics(df_tetrad,markers)
    write_marker_dict_to_disk(output_dict,file_out)
    