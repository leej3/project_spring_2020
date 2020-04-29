'''
This module contains functions to help in plotting / graphing elements of a EEG recording,
it contains an array of useful plot types with comments briefly summarizing the purpose or use of the plot. 
this function has an emphasis on graphing power/amplitude (in uV) and also frequency (in Hz) data, from specified
picks / selections of electrodes. 
'''

import os.path as op
import os
import numpy as np
import mne
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pydoc import help
from scipy.stats.stats import pearsonr


def read_raw_eeg_file(eeg_file_path):
    '''
    getting MNE to read the data file 'AusEC.edf', be sure to put the eeg_file_path in single quotes and also having it as an absolute path
    i.e. '/Users/barlehmann/desktop/JiEC.edf'
    This is an example of a way to use the read_raw_eeg_file function is as a comment:
    read_raw_eeg_file('/Users/barlehmann/desktop/AusEC.edf')
    raw.plot_psd(fmax=40)
    print(raw.info)
    '''
    pass
    mne.io.read_raw_edf(eeg_file_path, montage='deprecated', eog=None, misc=None, stim_channel='auto', exclude=(),
                        preload=False, verbose=None)
    global raw
    raw = mne.io.read_raw_edf(eeg_file_path)


def epoch_raw_eeg_file(Picks, start_epochs_seconds, stop_epochs_seconds, epoch_duration):
    '''
    This epoching function is for putting the raw data into epochs of a fixed regular length/interval, which also allows for different graphing functions
    Picks are the channels to include, start_epochs_seconds are the seconds in the recording where the epoching segmentation will begin, stop_epochs_seconds
    are the seconds in the recording where the epoching segmentation will end, epoch_duration is the duration of each segment /epoch being created
    '''
    pass
    global new_events
    new_events = mne.make_fixed_length_events(raw, start=start_epochs_seconds, stop=stop_epochs_seconds,
                                              duration=epoch_duration)
    global epochs
    epochs = mne.Epochs(raw, new_events, event_id=None, tmin=-0.1, tmax=5, baseline=(None, 0), picks=Picks,
                        preload=False, reject=None, flat=None, proj=True, decim=1, reject_tmin=None, reject_tmax=None,
                        detrend=None, on_missing='error', reject_by_annotation=True, metadata=None,
                        event_repeated='error', verbose=None)



def plot_epochs_vs_uV():
    ''' This function takes no arguments. The plot_epochs_vs_uV function is a more intuitive name for a plot of epochs created that plots the epochs in
    regard to amplitude (i.e in uV)
    This is an example using this function alongside the epoch_raw_eeg_file function:
    epoch_raw_eeg_file(Picks = 'EEG F4-LE', start_epochs_seconds=5, stop_epochs_seconds=50, epoch_duration=2)
    epochs.plot_image()
    '''
    pass
    epochs.plot_image()



def plot_epochs_PSD(fmin, fmax):
    '''
    The plot_epochs_PSD function is just a more intuitive name for a plot of epochs PSD  (in uV^2)
    This is an example of a way to use the above function is as a comment right here with fmin at 20 and fmax at 30:
    epochs.plot_psd(20,30)
    '''
    pass
    epochs.plot_psd(fmin=fmin, fmax=fmax, average=False, spatial_colors=True)
