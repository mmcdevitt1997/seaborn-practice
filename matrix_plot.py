
import matplotlib.pyplot as plt
import numpy as np, pandas as pd; np.random.seed(0)
import seaborn as sns; sns.set(style="white", color_codes=True)

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")

print('tips',tips.head(),)
print('flights',flights.head())

