import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Set your path to the folder containing the .csv files
PATH = './' # Use your path

### Fetch all files in path
fileNames = os.listdir(PATH)

### Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

count = 0

### Loop over all files
for file in fileNames:
    x=()
    y=()

    ### Read .csv file and append to list
    data = pd.read_csv(PATH + file)
    x=np.append(x,data.loc[:,['Date']])
    y=np.append(y,data.loc[:,['High']])


    x[78] = 'Covid-19'


    plt.scatter(x, y, label=fileNames[count])
    plt.xticks(x[::26], x[::26])
    # ax = plt.gca()
    # temp = ax.xaxis.get_ticklabels()
    # temp = list(set(temp) - set(temp[::3]))
    # for label in temp:
    #     label.set_visible(False)

    count += 1

    plt.legend()

### Generate the plot
plt.show()