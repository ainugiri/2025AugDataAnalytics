import pandas as pd

data = {
    'DasID':['A825662', 'A825663', 'A825664', 'A825665', 'A825666', 'A825667', 'A825668', 'A825662','A825668'],
    'Name': ['Giri', 'Prasad', 'John', 'Rose','Mohammed','Afzal','Eliza',None,'Eliza'],
    'Age': [25, 30, 35,None, 40, 45, 50, 55,50],
    'City': ['Hyderabad',None, 'Bangalore', 'Chennai', 'Mumbai', 'Delhi', 'Pune', 'Ahmedabad','Pune']
}
df = pd.DataFrame(data)
print("Emp Table / DataFrame\n",df)

# to detect missing value, isnull()

print("We are having Null", df.isnull())
print("We are having Null in City\n", df['City'].isnull())
print("No of nulls in my data\t:", df.isnull().sum().sum())
print("No of nulls in the City column\t:", df['City'].isnull().sum())


df1 = df.dropna()   # drop the rows with null values
print("After dropping the null values\n", df1)


df2 = df.fillna(0)
print("After filling the null values with 0\n", df2)

df3 = df[['DasID','Name','Age','City']].fillna({'Name':'No Name', 'Age':df['Age'].mean(),'City':'NA'})
print("After filling the null values with appropriate values\n", df3)

# To check duplicates in df3
print("Do we have duplicates",df3.duplicated()) #Check for duplicates

df3 = df3.drop_duplicates() # drop the duplicates
print(df3)


print(df3['DasID'].duplicated())    # To check on DASID Column

df3 = df3.drop_duplicates(subset=['DasID'],keep='first')  # drop duplicates based on DasID column
print(df3)

df3['Age'] = df3['Age'].astype(int) # converting the datatype of Age column to int
print(df3)

df3[['Name','City']] = df3[['Name','City']].apply(lambda x: x.str.upper())
print(df3)


df3['City'].replace({'NA':'MANGLORE'}, inplace=True)
print(df3)