
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


#entries = os.listdir('/Users/barlehmann/desktop/')
#print(entries)

#sample_data_folder = mne.datasets.sample.data_path()
#sample_data_raw_file = os.path.join(/Users/barlehmann/desktop/BL61EO.edf, 'EEG', 'sample',
                                   # '/desktop/BL61EO.edf')
#raw = mne.io.read_raw_fif(/Users/desktop/BL61EO.edf)
#raw = /Users/desktop/BL61EO.edf
#import /Users/barlehmann/desktop/BL61EO.edf
#mne.io.read_raw_edf(BL61EO.edf)
#raw.crop(tmax=60).load_data()

################## mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf', montage='deprecated', eog=None, misc=None, stim_channel='auto', exclude=(), preload=False, verbose=None)

################## raw = mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf')
#mne.viz.ClickableImage(BL61EO.edf, **kwargs)
#These all work well!
#raw.plot_psd(fmax=40) # THIS WORKS: TO SHOW AMPLITUDE THROUGHOUT THE RECORDING OR SOMETHING LIKE THAT
#raw.plot(duration=10, n_channels=20)   # for some reason changing duration from 5 to 10 makes each line thicker but the time is still 0-350seconds on each graph!

#print(raw)
#print(raw.info)     #THIS WORKS: TO SHOW MUCH INFO ABOUT THE FILE
################## new_events = mne.make_fixed_length_events(raw, start=5, stop=50, duration=2.)
#eventss = mne.events_from_annotations(raw)
#events = mne.find_events(new_events)
################## epochs = mne.Epochs(raw, new_events, event_id=None, tmin=-0.2, tmax=0.5, baseline=(None, 0), picks=None, preload=False, reject=None, flat=None, proj=True, decim=1, reject_tmin=None, reject_tmax=None, detrend=None, on_missing='error', reject_by_annotation=True, metadata=None, event_repeated='error', verbose=None)
#mne.viz.plot_epochs(epochs, picks=None, scalings=None, n_epochs=2, n_channels=4, title=None, events=None, event_colors=None, order=None, show=True, block=False, decim='auto', noise_cov=None, butterfly=False, show_scrollbars=True, epoch_colors=None)
# THIS ONE ABOVE SHOWS THE EPOCHS FOR EACH CHANNEL (EPOCHS = TIME),
# AND THE PLOT IS WAYY LESS FUZZY THAN THE raw.plot() PLOT!!!!!
# OR THE FILTERED PLOTS WHEN FILTERING EITHER RAW OR WITH EPOCHS
# *** ALSO YOU CAN CHANGE NUM OF CHANNELS BY AN ARGUMENT

#epochs.plot_image(1, cmap='interactive', sigma=1., vmin=-250, vmax=250)
# *** This one gives 2 in one fancy color plot of uV vs epochs, but for some
#*** reason is only giving a very small time segment,
#*** the first argument '1' signifies which electrode is being looked at 1 = fp2, and 2 = f3 (both compared to LE)
#*** also if you change the tmax in Epochs above, you will extend the time shown in the graph



#epochs.plot_psd_topomap(ch_type='grad', normalize=True)
#mne.time_frequency.psd_multitaper()

#power.plot_joint(baseline=(-0.5, 0), mode='mean', tmin=-.5, tmax=2,
#                 timefreqs=[(.5, 10), (1.3, 8)])



#raw.plot_psd_topo()
#RuntimeError: No digitization points found.

#raw.plot_sensors(ch_type='eeg')
#22 matching events found
#Applying baseline correction (mode: mean)
#Not setting metadata
#0 projection items activated

#BELOW NOT WORKING :AttributeError: module 'mne.preprocessing' has no attribute 'create_eeg_epochs' AND THIS IS AFTER CHANGING RAW FOR NEW_EVENTS
#eeg_epochs = mne.preprocessing.create_eeg_epochs(raw)
#eeg_epochs.plot_image(combine='mean')
######NameError: name 'event_dict' is not defined



#fig = mne.viz.plot_events(events = new_events, sfreq=raw.info['sfreq'],
 #                         first_samp=raw.first_samp, event_id=event_dict)
#fig.subplots_adjust(right=0.7)  # make room for legend




