import pandas as pd

df_sales = pd.read_csv('data/processed/sales.csv')
df_customers = pd.read_csv('data/processed/customers.csv')
df_products = pd.read_csv('data/processed/products.csv')

df_main = df_sales.merge(df_customers, on='CustomerID', how='left')
df_main = df_main.merge(df_products, on='ProductID', how='left')

df_main.to_csv('data/processed/main.csv')