import pytest
from eeg_gsr_wellness_tracker import append_table
import pandas
import mne
import numpy


'''
def extract_mean_amplitude_to_data():
   # assert append_table.extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE') type(sumdf) is pandas.core.frame.DataFrame
    assert append_table.extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE') type(raw) is mne.io.edf.edf.RawEDF
    assert append_table.extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE') type("time") is numpy.int64
'''




def read_raw_eeg_file(eeg_file_path):
    assert isinstance(eeg_file_path,  str)
    assert isinstance(raw,  RawEDF)
    
    
def test_extract_mean_amplitude_to_data():
    assert isinstance(Picks,  str)
    #assert isinstance(sumdf, )
    assert type("time") is str
    #assert MeanPzdf = Pzdf.mean()
    #assert picks==Picks


