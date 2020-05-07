import MID_proc
import os

#set up some example directories and files for use with tests
cwd=os.getcwd()
os.mkdirs(f'{cwd}MID_test_data/subjects')
os.mkdirs(f'{cwd}MID_test_data/scripts/swarm')
fake_subdir='{cwd}MID_test_data/subjects/'
fake_subs=['7','13','101','102','99','990','9999']
for sub in fake_subs:
	os.mkdirs(f'{fake_subdir}{sub}/meg')
	os.mkdirs(f'{fake_subdir}{sub}/behavior')

#first test is for the param file maker function
def test_make_param():
	"""This tests if make_param() can make parameter files with a few non-default inputs and put them in fake subjects' meg folders."""
	make_param(rootdir=fake_subdir,freq=alpha,Marker1='cue', marker1window='0 4')
	paramfiles_exist=[os.path.exists(f'{fake_subdir}{sub}') for sub in fake_subs]
	assert paramfiles_exist==[1]*len(fake_subs),'Param files were not created properly--oh no!'

if __name__=='__main__':
	test_make_param()
