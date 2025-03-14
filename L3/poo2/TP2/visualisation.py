import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys

df = pd.read_csv("donnees.csv", sep=" ", header=None)
df.columns = ["Annual income (k$)", "Spending Score (1-100)"]
sns.scatterplot(x=df["Annual income (k$)"], 
                y=df["Spending Score (1-100)"])
plt.title("Scatterplot of spending (y) vs income (x)")

# After clustering
plt.figure()
df = pd.read_csv("output.csv")
sns.scatterplot(x=df.x, y=df.y, 
                hue=df.c, 
                palette=sns.color_palette("hls", n_colors=int(sys.argv[1])))
plt.xlabel("Annual income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Clustered: spending (y) vs income (x)")

plt.show()

