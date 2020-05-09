import numpy as np
import os
import pandas as pd
import statistics

### Set your path to the folder containing the .csv files
PATH = './' # Use your path

### Fetch all files in path
fileNames = os.listdir(PATH)

### Filter file name list for files ending with .csv
fileNames = [file for file in fileNames if '.csv' in file]

count = 0

### Loop over all files
for file in fileNames:
    prices=[]
    dates =[]

    ### Read .csv file and append to list
    data = pd.read_csv(PATH + file)
    prices = np.append(prices,data.loc[:,['High']])
    dates = np.append(dates,data.loc[:,['Date']])

    c_index =np.where(dates == "2020-03-16")
    before = prices[:int(c_index[0])]
    after = prices[int(c_index[0]):]

    mean_b = statistics.mean(before)
    mean_a = statistics.mean(after)

    print(fileNames[count],mean_b, "Before")
    print(fileNames[count],mean_a, "After")

    count += 1
