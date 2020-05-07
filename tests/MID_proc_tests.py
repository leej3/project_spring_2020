import MID_proc as mid
import os
import shutil

#set up some example directories and files for use with tests
cwd=os.getcwd()
#os.makedirs(f'{cwd}/MID_test_data/subjects',exist_ok=True)
os.makedirs(f'{cwd}/MID_test_data/scripts/swarm',exist_ok=True)
fake_subdir=f'{cwd}/MID_test_data/subjects/'
#set sub fake sub ID numbers; these were picked to test that prefix length calculation in make_param() works with a variety of ID lengths
fake_subs=['7','13','101','102','99','990','9999']
for sub in fake_subs:
	os.makedirs(f'{fake_subdir}sub-{sub}/meg',exist_ok=True)
	os.makedirs(f'{fake_subdir}sub-{sub}/behavior',exist_ok=True)

#first test is for the param file maker function
def test_make_param():
	"""This tests if make_param() can make parameter files with a few non-default inputsarguments and put them in fake subjects' meg folders."""
	mid.make_param(rootdir=fake_subdir,Marker1='cue', marker1window='0 4')
	paramfiles_exist=[os.path.exists(f'{fake_subdir}sub-{sub}/meg/highgamma_cue.param') for sub in fake_subs]
	assert paramfiles_exist==[1]*len(fake_subs),'Param files were not created properly--oh no!'

#second test is coming soon


if __name__=='__main__':
	test_make_param()


#remove the example files once complete
shutil.rmtree(f'{cwd}/MID_test_data', ignore_errors=False, onerror=None)

#celebrate
print('All tests passed! Woo!!')
