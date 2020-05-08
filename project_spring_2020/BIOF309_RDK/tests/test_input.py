
from EHT_RDK.input_files import *

def test_input_list():
    directory_name = "/Users/dewanr2/Documents/Ramitas_Docs/NIH_Classes/BIOF309/Input_test"
    obs = create_input_list(directory_name)
    exp = []
    assert obs == exp
    
def test_df_list():
    dir_name = "/Users/dewanr2/Documents/Ramitas_Docs/NIH_Classes/BIOF309/create_df_test"
    file_list = ['AFF2.txt']
    obs = create_dataframe_list(file_list, dir_name)
    exp = NotImplemented
    assert obs == exp
