#!/usr/bin/env python3

import csv
from operator import itemgetter
import getopt,sys
from collections import defaultdict
import datetime


year = '2020'
input_trades = 'SAMPLE_ETORO.csv'

output_trades='input.txt'

def usage():
    print('ERROR: Missing parameters: ')
    print('convert_etoro.py -i SAMPLE_ETORO.csv [-y 2020]')

def main(argv):

    global year
    global input_trades

    transactions = []
    ticker_count = {}
    
    req = False
    try:
        opts, _ = getopt.getopt(argv,"hi:y:")
    except:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == "-i":
            input_trades = arg
            req = True
        elif opt == "-y":
            year = arg
    
    if not req:
        usage()
        sys.exit(2)

    print(f'Processing {input_trades} for {year}')
    with open(input_trades) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            sell = {}
            buy = {}    

            if year in row['Close Date']:
                ticker = row['Action'].split(None,1)[1]
                if ticker not in ticker_count:
                    ticker_count[ticker] = 0
                else:
                    ticker_count[ticker] += 1

                buy = {'Ticker': ticker,
                        'Transaction Type': 'Buy',
                        'Date': datetime.datetime.strptime(row['Open Date'],"%d/%m/%Y %H:%M").strftime("%Y-%m-%d"),
                        'Shares': row['Units'].strip(),
                        'Price': row['Open Rate'].strip(),
                        'ValidLoss': 'true',
                        'Transaction Id': ticker_count[ticker]}

                ticker_count[ticker] += 1
                sell = {'Ticker': ticker,
                        'Transaction Type': 'Sell',
                        'Date': datetime.datetime.strptime(row['Close Date'],"%d/%m/%Y %H:%M").strftime("%Y-%m-%d"),
                        'Shares': row['Units'].strip(),
                        'Price': row['Close Rate'].strip(),
                        'ValidLoss': 'true',
                        'Transaction Id': ticker_count[ticker]}  
                
                transactions.append(buy)
                transactions.append(sell)

    print(ticker_count)
    sorted_transactions = sorted(transactions, key=itemgetter('Ticker'))                   
    # header Ticker;Transaction Id;Transaction Type (Buy/Sell/SellShort/BuyCover);Date;Shares;Price;Loss Valid (true/false)
    fieldnames = ['Ticker','Transaction Id','Transaction Type','Date','Shares','Price','ValidLoss']
    with open(output_trades, 'w', newline='') as csvfile:
        fieldnames = ['Ticker','Transaction Id','Transaction Type','Date','Shares','Price','ValidLoss']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        #writer.writeheader()
        print(f'Writing trades into: {output_trades}')
        writer.writerows(sorted_transactions)

if __name__ == "__main__":
   main(sys.argv[1:])