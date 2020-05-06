# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)

## MID MEG Processing!
A very amateur python package by Christina Wusinich

Last updated: 04/06/2020

## Objective of package:  
A series of scripts for processing behavioral and MEG data from a reward processing task, called the Monetary Incentive Delay (MID) task.

## Background:  
The MID task shows various shapes which allow participants to win money, avoid losing money, or do nothing (a neutral condition) if they press a button within a particular time window following the shape. After pressing the button, they receive feedback indicating whether they won money, avoided losing money, or had no reward in either direction.

The goal of my initial analysis was to report on deep source activity (i.e. striatum in this case) in the task’s MEG data using synthetic aperture magnetometry (SAM) for source localization. Showing that this is possible in MEG (usually not known for deep source analyses) will pave the way for studying reward processing in mood disorders and the impact of novel treatments using MEG. Moving forward, we are going to (and already have done a bit) conduct analyses in different time windows in the task and in different frequency bands, so the scripts below were designed to make it easier to repeat processing steps with different parameters.

In terms of our analysis of behavior data, we need to gather mean reaction times and accuracy of button presses for analysis with an ANOVA (more details to come based on what factors will be involved).

## Files that need to be processed:  
-	Behavior data: a .txt output from the MID task that indicates button presses, timing of stimuli, etc.
-	MEG data: a CTF (NIH's MEG system) file of MEG data from the MID task
-	MRI data: structural MRIs for use with source localization (already converted to .nii before this)

## Setup of directories for use with this package:
-	Behavior data example: MID_data/subjects/sub-201/beh
-	MEG data example: MID_data/subjects/sub-201/meg
-	MRI data example: MID_data/subjects/sub-201/mri
-	swarm files: MID_data/scripts/swarm


# Processing steps (that this package helps with):  

##	Behavior processing (still under construction; need to make jupyter notebook copied file into py script)
1.	**MID_behprocess.py** (doesn't exist yet)
-	Makes marker files for more MEG processing; these markers will designate win/loss/neutral cues to be marked in the MEG file and are output as three separate .txt files to the subject’s MEG directory
-	Pulls columns from behavior data file and calculates mean RTs and accuracy by trial and subject and appends that to master behavior data sheet
2.	Input: cue markers text file (this is from a previous MEG processing step not included here), behavior text file
3.	Output: win/loss/neutral text files (3), master csv that includes mean reaction times and accuracy by participant and trial

##	Create dataset copies with fresh, new, hip parameters
1.	**make_newDs_swarm.py**:
-	Makes a swarm file that will create new datasets from existing MEG datasets (helpful if you want to look in a new time window or use different markers and make a fresh batch of datasets to work with)
-	As of now, you need to edit the variables at the beginning of the script to make paramter changes
2.	Input: and original MEG file (something.ds) and processinglist.txt (a file with a list of participant ID numbers you want to include--one day this will be fancier, but this is what we're working with this week)
3.	Output: a .swarm file in your swarm directory; also after running this, you will see the swarm command you need to run as output in your terminal window

##	Pre-SAM parameter file creation
1.	**make_paramfiles.py**:
-	Makes parameter files for use with SAM commands (see step below) and drops each unique and glorious param file into each subject's meg directory
-	Again, there are variables at the beginning of script that make changing the parameters (as needed for your analysis) relatively easy, though in the future, this will hopefully be upgraded to something more interactive in the command line so no one has to edit the script.
2.	Input: nothing! This script really knows what its doing! (well technically it needs to find subject folders in your subjects directory, but this is still pretty exciting)
3.	Output: a param file in each subject's meg directory

##	MEG processing with SAM
1.	**make_sam_swarm.py**:
-	Makes three swarm files for all subjects in processinglist.txt; each swarm file has a a command for source localization in high gamma using SAM (from samsrcv3)
-	There are a few variables clearly labelled at the top of the script that can be changed to reflect the frequency band, marker, and dataset you want to use.
2.	Input: MRI with fiducial markers set, MEG file, parameter file (highgamma.param)
3.	Output: three .swarm files in your swarm directory; also after running this, you will see the swarm commands as output in your terminal window, and you just need to copy them one at a time into the command line!
4.	Final output after running all three swarms: *Mean.nii file for use in analysis


# Notes about this young and naive package
-	Obviously this package does not cover all of the processing steps involved, but it has streamlined the process substantially and will hopefully one day grow up to be a mature pipeline that takes in MEG data and outputs magic.
-	The SAM swarm script successfully creates the swarm files, and the swarm files run successfully (according to the output), but the files that are created are bad (as in not the same as if each SAM command was run individually and not in a swarm). Still working on trouble-shooting this before the project deadline!
