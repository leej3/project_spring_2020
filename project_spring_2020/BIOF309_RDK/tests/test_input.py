
from EHT_RDK.input_files import *
from pathlib import Path

tests_dir = Path(__file__).parent

def test_input_list():
    directory_name = tests_dir
    obs = create_input_list(directory_name)
    exp = []
    assert obs == exp

def test_df_list():
    dir_name = tests_dir / "create_df_test"
    file_list = ['AFF2.txt']
    obs = create_dataframe_list(file_list, dir_name)
    exp = NotImplemented
    assert obs == exp
