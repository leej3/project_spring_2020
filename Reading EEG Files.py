
import os.path as op
import numpy as np
import mne
from mne.time_frequency import tfr_morlet, psd_multitaper, psd_welch
import matplotlib.pyplot as plt



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

mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf', montage='deprecated', eog=None, misc=None, stim_channel='auto', exclude=(), preload=False, verbose=None)

raw = mne.io.read_raw_edf('/Users/barlehmann/desktop/AusEC.edf')
#mne.viz.ClickableImage(BL61EO.edf, **kwargs)
#These all work well!
#raw.plot_psd(fmax=200)  # THIS WORKS: TO SHOW AMPLITUDE THROUGHOUT THE RECORDING OR SOMETHING LIKE THAT
#print(raw)
#print(raw.info)     #THIS WORKS: TO SHOW MUCH INFO ABOUT THE FILE
new_events = mne.make_fixed_length_events(raw, start=5, stop=50, duration=2.)
#eventss = mne.events_from_annotations(raw)
#events = mne.find_events(new_events)
epochs = mne.Epochs(raw, new_events, event_id=None, tmin=-0.2, tmax=0.5, baseline=(None, 0), picks=None, preload=False, reject=None, flat=None, proj=True, decim=1, reject_tmin=None, reject_tmax=None, detrend=None, on_missing='error', reject_by_annotation=True, metadata=None, event_repeated='error', verbose=None)
#mne.viz.plot_epochs(epochs, picks=None, scalings=None, n_epochs=2, n_channels=2, title=None, events=None, event_colors=None, order=None, show=True, block=False, decim='auto', noise_cov=None, butterfly=False, show_scrollbars=True, epoch_colors=None)
# THIS ONE ABOVE SHOWS THE EPOCHS FOR EACH CHANNEL (EPOCHS = TIME),
# AND THE PLOT IS WAYY LESS FUZZY THAN THE raw.plot() PLOT!!!!!
# OR THE FILTERED PLOTS WHEN FILTERING EITHER RAW OR WITH EPOCHS

#epochs.plot_image(1, cmap='interactive', sigma=1., vmin=-250, vmax=250)
#This one gives 2 in one fancy color plot of uV vs epochs, but for some
# reason is only giving a very small time segment


#epochs.plot_psd_topomap(ch_type='grad', normalize=True)
#mne.time_frequency.psd_multitaper()

power.plot_joint(baseline=(-0.5, 0), mode='mean', tmin=-.5, tmax=2,
                 timefreqs=[(.5, 10), (1.3, 8)])

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
#ica = mne.preprocessing.ICA(n_components=1, random_state=97, max_iter=800)
#ica.fit(raw)
#ica.exclude = [1]  # details on how we picked these are omitted here
#ica.plot_properties(raw, picks=ica.exclude)

#raw.load_data()
#ica.apply(raw)
# show some frontal channels to clearly illustrate the artifact removal
#chs = ['EEG T3-LE', 'EEG T4-LE']
#chan_idxs = [raw.ch_names.index(ch) for ch in chs]
#orig_raw.plot(order=chan_idxs, start=12, duration=4)
#raw.plot(order=chan_idxs, start=12, duration=4)



#ENTROPY ANALYSES FROM ENTROPY
from entropy import *
#np.random.seed(1234567)
#x = np.random.rand(3000)
#print(perm_entropy(raw, order=3, normalize=True))                 # Permutation entropy
#print(spectral_entropy(raw, sf, normalize=True)) # Spectral entropy


#ENTROPY ANALYSES FROM NeuroKit
import neurokit as nk

