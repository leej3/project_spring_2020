#written for python 3.7; run from scripts folder (/data/MoodGroup/07M0021_meg_analysis/MID_data/scripts)

#output of this script includes marker files (for marker placement in MEG file processing) and behavioral data results (adds them to master spreadsheet
#MEG preprocessing script must be run first so that the cue files exist
#notes for tomorrow: need to figure out loop, add in cue txt part, and send results to an aggregate output

#CW 2.18.20 :)

#notes: RTs of 0 were excluded from means

import csv
import numpy as np
import pandas as pd
import statistics

#set some variables
rootdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/'
subjectlist=open('/data/MoodGroup/07M0021_meg_analysis/MID_data/processinglist.txt', 'r')
processinglist=subjectlist.readlines()
processinglist=map(lambda x: x.strip(), processinglist)

#loop begins here!
for subject in processinglist:
   subdir=rootdir + 'sub-' + subject


##############################
#STEP 1: MAKE MARKER TXT FILES
#read cue_marks text file (this is generated during the first step of meg preprocessing)
stimtime=pd.read_csv(subdir + '/meg/cue_marks',delimiter=' ',names=["Onset","Time"])


#read MID behavior file
data_read=pd.read_csv(subdir + '/behavior/MID1-' + subject + '-1_behavior.txt',delimiter='\t',skiprows=1,encoding='utf-16',engine='python')


#pull data from cue file and behavior file to make a stimtimes variables (includes all trial types)
trial=data_read[['Cue']]
frames=[trial,stimtime]
stimtimes_full=pd.concat(frames,axis=1)


#from stimtimes_#_full, pulls out win stim times and adds to a matrix (df_#_win)
stimtimes_win=stimtimes_full[stimtimes_full.Cue=='Win2']
df_win=stimtimes_win[stimtimes_win.columns[1:3]]


#repeats the above for lose stims
stimtimes_lose=stimtimes_full[stimtimes_full.Cue=='Lose2']
df_lose=stimtimes_lose[stimtimes_lose.columns[1:3]]


#repeats the above for control stims
stimtimes_cont=stimtimes_full[stimtimes_full.Cue=='Control']
df_cont=stimtimes_cont[stimtimes_cont.columns[1:3]]


#adds win, lose, and control stim time matrices each to its own text file; these text files are used in MEG preprocessing step 2 to add trial type stim markers
df_win.to_csv(subdir + '/meg/' subject + '_win.txt',index=False,header=False,sep=' ')
df_lose.to_csv(subdir + '/meg/' subject + '_lose.txt',index=False,header=False,sep=' ')
df_cont.to_csv(subdir + '/meg/' subject + '_cont.txt',index=False,header=False,sep=' ')


#####################################################
#STEP 2: PROCESS MID BEHAVIORAL DATA AND OUTPUT STATS
#read raw MID behavior data file and assign to behavior_subj#
data_read=pd.read_csv('/data/MoodGroup/07M0021_meg_analysis/data_to_work_with/NatHx/sub-1023/behavior/MID1-1023-1_behavior.txt',delimiter='	',skiprows=1,encoding='utf-16',engine='python')
behavior_1023=data_read[['Cue','ResponseType','TrialCategory','Target.RT']]


#assign win/loss/control hits and misses to variables respectively
behavior_1023_win=behavior_1023[behavior_1023.Cue=='Win2']
behavior_1023_win_hit=behavior_1023_win[behavior_1023_win.ResponseType=='GoodResponse']
behavior_1023_win_miss=behavior_1023_win[behavior_1023_win.ResponseType=='NoResponse']

behavior_1023_lose=behavior_1023[behavior_1023.Cue=='Lose2']
behavior_1023_lose_hit=behavior_1023_lose[behavior_1023_lose.ResponseType=='GoodResponse']
behavior_1023_lose_miss=behavior_1023_lose[behavior_1023_lose.ResponseType=='NoResponse']

behavior_1023_cont=behavior_1023[behavior_1023.Cue=='Control']
behavior_1023_cont_hit=behavior_1023_cont[behavior_1023_cont.ResponseType=='GoodResponse']
behavior_1023_cont_miss=behavior_1023_cont[behavior_1023_cont.ResponseType=='NoResponse']


