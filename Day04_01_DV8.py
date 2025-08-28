import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins") 
(
    so.Plot(penguins,x="flipper_length_mm", y="body_mass_g",color="species")
    .add(so.Dots(alpha=0.7))         # scatter dot
    .add(so.Line(), so.PolyFit((1))) # regressionline
    .facet(col="species")                    # facet by species
    .label(title="Penguin Flipper Length vs Body Mass by Species")
    .show()
)