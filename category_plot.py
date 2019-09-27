
import matplotlib.pyplot as plt
import numpy as np, pandas as pd; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)

tips = sns.load_dataset("tips")

# sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
# sns.boxplot(x='day', y='total_bill', data=tips)
# sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)
sns.scatterplot(x='day', y='total_bill', data=tips, x_jitter=True, y_jitter=True)

