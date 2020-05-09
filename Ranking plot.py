# COVID-19's impact on the US Stock Market
# Done in collaboration of Muhammad Usama Ijaz and Nikola Danevski

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("ranking.csv")


data.plot()
plt.xticks([])
plt.show()