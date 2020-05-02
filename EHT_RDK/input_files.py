
import os
import glob
import pandas as pd

def create_input_list(directory_name):
    file_list = []

    # Check to make sure that only '.txt' files are being appended to list
    for filename in os.listdir(directory_name):
        if filename.endswith('.txt'):
            file_list.append(filename)
        else:
            print('Found non .txt file in directory: ' + filename)
            
    return(file_list)
