#CW 4.19.2020
#written for python 3.7 but works in older versions
#makes swarm file in swarm folder for copying OG MID dataset into a new dataset; this can be run from anywhere
#if you run this twice on the same date, it will overwrite the old files (on purpose!)
#make sure proocessinglist.txt in swarm folder has subjects you want to include, and make sure variables in beginning are all set to values you want

import os
from datetime import datetime

#set variables here:
origds='_MID-f.ds'
newds='_MID_cue-f'
marker='cue'
timewindow='-0.2 4.05'


#set directories we're going to use
subdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/subjects/'
swarmdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/scripts/swarm/'

#set current date for use in filenames
date_today=datetime.now().strftime('%m%d%Y')

#set list of subjects we want included (edit processinglist.txt to change this)
proc_file=open(swarmdir +'processinglist.txt','r')
proc_list=proc_file.read().splitlines()
proc_file.close()


#create newDs swarm file and add info about how to run it
swarmfile_name=str(swarmdir + 'newDs_' + date_today + '.swarm')
swarmfile=open(swarmfile_name,'w+')	
swarmcommand='Run newDs swarm using this command: swarm -f ' + swarmfile_name + ' -g 15 -t auto --module ctf --logdir ' + swarmdir + 'swarm_logs'
swarmfile.write('#' + swarmcommand + '\n')
swarmfile.close()

#append line to swarm file for each subject for newDs command
for sub in proc_list:
	swarmfile=open(swarmfile_name,'a')
	swarmfile.write('set -e ; cd ' + subdir + 'sub-' + sub + '/meg ; newDs -marker ' + marker + ' -time ' + timewindow + ' ' + sub+origds + ' ' + sub+newds + '\n')
	swarmfile.close()


#print message that it is complete, and include command for running each swarm file
print('Swarm file has been added! \n')
print(swarmcommand)
