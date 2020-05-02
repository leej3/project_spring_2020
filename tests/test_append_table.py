import pytest
from eeg_gsr_wellness_tracker import append_table
import pandas
import mne
import numpy
from pathlib import Path


'''
def extract_mean_amplitude_to_data():
   # assert append_table.extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE') type(sumdf) is pandas.core.frame.DataFrame
    assert append_table.extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE') type(raw) is mne.io.edf.edf.RawEDF
    assert append_table.extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE') type("time") is numpy.int64
'''



def read_raw_eeg_file(eeg_file_path):
    assert isinstance(eeg_file_path,  str)
    assert isinstance(raw,  RawEDF)
    
    
    
@pytest.mark.parametrize("Picks", ["EEG Fp2-LE"])
@pytest.mark.parametrize("excel_file", ["Mood_Focus_Table.xlsx"])
def test_extract_mean_amplitude_to_data(Picks, excel_file):
    #file_dir = excel_file / 'file'
    #extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE')
    assert isinstance(Picks,  str)
    #assert isinstance(sumdf, )
    assert type("time") is str
    assert MeanPzdf != 0
    assert MeanPzdf == Pzdf.mean()
    #assert picks==Picks
    #assert Path(excel_file).is_file()
    #assert isin(df.columns)
    #assert isinstance (Picks, channel) Pick.type() == "channel
    #assert excel_file.is_file()