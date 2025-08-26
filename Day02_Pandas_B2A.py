import pandas as pd

a = ['Name','Giri','Prasad','John','Rose']

myseries = pd.Series(a, index = ['CN','Rank1','Rank2','Rank3','Rank4'])     # to create column in a Table, One Dimensional - any datatype
print(myseries)
print(myseries['Rank4'])



emp = {'A825662':'Giri', 'A825663':'Prasad', 'A825664':'John', 'A825665':'Rose'}
empseries = pd.Series(emp)   # dictionary to series
print(empseries)
print(empseries['A825664'])

testingemp = pd.Series(emp, index=['A825662','A825665'])
print("\nTesting Emp\n",testingemp)


# one-dimensional - series
# multidimensional - DataFrame


data = {
    'Name': ['Giri', 'Prasad', 'John', 'Rose','Mohammed','Afzal','Eliza'],
    'Age': [25, 30, 35, 40, 45, 50, 55],
    'City': ['Hyderabad', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi', 'Pune', 'Ahmedabad']
}
df = pd.DataFrame(data)
print("Emp Table / DataFrame\n",df)


print("\nMohammed Value\n",df.loc[4])

print("\nAfzal:\n",df.loc[df['Name'] == 'Afzal'])

print("\nBelow 40 Years old:\n",df.loc[df['Age'] < 40])

print("\nName Contains z:\n", df.loc[df['Name'].str.contains('z')])

print("\nName Contains z:\n", df[df['Name'].str.contains('z')])
