#CW 5.6.2020
#written for python 3.7
#makes swarm file in swarm folder for copying OG MID dataset into a new dataset; also makes SAM command swarm files (sam_cov, sam_wts, and sam_3d)
#if you run this twice on the same date, it will overwrite the old files (on purpose!)

import os
from datetime import datetime

#set directories we're going to use
subdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/subjects/'
swarmdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/scripts/swarm/'

#set current date for use in filenames
date_today=datetime.now().strftime('%m%d%Y')

#set default file with list of subjects we want included
rootdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/'
default_sublist=swarmdir +'processinglist.txt'

#set default variables here:
default_origds='_MID-f.ds'
default_newds='_MID_respwin-f'
default_marker='respwin'
default_timewindow='0.5 2'
default_ds='_MID_respwin-f.ds'
marker='respwin'
default_freqband='highgamma'


### MAKE NEWDS SWARM FILE
def make_swarm_newDs(subjectlist=default_sublist, origds=default_origds, newds=default_newds, marker=default_marker, timewindow=default_timewindow):
	"""Makes swarm file for creating new MEG datasets based on input parameters."""
	#create newDs swarm file and add info about how to run it
	swarmfile_name=f'{swarmdir}newDs_{date_today}.swarm'
	swarmfile=open(swarmfile_name,'w+')	
	swarmcommand=f'Run newDs swarm using this command: swarm -f {swarmfile_name} -g 15 -t auto --module ctf --logdir {swarmdir}swarm_logs'
	swarmfile.write(f'#{swarmcommand}\n')
	swarmfile.close()

	#read list of subjects	
	sublist=open(subjectlist, 'r')
	proclist=sublist.readlines()
	proclist=map(lambda x: x.strip(), proclist)

	#append line to swarm file for each subject for newDs command
	for sub in proclist:
		swarmfile=open(swarmfile_name,'a')
		swarmfile.write(f'set -e ; cd {subdir}sub-{sub}/meg ; newDs -marker {marker} -time {timewindow} {sub}{origds} {sub}{newds}\n')
		swarmfile.close()

	#print message that it is complete, and include command for running swarm file
	print('Swarm file has been added! \n')
	print(swarmcommand)


### MAKE SAM SWARM FILES
def make_swarm_sam(subjectlist=default_sublist, ds=default_ds, marker=default_marker, freqband=default_freqband):
	#read list of subjects	
	sublist=open(subjectlist, 'r')
	proclist=sublist.read().splitlines()
	sublist.close()

	#set paramfile name for use in sam command
	paramfile_name=f'{freqband}_{marker}.param'

	#create sam_cov swarm file and add info about how to run it
	swarmfile_name=f'{swarmdir}sam_cov_{freqband}_{marker}_{date_today}.swarm'
	swarmfile=open(swarmfile_name,'w+')	
	swarmcommand_cov=f'Run sam_cov swarm using this command: swarm -f {swarmfile_name} -g 15 -t auto --module samsrcv3 --logdir {swarmdir}swarm_logs'
	swarmfile.write('#' + swarmcommand_cov + '\n')
	swarmfile.close()

	#append line to swarm file for each subject for sam_cov command
	for sub in proclist:
		swarmfile=open(swarmfile_name,'a')
		swarmfile.write(f'set -e ; cd {subdir}sub-{sub}/meg ; sam_cov -r {sub}{ds} -m {paramfile_name} -v \n')
		swarmfile.close()


	#now to make a swarm file for sam_wts
	swarmfile_name=f'{swarmdir}sam_wts_{freqband}_{marker}_{date_today}.swarm'
	swarmfile=open(swarmfile_name,'w+')	
	swarmcommand_wts=f'Run sam_wts swarm using this command: swarm -f {swarmfile_name} -g 15 -t auto --module samsrcv3 --logdir {swarmdir}swarm_logs'
	swarmfile.write(f'#{swarmcommand_wts}\n')
	swarmfile.close()
	for sub in proclist:
		swarmfile=open(swarmfile_name,'a')
		swarmfile.write(f'set -e ; cd {subdir}sub-{sub}/meg ; sam_wts -r {sub}{ds} -m {paramfile_name} -v --MRIPattern %M/%s -H hull.shape \n')
		swarmfile.close()


	#and finally make sam_3d swarm file
	swarmfile_name=f'{swarmdir}sam_3d_{freqband}_{marker}_{date_today}.swarm'
	swarmfile=open(swarmfile_name,'w+')	
	swarmcommand_3d=f'Run sam_3d swarm using this command: swarm -f {swarmfile_name} -g 15 -t auto --module samsrcv3 --logdir {swarmdir}swarm_logs'
	swarmfile.write(f'#{swarmcommand_3d}\n')
	swarmfile.close()
	for sub in proclist:
		swarmfile=open(swarmfile_name,'a')
		swarmfile.write(f'set -e ; cd {subdir}sub-{sub}/meg ; sam_3d -r {sub}{ds} -m {paramfile_name} -v \n')
		swarmfile.close()


	#print message that it is complete, and include commands for running each swarm file
	print('Swarm files have been added! \n')
	print(f'1.) {swarmcommand_cov}\n\n2.) {swarmcommand_wts}\n\n3.) {swarmcommand_3d}')


if __name__=='__main__':
	make_swarm_newDs()
	make_swarm_sam()
