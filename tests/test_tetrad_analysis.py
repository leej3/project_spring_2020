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

    expected_tail = SAMPLE_DF_TAIL.set_index("Plate")
    


    result = dataframe_functions.read_excel_file(SAMPLE_XLSX)
    
    assert result.tail(3) == expected_tail