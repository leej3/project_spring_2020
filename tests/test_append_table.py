import pytest
from eeg_gsr_wellness_tracker import append_table
#from eeg_gsr_wellness_tracker import Mood_Focus_Table
import pandas
import mne
import numpy
from pathlib import Path
from openpyxl import load_workbook

WORKBOOK_PATH = Path(__file__).parent / 'data' / 'Mood_Focus_Table.xlsx'
RAWDATA_PATH = WORKBOOK_PATH.with_name('AusEC.edf')


def test_read_raw_eeg_file():
    first_3_values = [-1.21509270e-05, -1.13508659e-05, -1.09508354e-05]
    
    # Read some sample data
    data = append_table.read_raw_eeg_file(RAWDATA_PATH)
    raw_data = data.get_data()

    # check that the first 3 values of the first row are as expected
    assert numpy.allclose(first_3_values, raw_data[0,:3])
    assert RAWDATA_PATH.exists()
   
    
    
@pytest.mark.parametrize("Picks", ["EEG F3-LE"])
@pytest.mark.parametrize("excel_file", ["Mood_Focus_Table.xlsx"])
def test_extract_mean_amplitude_to_data(Picks, excel_file):
    #file_dir = excel_file / 'file'
    #extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE')
    assert isinstance(Picks,  str)
    #assert isinstance(sumdf, )
    assert type("time") is str
    # assert MeanPzdf != 0
    # assert MeanPzdf == Pzdf.mean()
    #assert picks==Picks
    #assert Path(excel_file).is_file()
    #assert isin(df.columns)
    #assert isinstance (Picks, channel) Pick.type() == "channel
   
    #assert excel_file.is_file()
    #filename = 'Mood_Focus_Table.xlsx'
    #first_ten_values = [1,2,3,2,2,0,0,0,-10,20]   
    #filename = 'Mood_Focus_Table.xlsx'
    #first_value = ['4.62613']
    #sheet_value = sheet.cell(row=27, column=5).value
    #assert first_value == sheet_value
