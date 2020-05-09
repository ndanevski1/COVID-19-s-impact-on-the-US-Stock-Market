# COVID-19's impact on the US Stock Market
# Done in collaboration of Muhammad Usama Ijaz and Nikola Danevski

import pandas as pd
import numpy as np
import copy


data = pd.read_csv("Dataset - with converter.csv")

divide_percent = []
step = 25
for i in range (-95, 105, step):
    divide_percent.append(i)
data['Percentage Increase/Decrease'] = pd.cut(data['Percentage Increase/Decrease'], divide_percent)

# print(data['Average Increase/Decrease (in %)'])

data.to_csv('Dataset - with converter and categorical.csv', index=False)