import argparse as ag
import datetime as dt
import csv
import pandas

import qstkutil.qsdateutil as du
import qstkutil.DataAccess as da

# working with arguments

argparser = ag.ArgumentParser(description="Take 3 agruments: cash, input and output file")

# add arguments
argparser.add_argument('cash', type=float)
argparser.add_argument('infile')
argparser.add_argument('outfile')

args = argparser.parse_args()

print "Starting with: " + str(args.cash)
print "Input file: " + args.infile
print "Output file: " + args.outfile + "\n"

# working with csv

orders = []

# open file's - use "with" because dont need close file manualy
with open(args.infile, 'rU') as infile:
    with open(args.outfile, 'w') as outfile:

        # read & write input/output file
        reader = csv.reader(infile, 'excel')
        writer = csv.writer(outfile)

        for row in reader:
            orders.append([dt.datetime(int(row[0]),int(row[1]),int(row[2]),16,0), \
                            row[3], row[4],int(row[5])])
            writer.writerow(row)

# output data from input file
for order in orders:
    print order

# waiting user's input
spam = raw_input('\nPress enter\n')

# get data from yahoo

# working with time and day when market is open
startday = min(orders)[0]
endday = max(orders)[0]
timeofday = dt.timedelta(hours=16)
timestamps = du.getNYSEdays(startday,endday,timeofday)


# create list data symbol
symbol = list(set(order[1] for order in orders))

# get data
dataobj = da.DataAccess('Yahoo')
close = dataobj.get_data(timestamps, symbol, 'close')


print startday
print endday
print symbol

#print '\n', close

# sum date and value close price
count = zip(close.index,close.values)

def buy_sell(action,tiker,cash):
    print cash
    for k in range(len(orders)):
        new_dt = close[(close.index == orders[k][0])]
        #print new_dt.tiker
        #tiker = close.columns
        #print tiker[0]

        if new_dt.index == orders[k][0]:
            if orders[k][2] == action and orders[k][1] == tiker:
               # print orders[k][1]
                price = new_dt.get(tiker)[0]
                #price = price[0]
                #print price
                cash = cash - price
                print cash
#                break

#        if orders[k][2] == action and orders[k][1] == tiker:
            ##price = close.GOOG
            #price = new_dt[(new_dt.index == orders[k][0])]
            #price = price.tiker # work price = price.GOOG
            #okay = price * orders[k][3]
            #cash = cash - okay
            ##print price

#buy_sell('Buy', 'AAPL', 100000)
#buy_sell('Sell', 'AAPL', 100000)

def func1(tiker):
    for k in range(len(orders)):
        if orders[k][1] == tiker:
            print close[tiker][orders[k][0]], orders[k][2]
func1("AAPL")
func1("IBM")

