# Convert Firstrade tax data into Makexml format

```
convert_firstrade.py -i FT_CSV_SAMPLE.csv [-y 2020]
```

Input format on firstrade.com can be found here:

[Download data](https://invest.firstrade.com/cgi-bin/main#/content/myaccount/taxcenter/?h=overview&l=tax_download)

Download Account infromation and select Excel CSV files

[Sample file](./SAMPLE_FT_CSV.csv) 

Output:
    Writing trades into: input.txt
    Writing dividends into: dividends.csv
    Writing interests into: interests.csv

