# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)
  
Christina Wusinich  
Intro to Python  
February 27, 2020

# Outline for Final Project

## Objective of package:  
I would like to design a series of scripts that will allow me to process behavioral and MEG data from a reward processing task, called the Monetary Incentive Delay (MID) task. I would use this package for the next year as we collect additional data on this task, and if the lab keeps using the task, hopefully the scripts I make can be helpful even after I leave the NIH.

## Background:  
The MID task shows various shapes which allow participants to win money, avoid losing money, or do nothing (a neutral condition) if they press a button within a particular time window following the shape. After pressing the button, they receive feedback indicating whether they won money, avoided losing money, or had no reward in either direction. Our sample is still being collected but includes healthy controls, participants diagnosed with mood disorders on medication, and participants diagnosed with mood disorders off medication.

The goal of my analysis is to report on deep source activity (i.e. striatum in this case) in the task’s MEG data using synthetic aperture magnetometry (SAM) for source localization. If we find activity as expected in the high gamma band during the feedback phase of the task, it will become a useful way to study reward processing in mood disorders and the impact of novel treatments using MEG.

Additionally, we plan to explore connectivity between regions related to reward processing using modelling (of some sort?), though the details of that are still being worked out.

In terms of our analysis of behavior data, we need to gather mean reaction times and accuracy of button presses for analysis with an ANOVA (more details to come based on what factors will be involved).

## Files that need to be processed:  
-	Behavior data: a .txt output from the MID task that indicates button presses, timing of stimuli, etc.
-	MEG data: a CTF (this is the MEG system we have at the NIH) file of MEG data from the task
-	MRI data: structural MRIs for use with source localization (I already have a script for converting the files from the DICOM site to .nii files from my lab)

# Processing steps:  
I am not sure that is the best way to do this, but this is what needs to happen to get the data from its raw state to stats that I can report. The bolded script names are the ones I would like to create for my package based off a naming convention I’ve seen in our fMRI processing pipeline, though they are still subject to change:

## Manual steps before scripts:
1.	Transfer MEG, behavior, and MRI data to data processing folder on biowulf (this is just done with a BASH command)
2.	Update demographics spreadsheet for use in analysis
3.	Set fiducial markers on MRI copy

##	MEG preprocessing step 1
1.	Script name will be **01_megpreprocess1**, and I would like it to do the following:
-	 Change file name using CTF command (to make file names look like “subject#_MID.ds” so they are more uniform)
-	Set markers for stimuli (cue markers) and output file (.txt file) of the times of the cue marks (this file will be used in the next step)
-	I already have some of the CTF commands for this, but I would like to figure out how to give this script (and all of the following ones) a list of subject names to loop through so I can do this all at once.
2.	Input: MEG data file
3.	Output: copied and edited MEG data file, cue markers text file

##	Behavior processing
1.	Script name will be **02_behprocess**, and it will do the following:
-	Makes marker files for more MEG processing; these markers will designate win/loss/neutral cues to be marked in the MEG file and are output as three separate .txt files to the subject’s MEG directory
-	Pulls columns from behavior data file and calculates mean RTs and accuracy by trial and subject and appends that to master behavior data sheet (I will probably work with this sheet in R unless I can do an ANOVA as another step)
-	I have already made two separate jupyter notebook files to do each of the above tasks, but I can figure how to do it without finding and replacing the subject ID; obviously a loop would be a lot easier, so I would like to figure that out and collapse both notebooks into one script
2.	Input: cue markers text file, behavior text file
3.	Output: win/loss/neutral text files (3), master file (csv? Not sure of best format for this) that includes mean reaction times and accuracy by participant and trial

##	MEG preprocessing step 2
1.	Script name will be **03_megpreprocess2**, and I would like it to do the following:
-	Adds win/loss/neutral markers to cues
-	Adds win/loss/neutral markers to responses
-	Filter data based on existing filtering parameters file
2.	Problems to figure out:
-	When I do this one command at a time (which is how I’ve been doing this so far), it always misses two markers that I have to then add manually, so I need to figure out how to get it to add those two markers on its own.
3.	Input: MEG file, win/loss/neutral marker files from the step above
4.	Output: edited MEG file

##	MEG processing with SAM
1.	Script name will be **04_sam** and will do the following:
-	orthohull (from subject’s MRI folder)
-	Source localization in high gamma using three SAM commands and parameter file→ output is .nii file
-	Copy .nii file from subject’s MEG directory to their MRI directory
-	Talairach SAM results for analysis in afni
-	Copy talairached .nii file into a group folder for group analysis
2.	Problems:
-	This step uses a parameter file that I would like to be able to create and distribute among subject directories whenever we want to change parameters (e.g. the time window we’re looking at in the task)
-	Each of the three SAM commands takes a bit of time, but I heard that using swarm in biowulf may be a good way to do this. I am not sure how it would work with a loop just yet, but it’s an aspiration to make this somewhat efficient if possible.
3.	Input: MRI with fiducial markers set, MEG file, parameter file (highgamma.param), [maybe demographics spreadsheet]
4.	Output: .nii file, adds file path of the .nii file to a text file for analysis
-	This text file is for 3dLME and also needs to have participant demographic info; I was manually adding this from another spreadsheet, but maybe I can have this script copy those demographic columns in and match the file path based on subject ID?

##	Analysis
1.	Right now, I will plan to make this a step for 3dLME in afni, but we may choose to do a different analysis in the coming weeks.
2.	Script name will be **05_3dLME** and will do the following:
-	Runs 3dLME on all the .nii files
-	I already have a tcsh script that does this, so I’m not sure if this is really necessary to make it in python?
3.	Input: do_3dLME_MID_highgamma2.txt (this is the text file I mentioned above that contains file paths of the .nii files and demographic info of participants, such as group and age)
4.	Output: text file named by date and type of analysis with results from 3dLME

##	Permissions
1.	I want a script that will set all of the permissions correctly for my group for all of the output files above because umask in my bash profile does not seem to work for this.
2.	The commands in this script may just be put at the end of each of the above ones depending on how this works out, or should it just be a bash script?

# Additional Questions:  
-	Can I have a script do “module load afni” (and ctf, and R) so that I don’t have to?
-	If the commands are from CTF, can they be in a python script? I had just been running them in the terminal, so would I have to add something special to the beginning of each one to include it in a python script?
-	Can I make a giant script that will run all of these steps (01-05 and setting permissions) on a list of subjects?
-	How can I set my default python version in biowulf without manually having to load 3.7 every time? Can I do that at the beginning of the first script or in my profile?
