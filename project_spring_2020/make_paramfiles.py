#CW 4.19.2020
#written for python 3.7 but works in older versions
#makes highgamma.param files and puts them in each subject's meg folder; this can be run from anywhere
#make sure to set param variables you want!

import os

#set directory, subject list, and some other things
rootdir='/data/MoodGroup/07M0021_meg_analysis/MID_data/subjects/'
root, dirs, files = os.walk(rootdir).next()
subj_list=list(dirs)
alpha=['alpha','8 14']
beta=['beta','15 29']
gamma=['gamma','30 60']
highgamma=['highgamma','62 118']

#set variables here:
NumMarkers='1'
Marker1='cue'
marker1window='0 4'
freqname,freqband=gamma

OrientBand=freqband
NoiseBand=freqband
CovBand=freqband
ImageBand=freqband
DataSegment=marker1window
XBounds='-10 10'
YBounds='-9 9'
ZBounds='0 15'
ImageStep='.5'
ImageMetric='Power'
Model='Nolte'
CovType='SUM'
ImageFormat='TLRC 5'

#makes param files for each subject in their meg folder
paramfile_name=freqname+'_'+Marker1+'.param'
for sub in subj_list:
	new_paramfile=open(rootdir + sub + '/meg/' + paramfile_name,'w+')	
	new_paramfile.write('NumMarkers '+NumMarkers+'\n' +'Marker1 '+Marker1+' '+marker1window+' TRUE'+'\n'+ 'OrientBand '+OrientBand+'\n'+ 'NoiseBand '+NoiseBand+'\n'+ 'CovBand '+CovBand+'\n'+ 'ImageBand '+ImageBand+'\n'+ 'DataSegment '+DataSegment+'\n'+ 'XBounds '+XBounds+'\n'+ 'YBounds '+YBounds+'\n'+ 'ZBounds '+ZBounds+'\n'+ 'ImageStep '+ImageStep+'\n'+ 'ImageMetric '+ImageMetric+'\n'+ 'PrefixLength '+str(len(sub))+'\n'+ 'MRIDirectory '+rootdir+sub+'/mri\n'+ 'Model '+Model+'\n'+ 'CovType '+CovType+'\n'+ 'ImageFormat '+ImageFormat)
	new_paramfile.close()

print("Param files have been added!")
