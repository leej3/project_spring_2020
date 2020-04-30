import pandas as pd
cd dferhadianproject_spring_2020/project_spring_2020/
data = pd.read_csv("Data.csv")  #if UnicodeDecodeError open csv file in Sublime Text and Save with UTF-8 encoding
data.head()
clean_data = data[['Sample Time','Type', 'Conc.']]
clean_data.head()
