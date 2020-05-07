import pandas as pd
import numpy as np

file1 = pd.read_csv('/Users/avapapetti/Desktop/CNV_Files/SL88823_20180802.cnv.csv', sep = "\t")
file2 = pd.read_csv('/Users/avapapetti/Desktop/CNV_Files/SL88824_20180802.cnv.csv', sep = "\t")

file1['Sample#'] = 1
file2['Sample#'] = 2

min_cnv_length = 1000
p_value_threshold = .90

"""Remove CNVs from both samples that fail to meet intial criteria"""

file1 = file1.drop(file1[file1.Chrom == 'chrM'].index)
file1 = file1[(np.abs(file1.Start - file1.Stop) >= min_cnv_length) & (file1.P_Value >= p_value_threshold)]

file2 = file2.drop(file2[file2.Chrom == 'chrM'].index)
file2 = file2[(np.abs(file2.Start - file2.Stop) >= min_cnv_length) & (file2.P_Value >= p_value_threshold)]

def common_cnvs_finder():
    
    """Find CNVs common to both samples that meet qualifying criteria and create output file of results"""
    
    common_cnvs = pd.DataFrame(columns = file1.columns)
    file2_byChrom = file2.groupby('Chrom')

    for i in range(len(file1)):
        file2_cnvs = file2_byChrom.get_group(file1.iloc[i].Chrom)
        file2_cnvs = file2_cnvs.loc[file2_cnvs.Type.isin(file1.iloc[[i]].Type)]
        file2_cnvs = file2_cnvs.loc[(np.abs(file2_cnvs.Start.subtract(file1.iloc[i].Start)) <= 25) &
        (np.abs(file2_cnvs.Stop.subtract(file1.iloc[i].Stop)) <= 25)]

        if(len(file2_cnvs) > 0):
            common_cnvs = pd.concat([common_cnvs, file1.iloc[[i]], file2_cnvs]).reset_index(drop = True)
    
    print(common_cnvs.info())
    common_cnvs_output = common_cnvs.to_csv()

common_cnvs_finder()