# THIS ONE WORKS AND SHOWS THE TWO CHANNELS FULL OF 60HZ INTERFERENCE
#THIS ONE IS SUPPOSED TO BE PUTTING TOGETHER BOTH EVENTS AND RAW DATA IN SAME PLOT
# BUT HARD TO SEE THIS, PRESUMABLY THE EVENTS ARE RED BUT UNCLEAR WHAT THEY REPRESENT
#raw.plot(events=new_events, start=5, duration=10, color='gray',
 #        event_color={1: 'r', 2: 'g', 3: 'b', 4: 'm', 5: 'y', 32: 'k'})
#BELOW -JUST THE RAW PLOT IS SAME THING BUT WITHOUT RED LINES FOR THE DIFFERENT EVENTS!
#raw.plot()


#plot()
# says plot is not defined if do not put raw.plot()!!!!!!!!!

#raw.plot_psd()
#we have seen above that this works to plot the PSD

#raw.plot_psd_topo()
# RuntimeError: No digitization points found.

#raw.plot_sensors()
#22 matching events found
#Applying baseline correction (mode: mean)
#Not setting metadata
#0 projection items activated

#raw.plot_projs_topomap()
#22 matching events found
#Applying baseline correction (mode: mean)
#Not setting metadata
#0 projection items activated


#mne.compute_proj_raw(raw)
#print(raw.info['projs'])
# AND THIS ALSO GIVES PRERTY MUCH SAME THING: mne.compute_proj_epochs(raw)
#22 matching events found
#Applying baseline correction (mode: mean)
#Not setting metadata
#0 projection items activated
#1606 matching events found
#No baseline correction applied
#Not setting metadata
#No gradiometers found. Forcing n_grad to 0
#No magnetometers found. Forcing n_mag to 0

#raw.load_data()   # NOT SURE WHY BUT THIS LINE NEEDS TO BE HERE FOR THE FILTERING TO TAKE PLACE!!!
#raw.notch_filter(np.arange(60), fir_design='firwin')
#raw.filter(1, 50, fir_design='firwin') # THIS ONE ACTUALLY LEADS TO FILTERING ANYTHING OUTSIDE OF 1-50!!!
#HOWEVER, EVEN WHEN FILTERED 1-30 IT STILL DOES NOT LOOK AS CLEAR AS OTHER PLOTS I'VE GOTTEN FOR SAME DATA HERE  - NOT SURE WHY THIS IS.
#raw.plot()
# LOOKS DIFF IF EXCHANGE 'EPOCHS' FOR 'RAW' IN THE FILTERING, BUT
# NEITHER IS NOT NEARLY AS CLEAR AS ABOVE MNE.VIZ.PLOT COMMAND!

# This part below gives "Assertion Error" and lists many files which
# I do not recognize but does not specify the error
#ica = mne.preprocessing.ICA(n_components=1, random_state=5, max_iter=70)
#ica.fit(raw)
#ica.exclude = [1]  # details on how we picked these are omitted here
#ica.plot_properties(raw, picks=ica.exclude) # This last line is most problematic and comes up with the errors

#raw.load_data()
#ica.apply(raw)
# show some frontal channels to clearly illustrate the artifact removal
#chs = ['EEG T3-LE', 'EEG T4-LE']
#chan_idxs = [raw.ch_names.index(ch) for ch in chs]
#orig_raw.plot(order=chan_idxs, start=12, duration=4)
#raw.plot(order=chan_idxs, start=12, duration=4)


# power.plot_topo(baseline=(-0.5, 0), mode='logratio', title='Average power')
# this one says "power" is not defined

#itc.plot_topo(title='Inter-Trial coherence', vmin=0., vmax=1., cmap='Reds')
# this one says "itc" is not defined


################## montage = mne.channels.read_montage(kind='filename', ch_names=None, path='/Users/barlehmann/desktop/AusEC.edf', unit='m', transform=False)
#print(montage)

#raw.set_montage(montage, set_dig=True)

#freqs = np.logspace(*np.log10([6, 35]), num=8)
#n_cycles = freqs / 2.  # different number of cycle per frequency
#power, itc = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles, use_fft=True,
#                        return_itc=True, decim=3, n_jobs=1)
#power.plot_topo(baseline=(-0.5, 0), mode='logratio', title='Average power')
#ValueError: At least one of the wavelets is longer than the signal. Use a longer signal or shorter wavelets.


