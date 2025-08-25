# read 
# import the pandas

import pandas as pd
df = pd.read_csv('SalesData.csv')
# print(df)       
# print(df.tail())
# print(df.head())
# print(df.head(3))
# print(df.tail(2))

# print(df.shape)  # NoMo rows, columns
# print(df.info())   # data types, null values


# print(df.columns)

print(df.dtypes)

print(df['Product'])
print(df['Product'].value_counts())