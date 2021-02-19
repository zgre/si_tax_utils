# Convert trade data into Makexml format (SI TAX - EDavki)

## Firstrade

```
convert_firstrade.py -i SAMPLE_FT_CSV.csv [-y 2020]
```

Input format on firstrade.com can be found here:

[Download data](https://invest.firstrade.com/cgi-bin/main#/content/myaccount/taxcenter/?h=overview&l=tax_download)

Download Account information and select Excel CSV files

![Screenshot](https://github.com/zgre/si_tax_utils/blob/master/firstrade.png?raw=true)

[Sample file](./SAMPLE_FT_CSV.csv) 

Supported transactions:

```
Buy
Sell
Interest
Dividend
```

Output:
    
    Writing trades into: input.txt
    
    Writing dividends into: dividends.csv
    
    Writing interests into: interests.csv


## ETORO

```
convert_etoro.py -i SAMPLE_ETORO_CSV.csv [-y 2020]
```


[Makexml and other tools](http://slotrade.blogspot.com/p/orodja.html)

