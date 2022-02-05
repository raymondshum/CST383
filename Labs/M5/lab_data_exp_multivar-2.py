# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

url = "https://raw.githubusercontent.com/grbruns/cst383/master/College.csv"
df = pd.read_csv(url)
df.info()

# 3

breaks = df["F.Undergrad"].quantile([0, 0.33, 0.66, 1])
df["Size"] = pd.cut(
    df["F.Undergrad"],
    include_lowest=True,
    bins=breaks,
    labels=["small", "medium", "large"],
)

df["Size"].value_counts().plot(kind="bar")

# 4
g = sns.FacetGrid(df, col="Size", height=4, aspect=0.8)
g.map(plt.scatter, "PhD", "Outstate", s=20)

# 5
sns.scatterplot(x="PhD", y="Outstate", data=df, hue="Size")

# 6
sns.scatterplot(x="PhD", y="Outstate", data=df, hue="Size", style="Size")

# 7
sns.violinplot(x="Size", y="Outstate", data=df)

# 8
sns.violinplot(x="Size", y="Outstate", data=df, inner='stick')

# 9
g = sns.FacetGrid(df, col='Size', height=4, aspect=0.8)
g.map(plt.hist, 'PhD')
