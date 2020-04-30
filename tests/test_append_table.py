import append_table

def test_read_raw_eeg_file():
    #assert type(sumdf) is 'pandas.core.frame.DataFrame'
    assert type(raw) is mne.io.edf.edf.RawEDF
#    assert type("time") is numpy.int64