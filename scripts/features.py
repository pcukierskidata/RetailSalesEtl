import pandas as pd

df_main = pd.read_csv('data/processed/main.csv')

# konwersja SaleDate na datetime
df_main['SaleDate'] = pd.to_datetime(df_main['SaleDate'])

df_main['YearMonth'] = df_main['SaleDate'].dt.to_period('M')
df_main['DayName'] = df_main['SaleDate'].dt.day_name()
df_main['Quarter'] = 'Q' + df_main['SaleDate'].dt.quarter.astype(str)
df_main['TotalValue'] = df_main['UnitPrice'] * df_main['Quantity']

df_main.to_csv('data/processed/features.csv', index=False)