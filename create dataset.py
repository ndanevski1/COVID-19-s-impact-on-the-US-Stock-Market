# COVID-19's impact on the US Stock Market
# Done in collaboration of Muhammad Usama Ijaz and Nikola Danevski

import yfinance as yf
import pandas as pd
import numpy as np
import statistics
import math

def print_inventory(dct):
    print("Items held:")
    for item, amount in dct.items():
        print("{} ({})".format(item, amount))



top500_original = pd.read_csv("S&P top 500 - with new columns.csv")
top500 = top500_original.set_index("Symbol", drop = True)

count = 0
for company in top500_original['Symbol']:
	
	company_info = yf.Ticker(company)
	prices=[]
	dates=[]

	### Read .csv file and append to list
	data = yf.download(company, start="2019-11-15", end="2020-04-20",group_by="ticker")	#getting company data within range
	data.to_csv("temp.csv")
	data = pd.read_csv("temp.csv")

	prices = np.append(prices,data.loc[:,['High']])
	dates = np.append(dates,data.loc[:,['Date']])

	c_index =np.where(dates == "2020-03-16")
	before = [1,2,3,4]
	after = [1,2,3,4]
	try:
		before = prices[:int(c_index[0])]
		after = prices[int(c_index[0]):]
	except:
		pass

	mean_b = statistics.mean(before)
	mean_a = statistics.mean(after)

	diff_mean = ((mean_a/mean_b)-1)*100

	top500.loc[company,'Percentage Increase/Decrease'] = diff_mean 
	try:
		company_info = company_info.info # it's a hashmap
	except:
		pass

	comp_info = 'N/A'
	try:
		comp_info = company_info['fullTimeEmployees']	
	except:
		continue

	top500.loc[company,'Full Time Employees'] = comp_info
	comp_info = 'N/A'
	try:
		comp_info = company_info['state']		
	except:
		pass

	top500.loc[company,'State'] = comp_info
	comp_info = 'N/A'
	try:
		comp_info = company_info['enterpriseValue']		
	except:
		pass

	top500.loc[company,'Enterprise Value'] = comp_info
	comp_info = 'N/A'
	try:
		comp_info = company_info['profitMargins']		
	except:
		pass

	top500.loc[company,'Profit Margins'] = comp_info
	comp_info = 'N/A'
	try:
		comp_info = company_info['marketCap']		
	except:
		pass

	top500.loc[company,'Market Cap'] = comp_info
	comp_info = 'N/A'
	try:
		comp_info = company_info['askSize']		
	except:
		pass

	top500.loc[company,'Ask Size'] = comp_info
	count += 1
	print(count, company)

# print(top500.to_string())
top500.to_csv("Dataset - Resulting.csv",index = False)