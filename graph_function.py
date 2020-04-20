
import os.path as op
import numpy as np
import mne
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import matplotlib.pyplot as plt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pydoc import help
from scipy.stats.stats import pearsonr
#help(pearsonr)


#getting MNE to read the data file 'AusEC.edf' and providing directions to it on the desktop
mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf', montage='deprecated', eog=None, misc=None, stim_channel='auto', exclude=(), preload=False, verbose=None)

#Parsing out data into Epochs or short intervals that can later be looked at with a timeline, and setting a montage by which to view data
new_events = mne.make_fixed_length_events(raw, start=5, stop=50, duration=2.)
epochs = mne.Epochs(raw, new_events, event_id=None, tmin=-0.2, tmax=0.5, baseline=(None, 0), picks=None, preload=False, reject=None, flat=None, proj=True, decim=1, reject_tmin=None, reject_tmax=None, detrend=None, on_missing='error', reject_by_annotation=True, metadata=None, event_repeated='error', verbose=None)
montage = mne.channels.read_montage(kind='AusEC.edf', ch_names=None, path='/Users/barlehmann/desktop/AusEC.edf', unit='m', transform=False)

#this plot shows that the data from the file is indeed being processed
raw.plot_psd(fmax=40) 


#******************************
#******************************
#******************************

#MAIN ISSUE I AM TRYING TO SOLVE HERE:
# I'm attempting to solve the problem of being able to plot a specific electrode's amplitude data, this is quite problematic right now. The problem appears to be "RuntimeWarning: Channel locations not available. Disabling spatial colors." Yet I have spent hours on the MNE tutorials and messageboards, and have not been able to resolve this yet. 
epochs.plot_image(picks=['EEG F3-LE'])
#though another error is NotADirectoryError: [Errno 20] Not a directory: '/Users/barlehmann/desktop/AusEC.edf' - this is also confusing because it appears that the EEG file 'AusEC.edf' is clearly being accessed and processed, so it is unclear what the problem is related to the directory. 