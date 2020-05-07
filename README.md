# project_spring_2020

[![CircleCI](https://circleci.com/gh/biof309/project_spring_2020/tree/master.svg?style=shield)](https://circleci.com/gh/biof309/project_spring_2020/tree/master)


# Tetrad Analysis

This package will allow for the user to upload an excel file consisting of tetrad information containing sample numbers and 1s and 0s, and allow for the user to sort their data by drug markers.  Afterwards, the user can combine all their sorted data and create a new excel document that contains sheets for each drug marker.  In these sheets, the positive marked spores that were filtered will be listed there.

# Imported file being used for practice

from tetrad_analysis import python_test_list.xlsx

# Steps of the program

1. import an excel document of choice and convert it into a dataframe that can be used by the program
2. sort this input by positive values for drug markers (in this case it would be the columns) and create separate dataframes for each drug marker
3. combine these dataframes into a single library that will be labeled all_positive
4. convert this library into a new excel document that will separate each drug marker into its own sheet


# Purpose for this program

This program will facilitate the process of sorting through data.  There can be over hundreds of samples of tetrad data for analysis.  It would take a long time to sort this amount.  Therefore, by having a program that does it, it would save time.

# Contact
Catherine Harvey (harveycas@nih.gov)
