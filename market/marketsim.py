import numpy as np

import qstkutil.qsdateutil as du
import qstkutil.tsutil as tsu
import qstkutil.DataAccess as da
import datetime as dt
import matplotlib.pyplot as plt
from pylab import *
import pandas


#### Get historical data
symbols = ['AAPL', 'IBM', 'GOOG', 'XOM']
startday = dt.datetime(2011, 1, 1)
endday = dt.datetime(2011, 12, 31)
timeofday = dt.timedelta(hours=16)
timestamps = du.getNYSEdays(startday,endday,timeofday)

dataobj = da.DataAccess('Yahoo')
close = dataobj.get_data(timestamps, symbols, "close")

plt.clf()
newtimestamps = close.index
pricedat = close.values
plt.plot(newtimestamps,pricedat)
savefig('test.pdf',format='pdf')

