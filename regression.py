import matplotlib.pyplot as plt
import numpy as np, pandas as pd; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)

tips = sns.load_dataset("tips")

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', markers=['o','v'])
# plt.show()
