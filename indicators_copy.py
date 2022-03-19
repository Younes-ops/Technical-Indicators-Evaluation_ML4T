

import datetime as dt
import numpy as np  		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
import pandas as pd  	
import matplotlib.pyplot as plt 	  	   		  	  			  		 			     			  	 
from util import get_data, plot_data  
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

sd=dt.datetime(2008, 1, 1)
ed=dt.datetime(2009,12,31)
dates = pd.date_range(sd, ed)
symbols = ['JPM']
prices = get_data(symbols, dates)
prices =prices[symbols]
prices_normed= prices/prices.iloc[0,:]
rollingMean = prices_normed.rolling(window = 20, center=False).mean()
rollingStd = prices_normed.rolling(window = 20, center=False).std()
upperBB = rollingMean + (2 * rollingStd)
lowerBB = rollingMean - (2 * rollingStd)

def plotBollingerBands():
		print(prices_normed)
		plt.plot(prices_normed,label="JPM Normalized Price")
		plt.xlabel("Date")
		plt.ylabel("Values for Normalized Prices")
		plt.legend(loc='best')
		plt.xticks(rotation=30)
		plt.title("Indicator Bollinger Bands")
		plt.savefig("figures/BollingerBands.png")
		plt.close()


		# plt.plot(self.bollingerIndex,label="BB Value")
		# plt.xlabel("Date")
		# plt.ylabel("Values for Normalized Prices")
		# plt.legend(loc='best')
		# plt.xticks(rotation=30)
		# plt.title("Indicator BB Value")
		# plt.savefig("BB_Value.png")
		# plt.close()





if __name__ == "__main__":  		  	   		  	  			  		 			     			  	 
    plotBollingerBands()  		  	   		  	  			  		 			     			  	 
