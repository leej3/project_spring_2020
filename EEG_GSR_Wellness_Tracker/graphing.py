# This graph_function is one created to help in plotting / graphing elements of a EEG recording,
# it contains an array of useful plot types with comments briefly summarizing the purpose or use of the plot. 
# this function has an emphasis on graphing power/amplitude (in uV) and also frequency (in Hz) data, from specified
# picks / selections of electrodes. 

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

def read_edf():
    #getting MNE to read the data file 'AusEC.edf' and providing directions to it on the desktop
    mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf', montage='deprecated', eog=None, misc=None, stim_channel='auto', exclude=(), preload=False, verbose=None)
    raw = mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf')


    #Parsing out data into Epochs or short intervals that can later be looked at with a timeline, and setting a montage by 
    # which to view data. The epochs take the argument of events or in the case below 'new_events' which specify the duration
    # of each time segment which in the case below is 2 seconds between the time of 5 and 50 seconds of the recording. 
    new_events = mne.make_fixed_length_events(raw, start=5, stop=50, duration=2.)
    epochs = mne.Epochs(raw, new_events, event_id=None, tmin=-0.2, tmax=5, baseline=(None, 0), picks=None, preload=False, reject=None, flat=None, proj=True, decim=1, reject_tmin=None, reject_tmax=None, detrend=None, on_missing='error', reject_by_annotation=True, metadata=None, event_repeated='error', verbose=None)

def plot_data():
    #This plot shows the Power Spectra Density (PSD) for all channels in a given recording comparing Frequency (Hz) on the 
    # x-axis and Amplitude/Power (uV^2) on the y-axis. In this case the minimum frequency has been set to 40. This plot function
    # also takes the argument of 'average,' which, when set to True, gives the average line of PSD for all included electrodes. 
    raw.plot_psd(fmax=40) 
    raw.plot_psd(average=True)

    #plotting the PSD plots can also be done with selections of individual electrodes or as a group, below are two example 
    # midline electrodes being plotted as a group as well as a single electrode being plotted. The x and y axes are the same
    # as before, simply with subtracted number of channels plotted.
    midline = ['EEG F3-LE', 'EEG F4-LE', 'EEG C3-LE', 'EEG C4-LE', ]
    raw.plot_psd(picks=midline)
    raw.plot_psd(picks='EEG F3-LE')


    #When segmented into epochs, or brief time segments of data, the epoched data has particular plots that can be applied to view
    # a particular electrode of interest such as below in viewing the F3 and F4 electrodes compared with the linked ears ('LE') reference
    epochs.plot_image(picks=['EEG F3-LE'])
    epochs.plot_image(picks=['EEG F4-LE'])
    # These plots work yet do not show the location of the specified sensor ('F3' or 'F4' 10-20 system sensor locations) in the above cases
    # An error shows as - RuntimeWarning: Cannot find channel coordinates in the supplied Evokeds. Not showing channel locations.

    #epoched data can also be used to plot PSD data above with similar arguments for the min and max frequencies to be plotted, average PSD option
    # and options to show spatial colors. 
    epochs.plot_psd(fmin=2., fmax=40., average=True, spatial_colors=True)




#******************************
#******************************
#******************************

## PROBLEMATIC PLOTTING BELOW:
def plot_channels():
    # I'm attempting to solve the problem of being able to plot certain graphs/plots but not being able to,
    # this is quite problematic right now. The problem appears to be "RuntimeWarning: Channel locations not 
    # available. Disabling spatial colors." Yet I have spent hours on the MNE tutorials and messageboards, and 
    # have not been able to resolve this yet. 


    #this first plot contains the same types of issues with identifying the channel locations 
    epochs.plot_psd_topomap(ch_type='grad', normalize=True)


    # this next "raw.plot_projs_topomap()" plot and similar plot has problems with 'digitization points' which are related to the montage setting and channel locations
    # per the error messages. I have many different lines of code as comments below which I tried from googling this error message, but 
    # have not been able to resolve this. 
    raw.plot_projs_topomap()


    # Some of the online reccomendations for fixing the channels not being found or the digitization point issue refer to setting a montage
    # I have tried many different montages to no avail. 
    montage = mne.channels.read_montage(kind='AusEC.edf', ch_names=None, path='datapath', unit='m', transform=False)
    print(montage)
    raw.set_montage(montage, set_dig=True)
    print(montage)


    # When trying to do the independent component analysis to clean up the data (ICA) -THE  DIGITIZATION POINT ERROR OCCURES AS WELL
    ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
    ica.fit(raw)
    ica.exclude = [1, 2]  # details on how these channels are picked  are omitted here
    ica.plot_properties(raw, picks=ica.exclude)


def if_executable():
    data = read_edf()
    output = other_function(data)
    save_output(output)


if __name__ == '__main__':
    if_executable()

