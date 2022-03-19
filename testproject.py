import indicators as Ind
import marketsimcode
import TheoreticallyOptimalStrategy as TOS
import datetime as dt


def author():  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    :return: The GT username of the student  		  	   		  	  			  		 			     			  	 
    :rtype: str  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    return "ybouzekraoui3"

if __name__ == "__main__":  		  	   		  	  			  		 			     			  	 
    orders=TOS.testPolicy(symbol='JPM', sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000) 
    TOS.test_code()

    Ind.test_function()
