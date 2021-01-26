# Convert Firstrade tax data into Makexml format (SI TAX - EDavki)

```
convert_firstrade.py -i FT_CSV_SAMPLE.csv [-y 2020]
```

Input format on firstrade.com can be found here:

[Download data](https://invest.firstrade.com/cgi-bin/main#/content/myaccount/taxcenter/?h=overview&l=tax_download)

Download Account information and select Excel CSV files

![Screenshot](https://github.com/zgre/si_tax_utils/blob/master/firstrade.png?raw=true)

[Sample file](./SAMPLE_FT_CSV.csv) 

Output:
    
    Writing trades into: input.txt
    
    Writing dividends into: dividends.csv
    
    Writing interests into: interests.csv

[Makexml and other tools](http://slotrade.blogspot.com/p/orodja.html)

