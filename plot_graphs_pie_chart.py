# COVID-19's impact on the US Stock Market
# Done in collaboration of Muhammad Usama Ijaz and Nikola Danevski

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show

data = pd.read_csv("Dataset - with converter and categorical.csv")
column_class = data['Percentage Increase/Decrease']

labels = 'Moderate Decrease', 'Minor Decrease', 'Major Decrease', 'Minor Increase', 'Extreme Decrease'

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

sizes = (data['Percentage Increase/Decrease'].value_counts())

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()