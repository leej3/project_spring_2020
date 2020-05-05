import pandas as pd
import numpy as np
df = pd.read_excel(r'/Users/harveycas/Documents/FAES/Python class/python_test_list.xlsx')
print(df)


df_index = df.set_index('Plate')
print(df_index)

sort_by_NAT = df_index.sort_values(['NAT'], ascending=False)
NAT_positive = df_index[df_index['NAT'] > 0]
print(NAT_positive)
dfNAT = pd.DataFrame(NAT_positive)
dfNAT.to_excel("NAT_positive_python_fp.xlsx")


sort_by_HYG = df_index.sort_values(['HYG'], ascending=False)
HYG_positive = df_index[df_index['HYG'] > 0]
print(HYG_positive)
dfNAT = pd.DataFrame(HYG_positive)
dfNAT.to_excel("HYG_positive_python_fp.xlsx")


sort_by_URA = df_index.sort_values(['URA'], ascending=False)
URA_positive = df_index[df_index['HYG'] > 0]
print(URA_positive)
dfNAT = pd.DataFrame(URA_positive)
dfNAT.to_excel("URA_positive_python_fp.xlsx")


all_positive = {'NAT_plus': NAT_positive, 'HYG_plus': HYG_positive, 'URA_plus': URA_positive}
writer = pd.ExcelWriter('Antibiotic_markers.xlsx', engine='xlsxwriter')

for sheet_name in all_positive.keys():
    all_positive[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
    
writer.save()