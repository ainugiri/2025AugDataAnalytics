import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('tips')
print(df.head())


# Box Plot : Total Bill by Day
plt.figure(figsize=(10, 5))
sns.boxplot(x='day', y='total_bill', data=df)
plt.title("Box Plot of Total Bill by Day")
plt.grid(True)
plt.show()


# Violin Plot : Total Bill by Day
plt.figure(figsize=(10, 5))
sns.violinplot(x='day', y='total_bill', data=df)
plt.title("Violin Plot of Total Bill by Day")
plt.grid(True)
plt.show()


# pair plot - relationships between variables

sns.pairplot(df, hue='day', palette='coolwarm')
plt.show()  

numeric_df = df.select_dtypes(include=["number"])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()



sns.heatmap(corr,
            fmt=".2f",
            cmap='YlGnBu',
            linewidths=0.8,
            cbar=True)
plt.show()


pivot1 = df.pivot_table(values="tip", index="day", columns="time", aggfunc="mean")
pivot2 = df.pivot_table(values="total_bill", index="day", columns="time", aggfunc="mean")

sns.heatmap(pivot1, annot=True, cmap='coolwarm')
plt.show()

sns.clustermap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()