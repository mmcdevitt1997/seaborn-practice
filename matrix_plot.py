
import matplotlib.pyplot as plt
import numpy as np, pandas as pd; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")

'tips',tips.head()
'flights',flights.head()

tc = tips.corr()
# sns.heatmap(tc)

flights_table=flights.pivot_table(index='month', columns='year', values='passengers')
print(flights_table)

# sns.heatmap(flights_table, cmap='magma')

sns.clustermap(flights_table)
# plt.show()
