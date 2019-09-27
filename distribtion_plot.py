
import matplotlib.pyplot as plt
import numpy as np, pandas as pd; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)

tips = sns.load_dataset("tips")
# g = sns.jointplot(x="total_bill", y="tip", data=tips,  kind="hex")
# sns.pairplot(tips, hue='sex', palette='coolwarm')
# sns.rugplot(tips['total_bill'])
# sns.distplot(tips['total_bill'], kde=False)
