#!/usr/bin/env python3

import csv
from operator import itemgetter
import getopt,sys

year = '2020'
input_trades = 'SAMPLE_FT_CSV.csv'

output_trades='input.txt'
dividends_out='dividends.csv'
interests_out='interests.csv'

def usage():
    print('ERROR: Missing parameters: ')
    print('convert_firstrade.py -i SAMPLE_FT_CSV.csv [-y 2020]')

def main(argv):

    global year
    global input_trades

    year_sells = {}
    transactions = []
    dividends = []
    interests = []

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
            if len(row['Symbol']) > 0:
                transaction_type = ''
                if row['Action'] == 'BUY':
                    transaction_type = 'Buy'
                elif row['Action'] == 'SELL':    
                    transaction_type = 'Sell'
                    if year in row['TradeDate']:
                        year_sells[row['Symbol'].strip()] = True
                elif row['Action'] == 'Dividend':
                    if year in row['TradeDate']:
                        dividends.append({'Ticker': row['Symbol'].strip(),
                                    'Transaction Type': row['Action'],
                                    'Date': row['TradeDate'].strip(),
                                    'Shares': int(abs(float(row['Quantity'].strip()))),
                                    'Price': row['Amount'].strip(),
                                    'ValidLoss': 'false'})
                elif row['Action'] == 'Interest':
                    if year in row['TradeDate']:
                        interests.append({'Transaction Type': row['Action'],
                                    'Date': row['TradeDate'].strip(),
                                    'Price': row['Amount'].strip()})
                if len(transaction_type) > 0:
                    transactions.append({'Ticker': row['Symbol'].strip(),
                                'Transaction Type': transaction_type,
                                'Date': row['TradeDate'].strip(),
                                'Shares': int(abs(float(row['Quantity'].strip()))),
                                'Price': row['Price'].strip()})    
                        
    sorted_transactions = sorted(transactions, key=itemgetter('Ticker', 'Date'))        
    found_ticker = {}
    # header Ticker;Transaction Id;Transaction Type (Buy/Sell/SellShort/BuyCover);Date;Shares;Price;Loss Valid (true/false)
    fieldnames = ['Ticker','Transaction Id','Transaction Type','Date','Shares','Price','ValidLoss']
    with open(output_trades, 'w', newline='') as csvfile:
        fieldnames = ['Ticker','Transaction Id','Transaction Type','Date','Shares','Price','ValidLoss']
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        #writer.writeheader()
        print(f'Writing trades into: {output_trades}')
        for t in sorted_transactions:
            if t['Ticker'] in found_ticker:
                found_ticker[t['Ticker']] = found_ticker[t['Ticker']] + 1
            else:
                found_ticker[t['Ticker']] = 0
            if t['Ticker'] in year_sells:
                t['Transaction Id'] = found_ticker[t['Ticker']]
                writer.writerow(t)

    with open(dividends_out, 'w', newline='') as divfile:
        print(f'Writing dividends into: {dividends_out}')
        div_writer = csv.DictWriter(divfile, fieldnames=fieldnames)
        div_writer.writerows(dividends)

    with open(interests_out, 'w', newline='') as intfile:
        print(f'Writing interests into: {interests_out}')
        int_writer = csv.DictWriter(intfile, fieldnames=fieldnames)
        int_writer.writerows(interests)

if __name__ == "__main__":
   main(sys.argv[1:])