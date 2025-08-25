import pandas as pd
# pandas - data analysis library, dataframes

filedata = pd.read_csv('Sample.csv')
# print(filedata)
print(filedata.head())
print(filedata.head(2))
print(filedata.info())
print(filedata.describe())
print(filedata['Department'].unique())

marketing = filedata[filedata['Department'] == 'Marketing']
print(marketing)

lowsal = filedata[filedata['Sal'] > 60000]
print(lowsal)