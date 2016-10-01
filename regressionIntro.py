import pandas as pd
import quandl
quandl.ApiConfig.api_key = 'zbVYF2wtsx7RDNpx-iRi'
df = quandl.get('NSE/GOLDTECH')

#print(df.head())

df = df[['Open', 'High', 'Low', 'Close']]
df['HL_PCT'] = ((df['High'] - df['Open'])/ df['Open']) * 100
df['PCT_change'] = ((df['Close'] - df['Open'])/ df['Open']) * 100

df = df[['Close', 'Open', 'HL_PCT', 'PCT_change']]

print(df.head())