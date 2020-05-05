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
from openpyxl import load_workbook


def read_raw_eeg_file(eeg_file_path):
    '''
    This is an example of a way to use the read_raw_eeg_file function:
    raw = read_raw_eeg_file('AusEC.edf')
    raw.plot_psd(fmax=40)
    print(raw.info)
    '''
    raw = mne.io.read_raw_edf(eeg_file_path)
    return raw



# Getting average amplitude (in uV) data from a specific sensor into a file and printing it:
def extract_mean_amplitude_to_data(Picks, excel_file):
    '''
    This extract_mean_amplitude_to_data function's  purpose is to read an EEG file (using the read_raw_eeg_file such as:
    'AusEC.edf' is used and to extract from it overall amplitude data for (a) specific electrode(s) of interest (in this
    case Pz is the 10-20 electrode location of interest) and to insert this information along with the timestamp of the
    recording as a new row in the excel datafile 'Mood_Focus_Table' tabulating biometric data alongside subjective report
    of mood and focus likert-scale ratings.
    The extract_mean_amplitude_to_data takes the argument Picks which specifies the specific electrode(s) being looked at
    An example of using this function might look like:
    read_raw_eeg_file('AusEC.edf')
    extract_mean_amplitude_to_data(Picks = 'EEG Fp2-LE')
    Of course, the read_raw_eeg_file must specify a particular file to be extracting the mean amplitude from, which is why
    this function is being used before the extraction function. Note that the amplitudes input into the excel sheet are sometimes rounded to the nearest whole number and sometimes not. This inconsistency will be addressed in a later version. 
    '''
    data = raw.get_data()
    Picks_channel_data = raw.get_data(picks=Picks)
    '''
    Note that the raw.get_data function used can also be used more specitifically for creating a set of variables to be used in analysis of particular sensors' data from the raw EEG file
    F3_channel_data = raw.get_data(picks='EEG F3-LE')
    C3_channel_data = raw.get_data(picks='EEG C3-LE')
    '''
    np.save(file='my_data.npy', arr=data)
    sampling_freq = raw.info['sfreq']
    start_end_secs = np.array([0, 99999])
    start_sample, stop_sample = (start_end_secs * sampling_freq).astype(int)
    df = raw.to_data_frame(picks=[Picks], start=start_sample, stop=stop_sample)
    '''
    Note that the mean amplitude can be printed more specifically using functions such as:
    print(F4_channel_data.mean())
    print(F3_channel_data.mean())
    '''
    print(Picks_channel_data.mean())
    Pzdf = pd.DataFrame(data=Picks_channel_data)
    MeanPzdf = Pzdf.mean()

    # creating data frame from excel sheet with present data in order to append this data, and setting index
    df = pd.read_excel(excel_file)
    df.set_index(df['Date_Time'])

    # Creating a dataframe extracting amplitude and data from a particular sensor as well as date_time information from the EEG file
    Amplitude_df = pd.DataFrame({'Average_Total_Amplitude': [MeanPzdf.mean() * 100000000],
                                 'Date_Time': [pd.to_datetime(raw.info['meas_date'][1])]})

    # Concatenating dataframes in order to join the existing data with the new data from a new EEG file
    sumdf = pd.concat([df, Amplitude_df], join="outer", sort=False, ignore_index=True)

    # printing the concatenated data-frames for viewing purposes
    print(sumdf)

    # exporting data to excel sheet
    writer = pd.ExcelWriter('Mood_Focus_Table.xlsx')
    sumdf.to_excel(writer, 'Sheet1', index=False)
    writer.save()

    print(
        "Please update Mood_Focus_Table.xlsx manually with subjective mood, subjective focus, and other columns before doing any anlysis, ensure that each column is filled in with its respective entries for the row you have just entered data into!")

# print(extract_mean_amplitude_to_data.__doc__)
# print(read_raw_eeg_file.__doc__)
