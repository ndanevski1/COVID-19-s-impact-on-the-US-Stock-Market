# COVID-19's impact on the US Stock Market
# Done in collaboration of Muhammad Usama Ijaz and Nikola Danevski

import seaborn as sn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


labels = ["Minor Decrease","Moderate Decrease","Major Decrease","Minor Increase", "Extreme Decrease"]
# array = [[111,36,0,2,0],
#           [36,101,13,2,0],
#           [1,21,17,2,1],
#           [12,0,2,1,0],
#           [0,0,2,0,0]
#           ]


# array = [[115,32,0,2,0],
#           [39,105,6,2,0],
#           [2,21,17,0,1],
#           [12,1,2,0,0],
#           [0,1,1,0,0]
#           ]
# df_cm = pd.DataFrame(array, index = [i for i in labels],
#                   columns = [i for i in labels])

# plt.figure(figsize = (10,8.5))
# sn.heatmap(df_cm/np.sum(df_cm), annot=True, fmt='.2%', cmap ='Blues')
# plt.show()

# array = [[109,39,1,0,0],
#           [46,100,6,0,0],
#           [1,29,11,0,0],
#           [10,3,2,0,0],
#           [0,1,1,0,0]
#           ]
# df_cm = pd.DataFrame(array, index = [i for i in labels],
#                   columns = [i for i in labels])

# plt.figure(figsize = (10,8.5))
# sn.heatmap(df_cm/np.sum(df_cm), annot=True, fmt='.2%', cmap ='Blues')
# plt.show()

# We had to do this manually because the library doesn't settle the case with division by 0.
# array = [[0.6566,0.2267,0.0476,0.0,00000.0000],
#           [0.2771,0.5814,0.2857,0.0000,0.0000],
#           [0.0060,0.1686,0.5238,0.0000,0.0000],
#           [0.0602,0.0174,0.0952,0.0000,0.0000],
#           [0.0000,0.0058,0.0476,0.0000,0.0000]
#           ]

df_cm = pd.DataFrame(array, index = [i for i in labels],
                  columns = [i for i in labels])
plt.figure(figsize = (10,7))
sn.heatmap(df_cm, annot=True, fmt='.2%', cmap ='Blues')
plt.show()