# Regression and Faceting in Seaborn
# To see trends in the data, we can use regression plots and faceting.
# To compare across subgroups (faceting -> small multiples), we can use the `col` parameter.
# To diagnose models visually, we can use residual plots.

# combine regression line + automatic faceting + shared legend

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")
# linear regression
sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="sex", palette="Set1", height=4, aspect=1.2, legend=True)
plt.show()


# polinomial regression


sns.lmplot(data=tips, x="total_bill", y="tip", 
           order=2, # degree of the polynomial
           ci = None,
           height=8,
           legend=True)
plt.tight_layout()
plt.savefig("tips.png", dpi=300, bbox_inches="tight")
plt.show()
