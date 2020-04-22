# the purpose of the Pearson_and_scatterplt function is to allow one to do simple analysis of pearson correlation
# as well as scatterplot between columns/variables of interest in the 'Mood_Focus_Table' which tabulates rows / instances
# of recorded biometrics with a respective timestamp as well as subjective mood and focus ratings in a likert-scale manner.
# This function allows to explore a relationship between the likert-scale ratings of mood or focus with particular biometrics
# such as the overall alpha power at 'Pz' (10-20 site) which recent recent MIT studies have found to correlate with a state of focus
# neurofeedback trials: http://news.mit.edu/2019/controlling-attention-brain-waves-1204
# and also other sources, several of which I list on my website as they relate to neurofeedback for improving focus: Better State of Mind:
# https://www.better-state-of-mind.com/neurofeedback-overview-and-research


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


# Directing MNE to read the data file 'AusEC.edf' and providing path to it on the desktop, and then creating a raw data object
mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf', montage='deprecated', eog=None, misc=None, stim_channel='auto', exclude=(), preload=False, verbose=None)
raw = mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf')


#Reading the excel file which includes columns specifying subjective mood and focus likert-scale-values as well as those of GSR, EEG, and Date_Time values
MFT = pd.read_excel('Mood_Focus_Table.xlsx')


# Defining variables/columns for exploration of possible trends
GSR = MFT['GSR_Values']
Mood = MFT['Mood_self_rating']
Focus = MFT['Focus_self_rating']
Time = MFT['Date_Time']
Avg_tot_amp = MFT['Average_Total_Amplitude']
Alpha_amp = MFT['Alpha_Amplitude']


#Creating Mood_Focus_Table customized (set by user) analysis of Pearson R and R^2

#First, print an introductory prompt for user to input the columns that wishes to do pearson r and scatterplot
# analyses on
print("Below are the columns/data from which you may choose two to perform a pearson correlation analysis and scatterplot on. Choose two columns to begin and watch your spe")
print(MFT.columns)

# Next, prompting user to input their variables of choice
Chosen_X = globals()[input("Type in your first (or x-axis) variable: ")]
Chosen_y = globals()[input("Type in your second (or y-axis) variable: ")]

#Outputting the pearson correlation analysis information
print("Mood and focus self ratings have a pearson r and r^2 respectively of: " )
print(pearsonr(Chosen_X, Chosen_y))
#print(pearsonr(Mood, Focus))

# outputting the scatter plot for variables that user input
plt.scatter(Chosen_X, Chosen_y)

# This is a function to access variable name, to put onto scatterplot graph automatically
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

# Setting Axis Labels and Title
plt.xlabel(namestr(Chosen_X, globals()))
plt.ylabel(namestr(Chosen_y, globals()))
X_var_name = namestr(Chosen_X, globals())
Y_var_name = namestr(Chosen_y, globals())
plt.title(str(X_var_name) + "vs" + str(Y_var_name))


# Show scatterplot and clean up
plt.show()
plt.clf()

