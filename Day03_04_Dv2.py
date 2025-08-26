import pandas as pd
import matplotlib.pyplot as plt

data = {
    'time':[10,11,12,13,14,15,16,17,18,19,20],
    'ChennaiTemperature':[30,31,34,35,34,33,32,31,30,29,28]
}
df = pd.DataFrame(data)
df.plot(kind='scatter', x='time', y='ChennaiTemperature', marker='o', label='Chennai', color='darkblue')
plt.show()


df1 = pd.read_csv('Day02_SampleData.csv')
# scatter 
plt.scatter(df1['Overs'], df1['TeamA'], marker='x', label='TeamA', color='darkblue')
plt.scatter(df1['Overs'], df1['TeamB'], marker='o', label='TeamB', color='darkred')
plt.legend()
plt.show()


df2 = pd.DataFrame({
    'Products':['Apple','Samsung','Sony','Moto'],
    'Revenue':[190,200,150,80]
})
df2.plot(kind='bar', x='Products', y='Revenue', color=['red','blue','green','orange'],title='Product Revenue')

plt.show()

df2.plot(kind='barh', x='Products', y='Revenue', color=['red','blue','green','orange'],title='Product Revenue')

plt.show()



# pie chart
df2.set_index('Products', inplace=True)
df2.plot(kind='pie', y='Revenue', autopct='%1.1f%%', legend=False, title='Product Revenue')
plt.show()