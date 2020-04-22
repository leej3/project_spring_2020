# This Append_Table_function's  purpose is to read an EEG file (in this case below the file: 'AusEC.edf' is used
# and to extract from it overall amplitude data for (a) specific electrode(s) of interest (in this case Pz is the
# 10-20 electrode location of interest) and to insert this information along with the timestamp of the recording
# as a new row in the excel datafile 'Mood_Focus_Table' tabulating biometric data alongside subjective report of
# mood and focus likert-scale ratings.

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


#getting MNE to read the data file 'AusEC.edf' and providing directions to it on the desktop
mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf', montage='deprecated', eog=None, misc=None, stim_channel='auto', exclude=(), preload=False, verbose=None)
raw = mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf')


#Getting average amplitude (in uV) data from a specific sensor into a file and printing it:
data = raw.get_data()
np.save(file='my_data.npy', arr=data)
sampling_freq = raw.info['sfreq']
start_end_secs = np.array([0, 99999])
start_sample, stop_sample = (start_end_secs * sampling_freq).astype(int)
df = raw.to_data_frame(picks=['EEG Pz-LE'], start=start_sample, stop=stop_sample)


#Creating a set of variables to be used in analysis of particular sensors' data from the raw EEG file
F4_channel_data = raw.get_data(picks='EEG F4-LE')
F3_channel_data = raw.get_data(picks='EEG F3-LE')
C3_channel_data = raw.get_data(picks='EEG C3-LE')
C4_channel_data = raw.get_data(picks='EEG C4-LE')
Pz_channel_data = raw.get_data(picks='EEG Pz-LE')


#print(first_channel_data.shape)
#print(F4_channel_data.mean())
#print(F3_channel_data.mean())
#print(C3_channel_data.mean())
#print(C4_channel_data.mean())
print(Pz_channel_data.mean())
Pzdf = pd.DataFrame(data=Pz_channel_data)
MeanPzdf = Pzdf.mean()


#creating data frame from excel sheet with present data in order to append this data, and setting index
df = pd.read_excel('Mood_Focus_Table.xlsx')
df.set_index(df['Date_Time'])

#Creating a dataframe extracting amplitude and data from a particular sensor as well as date_time information from the EEG file
Amplitude_df = pd.DataFrame({'Average_Total_Amplitude': [MeanPzdf.mean()*100000000],
                            'Date_Time': [pd.to_datetime(raw.info['meas_date'][1])]})

# Concatenating dataframes in order to join the existing data with the new data from a new EEG file
sumdf = pd.concat([df, Amplitude_df], join="outer", sort=False, ignore_index=True)

#printing the concatenated data-frames for viewing purposes
print(sumdf)

#exporting data to excel sheet
writer=pd.ExcelWriter('Mood_Focus_Table.xlsx')
sumdf.to_excel(writer, 'Sheet1')

writer.save()

print("Please update Mood_Focus_Table.xlsx manually with subjective mood, subjective focus, and other columns before doing any anlysis, ensure that each column is filled in with its respective entries for the row you have just entered data into!")

# ?? Getting 'extra index' columns, not sure how to get rid of these yet.

