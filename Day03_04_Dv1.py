import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('Day02_SampleData.csv')
print(df)
plt.plot(df['Overs'],df['TeamA'],marker='x', label='TeamA',color='darkblue')
plt.plot(df['Overs'],df['TeamB'],marker='o', label='TeamB',color='darkred')
plt.legend()
plt.show()



