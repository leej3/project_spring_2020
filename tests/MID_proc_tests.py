import MID_proc as mid
import os
import shutil
from datetime import datetime

#set current date for use in filenames
date_today=datetime.now().strftime('%m%d%Y')

#set up some example directories and files for use with tests
cwd=os.getcwd()
os.makedirs(f'{cwd}/MID_test_data/scripts/swarm',exist_ok=True)
fake_subdir=f'{cwd}/MID_test_data/subjects/'
fake_swarmdir=f'{cwd}/MID_test_data/scripts/swarm/'
#set sub fake sub ID numbers; these were picked to test that prefix length calculation in make_param() works with a variety of ID lengths
fake_subs=['7','13','101','102','99','990','9999']
with open(f'{cwd}/MID_test_data/scripts/fake_sub_file.txt','w') as fake_sub_file:
	fake_sub_file.write('\n'.join(fake_subs))
fake_sub_file=f'{cwd}/MID_test_data/scripts/fake_sub_file.txt'
for sub in fake_subs:
	os.makedirs(f'{fake_subdir}sub-{sub}/meg',exist_ok=True)
	os.makedirs(f'{fake_subdir}sub-{sub}/behavior',exist_ok=True)

#first test is for the param file maker function
def test_make_param():
	"""This tests if make_param() can make parameter files with a few non-default inputsarguments and put them in fake subjects' meg folders."""
	mid.make_param(rootdir=fake_subdir,Marker1='cue', marker1window='0 4')
	paramfiles_exist=[os.path.exists(f'{fake_subdir}sub-{sub}/meg/highgamma_cue.param') for sub in fake_subs]
	assert paramfiles_exist==[1]*len(fake_subs),'Param files were not created properly--oh no!'

#second test will test the swarm making functions
def test_make_swarms():
	"""This tests if make_swarm_newDs() and make_swarm_sam() make their respective swarm files with a fake subject list and some non-default args"""
	mid.make_swarm_newDs(subjectlist=fake_sub_file,newds='_MID_cue-f',marker='cue',timewindow='0 4',swarmdir=fake_swarmdir)
	mid.make_swarm_sam(subjectlist=fake_sub_file,ds='_MID_cue-f.ds',marker='cue',swarmdir=fake_swarmdir)
	swarmfiles_exist=[os.path.exists(f'{fake_swarmdir}newDs_{date_today}.swarm'),os.path.exists(f'{fake_swarmdir}sam_cov_highgamma_cue_{date_today}.swarm'),os.path.exists(f'{fake_swarmdir}sam_wts_highgamma_cue_{date_today}.swarm'),os.path.exists(f'{fake_swarmdir}sam_3d_highgamma_cue_{date_today}.swarm')]
	assert swarmfiles_exist==[1,1,1,1],'Swarm files not created. UGH!'


if __name__=='__main__':
	test_make_param()
	test_make_swarms()        


#remove the evidence
shutil.rmtree(f'{cwd}/MID_test_data', ignore_errors=False, onerror=None)

#celebrate
print('All tests passed! Woo!!')
