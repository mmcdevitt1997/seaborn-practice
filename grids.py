import matplotlib.pyplot as plt
import numpy as np, pandas as pd; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)

iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')
# print(iris.head())

unique_species=iris['species'].unique()

# print(unique_species)

# pair_grid= sns.PairGrid(iris)

# pair_grid.map_diag(sns.distplot)
# pair_grid.map_upper(plt.scatter)
# pair_grid.map_lower(sns.kdeplot)
# plt.show()

tips_grid = sns.FacetGrid(data=tips, col='time', row='smoker')
tips_grid.map(sns.distplot, 'total_bill')
# plt.show()