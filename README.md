# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)
Bar Lehmann - Project



Python Project Outline:

Program goal: create a program to help parse, clean, read, and analyze (Electro-encephalogram EEG) data.

The problem that this program attempts to solve is to aid in EEG data gathering and analysis to cost efficiently analyze EEG data. It is a package/tool aimed to assist more technically-minded biometric data gatherers, students, citizen scientists, or neurofeedback practitioners. This project would be used for conducting a set of analysis to help compare baseline with non-baseline recordings, other human EEG recordings, or even neurofeedback-sessions. The analyses of this tool/program (such as amplitude-frequency analyses) are highly relevant to helping track EEG biometrics or even biomarkers of interest. (Obviously, this program would not be used for any medical purposes during the timeline of this class as this would require extensive testing and verification, but all efforts will be taken to make it useful in this effort and also to test its validity in its analysis.) This program could also be used to offer quality control type verification for automatically generated reports that consumer and/or neurofeedback software do automatically. Such a program would be open source and could even serve as an initial platform to build more improved and specialized tools for easily and cheaply tracking and analyzing EEG data. 

This project would use the MNE: EEG Analysis and Visualization software that works through Python. It would have two main components (1) Preprocessing, and (2) Analysis/Visualization that each have a number of components to them. The program would be specialized to interpreting ‘.edf’ file formats.


1)	Preprocessing
Parsing/Cleaning the file
-	Converting from raw data and “Annotations” formats to “events”
-	“Epoching” or parsing the data into a time-segments that are readable, appropriate for a given analysis to be done
-	Artifact (noise in the signal) identification and suppressing
o	 Marking bad channels
o	Independent component analysis technique to identify and also to eliminate the “artifacts” (noise in the signal)

2)	Visualization and Analysis 
-	Much of the analysis will be concerned with analyzing amplitude statistics for electrodes separately or in conjunction, comparing this for different wavebands and sensor locations. 
-	Changing montages for EEG recordings (“montages” refer to different means of interpreting the recorded data from sensors via different calculations)
-	Filtering the data through high, low, and notch filters to allow for different views.
-	As I become more familiar with accessing the possibilities of the MNE-Python software I hope to expand this section on that basis. 



