import pandas as pd
from scripts.visualizations.matplotlib.mappers import MONTH_NAME_PL
from scripts.visualizations.matplotlib.mappers import DAY_NAME_PL

df_main = pd.read_csv('data/processed/main.csv')

# dodanie kolumn pomocniczych

# konwersja SaleDate na datetime
df_main['SaleDate'] = pd.to_datetime(df_main['SaleDate'])

df_main['YearMonth'] = df_main['SaleDate'].dt.to_period('M')
df_main['DayName'] = df_main['SaleDate'].dt.day_name()
df_main['Quarter'] = 'Q' + df_main['SaleDate'].dt.quarter.astype(str)
df_main['TotalValue'] = df_main['UnitPrice'] * df_main['Quantity']

# nazwa miesiąca - po polsku
# df_main['MonthNamePL'] = df_main['SaleDate'].dt.month_name().map(MONTH_NAME_PL)

# nazwa dnia tygodnia - po polsku
# df_main['DayOfWeekName'] = df_main['SaleDate'].dt.day_name().map(DAY_NAME_PL)

df_main.to_csv('data/processed/features.csv', index=False)