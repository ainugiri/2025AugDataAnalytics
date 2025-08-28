import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

penguins = sns.load_dataset("penguins")
df = penguins.dropna()
print(df.head())



sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")
# plt.show()


sns.jointplot(
    data=df,
    x="bill_length_mm", y="bill_depth_mm", 
    kind="reg",
    height=7, ratio=4, marginal_ticks=True
)
plt.show()

# density view (KDE) with hue
sns.jointplot(
    data=df,
    x="bill_length_mm", y="bill_depth_mm", hue="species",
    kind="kde",
    height=7, ratio=4, marginal_ticks=True
)

plt.show()


tips = sns.load_dataset("tips")
print(tips.head())
sns.stripplot(
    data=tips,
    x="day", 
    y="total_bill", 
    hue="smoker", 
    dodge=True, 
    jitter=True,
    alpha=0.7,
)
plt.title("Strip Plot of Total Bill by Day and Smoker Status")
plt.show()


sns.swarmplot(
    data=tips,
    x="day", 
    y="total_bill", 
    hue="sex", 
    dodge=True,
    alpha=0.7,
)
plt.title("Swarm Plot of Total Bill by Day and Sex")
plt.show()


sns.violinplot(data=tips,x="day",y="total_bill",inner=None, color=".8")
sns.swarmplot(
    data=tips,
    x="day", 
    y="total_bill", 
    hue="sex", 
    dodge=True,
    alpha=0.7,
)
plt.title("Violin and Swarm Plot of Total Bill by Day and Sex")
plt.show()
