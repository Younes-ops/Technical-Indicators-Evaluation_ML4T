

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


# We add data before the starting date so we avoid getting NANs for the fisrt days 
days_to_add = dt.timedelta(40)
sd_adjusted = sd - days_to_add
prices_history = get_data(symbols, pd.date_range(sd_adjusted, ed))[symbols]


def SMA():
    sma = prices_normed.rolling(window = 20, center=False).mean()
    sma_by_price = sma / prices_normed


    fig, axs = plt.subplots(2,constrained_layout=True,gridspec_kw={'height_ratios': [3, 1]})

    # fig.suptitle("Indicator Price/SMA")
    axs[0].plot(prices_normed,label='Prices normed')
    axs[0].plot(sma,label="SMA")
    axs[0].grid()
    axs[0].legend(loc='best')
    axs[0].set(xlabel='Date', ylabel='Price',title ='Price and SMA')
    axs[0].tick_params(labelrotation=30)


    axs[1].plot(sma_by_price, label="SMA/Price")
    axs[1].axhline(y=1.1,ls='--',c='r')
    axs[1].axhline(y=0.9,ls='--',c='g')
    axs[1].grid()
    axs[1].legend(loc='best')
    axs[1].set(xlabel='Date', ylabel='Ratio',title ='Price / SMA')
    axs[1].tick_params(labelrotation=30)

    
    plt.savefig("sma_by_price.png")
    plt.close()


def BollingerBands():
    
    rollingMean = prices_normed.rolling(window = 20, center=False).mean()
    rollingStd = prices_normed.rolling(window = 20, center=False).std()
    upperBB = rollingMean + (2 * rollingStd)
    lowerBB = rollingMean - (2 * rollingStd)
    BBP= (prices_normed - lowerBB) /(upperBB - lowerBB)

    fig, axs = plt.subplots(2,constrained_layout=True,gridspec_kw={'height_ratios': [3, 1]})

    fig.suptitle("Indicator Price/SMA")
    axs[0].plot(prices_normed,label='Prices normed')
    axs[0].plot(upperBB, label="Upper band")
    axs[0].plot(lowerBB, label="Lower band")
    axs[0].grid()
    axs[0].legend(loc='best')
    axs[0].set(xlabel='Date', ylabel='Values for Normalized Prices',title='Bollinger Bands')
    axs[0].tick_params(labelrotation=30)

    axs[1].plot(BBP,label="BB percentage")
    axs[1].axhline(y=0,ls='--',c='g')
    axs[1].axhline(y=1,ls='--',c='r')
    axs[1].grid()
    axs[1].legend(loc='best')
    axs[1].set(xlabel='Date', ylabel='Percentage',title='BB percentage')
    axs[1].tick_params(labelrotation=30)

    plt.savefig("BollingerBands_indicator.png")
    plt.close()


def MACD():

    ema12 = prices_history.ewm(span=12, adjust=False,min_periods=12).mean()
    ema26 = prices_history.ewm(span=26, adjust=False,min_periods=26).mean()
    macd = ema12 - ema26
    macd_signal = macd.ewm(span=9, adjust=False,min_periods=9).mean()

    ema12=ema12[sd:]
    ema26=ema26[sd:]
    macd=macd[sd:]
    macd_signal=macd_signal[sd:]
    
    plt.plot(macd,label="MACD")
    plt.plot(macd_signal, label="MACD Sinal")
    plt.grid()
    plt.legend(loc='best')
    plt.xticks(rotation=30)
    plt.xlabel("Date")
    plt.ylabel("Values for Normalized Prices")
    plt.title("Indicator MACD")
    plt.savefig("figures/MACD.png")
    plt.close()


def Momemtum():
    days =20
    momemtum =  prices_history / prices_history.shift(days) -1
    momentum = momemtum[sd:]
    # plt.plot(macd,label="MACD")

    fig, axs = plt.subplots(2,constrained_layout=True,gridspec_kw={'height_ratios': [3, 1]})

    # fig.suptitle("Indicator Price/SMA")
    axs[0].plot(prices_normed,label='Prices normed')
    axs[0].grid()
    axs[0].legend(loc='best')
    axs[0].set(xlabel='Date', ylabel='Price',title ='Stock Price Normed')
    axs[0].tick_params(labelrotation=30)


    axs[1].plot(momentum, label="Momentum",c='g')
    axs[1].grid()
    axs[1].legend(loc='best')
    axs[1].set(xlabel='Date', ylabel='Momentum',title ='Momentum')
    axs[1].tick_params(labelrotation=30)
    plt.savefig("Momentum.png")
    plt.close()

def Stochastic_Oscillator():

    prices_high=get_data(symbols, pd.date_range(sd_adjusted, ed),colname='High')[symbols]
    prices_low=get_data(symbols, pd.date_range(sd_adjusted, ed),colname='Low')[symbols]

    high14 = prices_high.rolling(14).max()
    low14 = prices_low.rolling(14).min()

    K_percent = 100 * (prices_history - low14)/(high14 - low14)
    D_percent = K_percent.rolling(3).mean()

    # We keep only the data for our time periode
    high14 = high14[sd:]
    low14 = low14[sd:]
    K_percent = K_percent[sd:]
    D_percent = D_percent[sd:]

    plt.plot(K_percent,label="%K")
    plt.plot(D_percent, label="%D")
    plt.axhline(y=80,ls='--',c='r')
    plt.axhline(y=20,ls='--',c='g')
    plt.grid()
    plt.legend(loc='best')
    plt.xticks(rotation=30)
    plt.xlabel("Date")
    plt.ylabel("Percentage")
    plt.title("Indicator Stochastic Oscillator")
    plt.savefig("Stochastic_Oscillator.png")
    plt.close()

def test_function():
    SMA()		
    BollingerBands()  
    MACD()
    Momemtum()
    Stochastic_Oscillator()	

def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "ybouzekraoui3" 

if __name__ == "__main__":  		  	   		  	  			  		 			     			  	 
    test_function()		  	  			  		 			     			  	 
