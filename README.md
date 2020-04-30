# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)
Bar Lehmann - Project



Python Project Outline:

Program goal: create a basic program that will help to parse, clean, read, and analyze Electro-encephalogram (EEG) data, with possible add on of Galvanic Skin Response / Skin Conductivity Response (GSR) Data to explore connections with self reports of mood and focus.

The problem that this program attempts to solve is to facilitate the ease of biometric data gathering (EEG and GSR) into a neat table of summary information that can be compared. It is a package/tool aimed to assist more technically-minded biometric data gatherers, students, citizen scientists, or those interested to explore neurofeedback in a non-clinical manner. This project would be used for facilitating swift and easy conversaion between recordings of biometric data into a spreadsheet tabulating biometrics of interest such as alpha amplitude at a particular 10-20 site, and help compare this with self reported mood and focus ratings. This tool/program would also offer easeir access to the MNE API plots to view data, such as amplitude-frequency analyses. Obviously, this program would not be used for any medical purposes during the timeline of this class as this would require extensive testing and verification. This program could also be used to offer quality control type verification for automatically generated reports that consumer and/or neurofeedback software do automatically. Such a program would be open source and could even serve as an initial platform to build more improved and specialized tools for easily and cheaply tracking and analyzing EEG and GSR data. 

This project would use the MNE: EEG Analysis and Visualization software that works through Python. It would have two main components (1) Preprocessing, and (2) Analysis/Visualization that each have a number of components to them. The program would be specialized to interpreting ‘.edf’ file formats.


1)	Preprocessing
Parsing/Cleaning the file
-	Converting from raw data and "Annotations" formats to "events"
-	"Epoching" or parsing the data into a time-segments that are readable, appropriate for a given analysis to be done
-	Artifact (noise in the signal) identification and suppressing
o	 Marking bad channels
o	Independent component analysis technique to identify and also to eliminate the "artifacts" (noise in the signal)

2)	Visualization and Analysis 
-	Much of the analysis will be concerned with analyzing amplitude statistics for electrodes separately or in conjunction, comparing this for different wavebands and sensor locations. 
-	Changing montages for EEG recordings ("montages" refer to different means of interpreting the recorded data from sensors via different calculations)
-	Filtering the data through high, low, and notch filters to allow for different views.
-	As I become more familiar with accessing the possibilities of the MNE-Python software I hope to expand this section on that basis. 