################## epochs.plot_psd_topomap(ch_type='grad', normalize=True)
# RuntimeError: No digitization points found.



#mne.time_frequency.tfr_morlet(epochs, freqs=freqs, n_cycles=1)


# create the REM annotations
#rem_annot = mne.Annotations(onset=[5, 41],
 #                           duration=[16, 11],
 #                           description=['REM'] * 2)
#raw.set_annotations(rem_annot)
#(rem_events,
 #rem_event_dict) = mne.events_from_annotations(raw, chunk_duration=1.5)

#print(raw.annotations)



#ENTROPY ANALYSES FROM ENTROPY
from entropy import *
#np.random.seed(1234567)
#x = np.random.rand(3000)
#print(perm_entropy(raw, order=3, normalize=True))                 # Permutation entropy
#print(spectral_entropy(raw, sf, normalize=True)) # Spectral entropy


#ENTROPY ANALYSES FROM NeuroKit
import neurokit as nk

#Reading and anlysing Excel Datasheet to analyse in relation to specific biometric events/data

#Reading the excel file including subjective mood and focus values, GSR, EEG, Date, and Time values
MFT = pd.read_excel('Mood_Focus_Table.xlsx')

# Defining variables for manipulation
GSR = MFT['GSR_Values']
Mood = MFT['Mood_self_rating']
Focus = MFT['Focus_self_rating']
Time = MFT['Time']
Date = MFT['Date']
Avg_tot_amp = MFT['Average_Total_Amplitude']
Alpha_amp = MFT['Alpha_Amplitude']

#Items = {1: 'Date', 2: 'Time', 3: 'Mood', 4: 'Focus', 5: 'Alpha_amp', 6: 'Avg_tot_amp', 7: 'GSR'}
#Items = [[Date, Time, Mood, Focus, Alpha_amp, Avg_tot_amp, GSR]]


# Make a line plot: year on the x-axis, pop on the y-axis
#plt.plot(Avg_tot_amp, Alpha_amp, GSR, Mood, Focus)

#Above scatter plot works so long as I keep it to no more than 3 variables,, not sure why that is


# Create histogram of life_exp data
#plt.hist(life_exp)

# Build histogram with 5 bins
#plt.hist(life_exp, 5)




#plt.xscale('log')

# Definition of tick_val and tick_lab
#tick_val = [1000, 10000, 100000]
#tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
#plt.xticks(tick_val, tick_lab)

# Add axis labels
#plt.xlabel(xlab)
#plt.ylabel(ylab)




#Creating Mood_Focus_Table customized (set by user) analysis of Pearson R and R^2

print("These are the data sets you may choose from the explore and analyse. Choose two to begin with")
print(MFT.columns)

Chosen_X = globals()[input("Type in your first (or x-axis) variable: ")]
Chosen_y = globals()[input("Type in your second (or y-axis) variable: ")]

#if Chosen_X == 'Mood' or Chosen_X == 'Mood':

#    print("Great pick for x")
#elif Chosen_y == 'Mood' or Chosen_y == 'Mood':
#    print("Great pick for y")
#else:
#    print("Uh oh, I don't know about that item")

print("Mood and focus self ratings have a pearson r and r^2 respectively of: " )
print(pearsonr(Chosen_X, Chosen_y))
#print(pearsonr(Mood, Focus))

# Create a scatter plot
plt.scatter(Chosen_X, Chosen_y)

#to access variable name
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

# Set Axis Labels and Title
plt.xlabel(namestr(Chosen_X, globals()))
plt.ylabel(namestr(Chosen_y, globals()))
X_var_name = namestr(Chosen_X, globals())
Y_var_name = namestr(Chosen_y, globals())
#plottitle = concat(X_var_name + "Vs" + Y_var_name)
#plt.xlabel('Average_Total_Amplitude [in uV]')
#plt.ylabel('Alpha_Amplitude [in uV]')
plt.title(str(X_var_name) + "vs" + str(Y_var_name))
# Show and clean up again
plt.show()

# Show and clean up again
#plt.clf()


