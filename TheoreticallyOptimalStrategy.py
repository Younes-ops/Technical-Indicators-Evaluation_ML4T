"""		  	   		  	  			  		 			     			  	 	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 
Student Name: Younes EL BOUZEKRAOUI   		  	  			  		 			     			  	 
GT User ID: ybouzekraoui3   		  	   		  	  			  		 			     			  	 
GT ID: 903738099 			  	   		  	  			  		 			     			  	 
"""  

import datetime as dt
from distutils.command.build_py import build_py  		  	   		  	  			  		 			     			  	 
import os  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import numpy as np  		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
import pandas as pd  	
import matplotlib.pyplot as plt 	  	   		  	  			  		 			     			  	 
from util import get_data, plot_data  
import marketsimcode
import sys	 

def testPolicy(symbol='JPM', sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000) :
    dates = pd.date_range(sd, ed)
    symbols = [symbol]
    prices = get_data(symbols, dates)
    # print(prices.iloc[250:300])

    orders = prices[[symbol]].copy()
    orders[:]=0
    orders.columns=['Shares']

    previous_order = 0
    for i in range(orders.shape[0]-1):
        if prices.iloc[i+1][symbol] > prices.iloc[i][symbol] :
            orders.iloc[i] = 1000 - previous_order
            previous_order = 1000
        elif prices.iloc[i+1][symbol] < prices.iloc[i][symbol] :
            orders.iloc[i] = -1000 - previous_order
            previous_order = -1000
        else:
            orders.iloc[i] = 0
            prev_order=0



    return orders

def test_code(): 
    sd=dt.datetime(2008, 1, 1)
    ed=dt.datetime(2009,12,31)
    sv = 100000
    orders=testPolicy('JPM',sd,ed,sv)
    # print(orders)
    port_vals=marketsimcode.compute_portvals(orders=orders,symbol='JPM')
    cr,adr,sddr,sr = marketsimcode.get_statistics(port_vals) 



    port_vals_normed=port_vals/port_vals.iloc[0,:]

    Benchmark_orders = orders.copy()
    Benchmark_orders[:]=0
    Benchmark_orders.iloc[0]=1000
    Benchmark_port_vals=marketsimcode.compute_portvals(orders=Benchmark_orders,symbol='JPM')
    cr_bench,adr_bench,sddr_bench,sr_bench = marketsimcode.get_statistics(Benchmark_port_vals) 

    Benchmark_port_vals_normed=Benchmark_port_vals/Benchmark_port_vals.iloc[0,:]
    sys.stdout = open("p6_results.txt", "w")
    print()
    print(f"Date Range: {sd} to {ed}") 
    print('--------------------------------------------------------------------------')	
    print('                                   TOS                 Benshmark       ')
    print('--------------------------------------------------------------------------')	  	   		  	  			  		 			     			  	   		  	   		  	  			  		 			     			  	 
    print(f"Sharpe Ratio                    {round(sr[0],6)}               {round(sr_bench[0],6)}") 
    print('--------------------------------------------------------------------------')			  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 		  	   		  	  			  		 			     			  	 
    print(f"Cumulative Return               {round(cr[0],6)}                 {round(cr_bench[0],6)}")  		  	   		  	  			  		 			     			  	 
    print('--------------------------------------------------------------------------')		  	   		  	  			  		 			     			  	  		  	   		  	  			  		 			     			  	 
    print(f"Standard Deviation              {round(sddr[0],6)}               {round(sddr_bench[0],6)}")
    print('--------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Average Daily Return            {round(adr[0],6)}               {round(adr_bench[0],6)}") 
    print('--------------------------------------------------------------------------')  		  	   		  	  			  		 			     			  	 
    print(f"Final Portfolio Value:          {round(port_vals.iloc[-1][0],6)}               {round(Benchmark_port_vals.iloc[-1][0],6)}")
    print('--------------------------------------------------------------------------')		
    # print(port_vals.iloc[250:300])


    df_temp = pd.concat(  		  	   		  	  			  		 			     			  	 
            [port_vals_normed, Benchmark_port_vals_normed], keys=["Portfolio", "Benchmark"], axis=1  		  	   		  	  			  		 			     			  	 
        )  		  	   		  	  			  		 			     			  	 
    ax = df_temp.plot(title="Theoretically optimal strategy vs Benchmark ",color=['r','purple'], grid=True, fontsize=12)
    ax.legend(['Theoretically optimal strategy','Benchmark strategy'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized daily portfolio value")
    fig = ax.get_figure()
    fig.savefig('TOSvsBenchmark.png')
    plt.close()

    # print(df_temp)

    sys.stdout.close()
def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "ybouzekraoui3"

if __name__ == "__main__":  		  	   		  	  			  		 			     			  	 
    test_code()  