#calculate reaction times and accuracy for each trial type and assign to variables respectively
win_hit_RT_1023=behavior_1023_win_hit['Target.RT'][behavior_1023_win_hit['Target.RT']!=0].mean()
win_hit_acc_1023=behavior_1023_win_hit.count()
win_miss_RT_1023=behavior_1023_win_miss['Target.RT'][behavior_1023_win_miss['Target.RT']!=0].mean()
win_miss_acc_1023=behavior_1023_win_miss.count()
lose_hit_RT_1023=behavior_1023_lose_hit['Target.RT'][behavior_1023_lose_hit['Target.RT']!=0].mean()
lose_hit_acc_1023=behavior_1023_lose_hit.count()
lose_miss_RT_1023=behavior_1023_lose_miss['Target.RT'][behavior_1023_lose_miss['Target.RT']!=0].mean()
lose_miss_acc_1023=behavior_1023_lose_miss.count()
cont_hit_RT_1023=behavior_1023_cont_hit['Target.RT'][behavior_1023_cont_hit['Target.RT']!=0].mean()
cont_hit_acc_1023=behavior_1023_cont_hit.count()
cont_miss_RT_1023=behavior_1023_cont_miss['Target.RT'][behavior_1023_cont_miss['Target.RT']!=0].mean()
cont_miss_acc_1023=behavior_1023_cont_miss.count()


#create dataframe for holding these variables; Type = type of trial (win, lose, control), Outcome = outcome of trial (hit, miss), RT = mean reaction times for each trial type/outcome, Acc = mean accuracy for each trial type/outcome
d_1023={'Type':['Win','Win','Lose','Lose','Cont','Cont'],
   'Outcome':['Hit','Miss','Hit','Miss','Hit','Miss'],
   'RT':[win_hit_RT_1023,win_miss_RT_1023,lose_hit_RT_1023,lose_miss_RT_1023,cont_hit_RT_1023,cont_miss_RT_1023],
   'Acc':[win_hit_acc_1023.Cue,win_miss_acc_1023.Cue,lose_hit_acc_1023.Cue,lose_miss_acc_1023.Cue,cont_hit_acc_1023.Cue,cont_miss_acc_1023.Cue]}
df_1023=pd.DataFrame(d_1023)
df_1023


#put dataframe from above into a csv
df_1023.to_csv('/data/MoodGroup/07M0021_meg_analysis/data_to_work_with/NatHx/sub-1023/behavior/behavior_1023_MID.csv',index=False)


#calculate mean RTs for each trial type (collapsing outcome)
win_RT_1023=behavior_1023_win['Target.RT'][behavior_1023_win['Target.RT']!=0].mean()
lose_RT_1023=behavior_1023_lose['Target.RT'][behavior_1023_lose['Target.RT']!=0].mean()
cont_RT_1023=behavior_1023_cont['Target.RT'][behavior_1023_cont['Target.RT']!=0].mean()


#calculate average accuracy for each trial type (what is .Cue??)
win_acc_1023=win_hit_acc_1023.Cue/26
lose_acc_1023=lose_hit_acc_1023.Cue/26
cont_acc_1023=cont_hit_acc_1023.Cue/26


#make new dataframe (I think this may have been a correction of the first one)
d_1023_2={'Type':['Win','Lose','Cont'],
   'RT':[win_RT_1023,lose_RT_1023,cont_RT_1023],'Acc':[win_acc_1023,lose_acc_1023,cont_acc_1023]}
df_1023_2=pd.DataFrame(d_1023_2)


#put dataframe from above into a csv in subject's behavior directory
df_1023_2.to_csv('/data/MoodGroup/07M0021_meg_analysis/data_to_work_with/NatHx/sub-1023/behavior/behavior_1023_MID_meanRT_acc.csv',index=False)


#put dataframe from above into a csv in aggregate behavior data folder
df_1023_2.to_csv('/data/MoodGroup/07M0021_meg_analysis/data_to_work_with/Behavior_Cleaned_All/behavior_1023_MID_meanRT_acc.csv',index=False)

