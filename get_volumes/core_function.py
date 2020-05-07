import pandas as pd
def get_volumes(input):
    data = pd.read_csv(input)  #if UnicodeDecodeError open csv file in Sublime Text and Save with UTF-8 encoding
    data.head()
    clean_data = data.copy()[['Sample Time','Type', 'Conc.']]
    clean_data.head()
    clean_data["Volume"] = 700/clean_data["Conc."]
    clean_data.head()
    return clean_data
