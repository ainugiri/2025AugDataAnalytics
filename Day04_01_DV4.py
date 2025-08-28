import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("tips")
print(df.head())

# scatter plot
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()

# line plot
plt.figure(figsize=(10,5))
sns.lineplot(x="total_bill", y="tip", data=df)
plt.title("Line Plot of Total Bill vs Tip")
plt.grid(True)
plt.show()

data = {
    'x': ['Giri','Prasad', 'Mohammed', 'Sunil', 'Priya'],
    'y': [76,82,59,100,95]
}


# visualize bar plot
plt.figure(figsize=(10, 5))
sns.barplot(x='x', y='y', data=data)
plt.title("Bar Plot of Names vs Scores")
plt.grid(True)
plt.show()


# count plot - frequency of each category
# tips dataset: categories the tips based on Monday,  Tuesday,  Wednesday,  Thursday,  Friday,  Saturday,  Sunday
plt.figure(figsize=(10, 5))
sns.countplot(x='smoker', data=df)
plt.title("Count Plot of smoker")
plt.grid(True)
plt.show()