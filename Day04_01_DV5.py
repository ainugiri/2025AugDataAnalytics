import seaborn as sns
import matplotlib.pyplot as plt

# global theme 
sns.set_theme(style="whitegrid",context="notebook") # global theme

# context preset: "paper" << "notebook" << "talk" << "poster"
sns.set_context("talk") # makes the fonts larger for slides

with sns.axes_style("ticks"),sns.plotting_context("paper",font_scale=1.2):
    # plot
    ax = sns.scatterplot(data=sns.load_dataset("tips"), x="total_bill", y="tip",hue="time")
    sns.despine() # removes the top and right spines
    plt.title("Scatter Plot of Total Bill vs Tip (paper context)")
    plt.show()



sns.set_palette("deep")
sns.set(rc={"axes.grid": True,
            "axes.facecolor": "#764343",
            "axes.titleweight": "bold"})

ax = sns.scatterplot(data=sns.load_dataset("tips"), x="total_bill", y="tip",hue="time",
                     style="time",size="size",sizes=(20,200),alpha=0.7)

ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title("Scatter Plot of Total Bill vs Tip (paper context)")
plt.tight_layout()
plt.show()
