#CW 4.23.2020
#written for python 3.7 but works in older versions
#makes SAM swarm files (cov, wts, and cov) with date of creation and puts them in swarm folder; this can be run from anywhere
#if you run this twice on the same date, it will overwrite the old files (on purpose!)
#make sure proocessinglist.txt in swarm folder has subjects you want to include, and make sure ds variable is set to appropriate suffix

import os
from datetime import datetime

#set directories we're going to use
subdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/subjects/'
swarmdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/scripts/swarm/'

#set Ds file name suffix and paramfilename
ds='_MID_respwin-f.ds'
marker='respwin'
freqband='beta'

paramfile_name=freqband + '_' + marker + '.param'

#set current date for use in filenames
date_today=datetime.now().strftime('%m%d%Y')

#set list of subjects we want included (edit processinglist.txt to change this)
proc_file=open(swarmdir +'processinglist.txt','r')
proc_list=proc_file.read().splitlines()
proc_file.close()


#create sam_cov swarm file and add info about how to run it
swarmfile_name=str(swarmdir + 'sam_cov_' + freqband + '_' + marker + '_' + date_today + '.swarm')
swarmfile=open(swarmfile_name,'w+')	
swarmcommand_cov='Run sam_cov swarm using this command: swarm -f ' + swarmfile_name + ' -g 15 -t auto --module samsrcv3 --logdir ' + swarmdir + 'swarm_logs'
swarmfile.write('#' + swarmcommand_cov + '\n')
swarmfile.close()

#append line to swarm file for each subject for sam_cov command
for sub in proc_list:
	swarmfile=open(swarmfile_name,'a')
	swarmfile.write('set -e ; cd ' + subdir + 'sub-' + sub + '/meg ; sam_cov -r ' + sub + ds + ' -m ' + paramfile_name + ' -v \n')
	swarmfile.close()


#now to make a swarm file for sam_wts
swarmfile_name=str(swarmdir + 'sam_wts_' + freqband + '_' + marker + '_' + date_today + '.swarm')
swarmfile=open(swarmfile_name,'w+')	
swarmcommand_wts='Run sam_wts swarm using this command: swarm -f ' + swarmfile_name + ' -g 15 -t auto --module samsrcv3 --logdir ' + swarmdir + 'swarm_logs'
swarmfile.write('#' + swarmcommand_wts + '\n')
swarmfile.close()

for sub in proc_list:
	swarmfile=open(swarmfile_name,'a')
	swarmfile.write('set -e ; cd ' + subdir + 'sub-' + sub + '/meg ; sam_wts -r ' + sub + ds + ' -m ' + paramfile_name + ' -v --MRIPattern %M/%s -H hull.shape \n')
	swarmfile.close()


#and finally make sam_3d swarm file
swarmfile_name=str(swarmdir + 'sam_3d_' + freqband + '_' + marker + '_' + date_today + '.swarm')
swarmfile=open(swarmfile_name,'w+')	
swarmcommand_3d='Run sam_3d swarm using this command: swarm -f ' + swarmfile_name + ' -g 15 -t auto --module samsrcv3 --logdir ' + swarmdir + 'swarm_logs'
swarmfile.write('#' + swarmcommand_3d + '\n')
swarmfile.close()

for sub in proc_list:
	swarmfile=open(swarmfile_name,'a')
	swarmfile.write('set -e ; cd ' + subdir + 'sub-' + sub + '/meg ; sam_3d -r ' + sub + ds + ' -m ' + paramfile_name + ' -v \n')
	swarmfile.close()


#print message that it is complete, and include commands for running each swarm file
print('Swarm files have been added! \n')
print('1.) ' + swarmcommand_cov + '\n\n2.) ' + swarmcommand_wts + '\n\n3.) ' + swarmcommand_3d)
