# COVID-19's impact on the US Stock Market
# Done in collaboration of Muhammad Usama Ijaz and Nikola Danevski

import pandas as pd
import numpy as np
import copy

data = pd.read_csv("Dataset - Resulting.csv")

data['Full Time Employees'] = pd.qcut(data['Full Time Employees'], 6)
data['Enterprise Value'] = pd.qcut(data['Enterprise Value'], 6)
data['Profit Margins'] = pd.qcut(data['Profit Margins'], 6)
data['Market Cap'] = pd.qcut(data['Market Cap'], 6)
data['Ask Size'] = pd.qcut(data['Ask Size'], 6, duplicates='drop')

# Separating the class attribute into categorical variables.

divide_percent = []
step = 25
for i in range (-95, 105, step):
    divide_percent.append(i)
data['Percentage Increase/Decrease'] = pd.cut(data['Percentage Increase/Decrease'], divide_percent)

# Calculating entropy for some of the classes
# We can see that it is the same if we use binning by frequency.

probs = data['Market Cap'].value_counts(normalize=True)
print(probs)
entropy = -1 * np.sum(np.log2(probs) * probs)
gini_index = 1 - np.sum(np.square(probs))
print("market cup entropy is ", entropy)
print("market cup gini_index is ", gini_index)

probs = data['Profit Margins'].value_counts(normalize=True)
print(probs)
entropy = -1 * np.sum(np.log2(probs) * probs)
gini_index = 1 - np.sum(np.square(probs))
print("profit margins entropy is ", entropy)
print("profit margins gini_index is ", gini_index)

probs = data['Ask Size'].value_counts(normalize=True)
print(probs)
entropy = -1 * np.sum(np.log2(probs) * probs)
gini_index = 1 - np.sum(np.square(probs))
print("ask size entropy is ", entropy)
print("ask size gini_index is ", gini_index)


gini_index = 1 - np.sum(np.square(probs))
print(gini_index)

data.to_csv('Dataset - with categorical variables.csv', index=False)
