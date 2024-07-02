import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load a sample dataset
tips = sns.load_dataset("tips")

# Function to convert problematic columns to numeric
def to_numeric(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            except:
                pass
    return df

# Apply the function to the dataset
tips = to_numeric(tips)

# Now proceed with your plots
##1.Relational plots:
# Scatterplot
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()

# Lineplot
sns.lineplot(data=tips, x="total_bill", y="tip")
plt.show()

# Relplot (Figure-level interface combining scatterplot and lineplot)
sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker", col="time", kind="scatter")
plt.show()

##2.Categorical plots:
# Boxplot
sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()

# Violinplot
sns.violinplot(data=tips, x="day", y="total_bill")
plt.show()

# Barplot
sns.barplot(data=tips, x="day", y="total_bill")
plt.show()

# Catplot (Figure-level interface for categorical plots)
sns.catplot(data=tips, x="day", y="total_bill", kind="box")
plt.show()

##3.Distribution plots:
# Histplot
sns.histplot(data=tips, x="total_bill")
plt.show()

# KDE plot
sns.kdeplot(data=tips, x="total_bill")
plt.show()

# Displot (Figure-level interface for distribution plots)
sns.displot(data=tips, x="total_bill", kde=True)
plt.show()

##4.Regression plots:
# Regplot
sns.regplot(data=tips, x="total_bill", y="tip")
plt.show()

# Lmplot (Figure-level interface for regression plots)
sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker")
plt.show()

##5.Matrix plots:
# Heatmap
correlation = tips.corr()
sns.heatmap(correlation, annot=True)
plt.show(block=False)

# Clustermap
sns.clustermap(tips.corr(), annot=True)
plt.show(block=False)

##6.Multi-plot grids:
# FacetGrid
g = sns.FacetGrid(tips, col="time", row="smoker")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()

# PairGrid
g = sns.PairGrid(tips)
g.map(sns.scatterplot)
plt.show(block=False)

# JointGrid
g = sns.JointGrid(data=tips, x="total_bill", y="tip")
g.plot(sns.scatterplot, sns.histplot)
plt.show(block=False)

##7.Figure-level functions:
# Set style
sns.set_style("whitegrid")

# Set context
sns.set_context("paper")

# Set palette
sns.set_palette("pastel")

##8.Color palette functions:
# Create a custom color palette
colors = sns.color_palette("husl", 8)
sns.palplot(colors)
plt.show(block=False)

##9. Utility functions:
# Load dataset
iris = sns.load_dataset("iris")

# Get dataset names
print(sns.get_dataset_names())

# Pairplot
sns.pairplot(iris, hue="species")
plt.show(block=False)
