import pandas as pd
import pyodbc
import datetime

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=PCUKIE\\SQLEXPRESS;'
    'DATABASE=PowerDatabase;'
    'Trusted_Connection=yes;'
)

df_sales = pd.read_sql("SELECT * FROM Sales", conn)
df_customers = pd.read_sql("SELECT * FROM Customers", conn)
df_products = pd.read_sql("SELECT * FROM Products", conn)

# sprawdzenie i uzupełnienie braków w danych
df_customers['City'] = df_customers['City'].fillna('Nieznane')
df_customers['RegistrationDate'] = df_customers['RegistrationDate'].fillna(datetime.date.today())

# usunięcie duplikatów
df_customers = df_customers.drop_duplicates()
df_sales = df_sales.drop_duplicates()
df_products = df_products.drop_duplicates()

# sprawdzenie i ewentualna konwersja typów danych
df_sales['SaleDate'] = pd.to_datetime(df_sales['SaleDate'])
df_customers['RegistrationDate'] = pd.to_datetime(df_customers['RegistrationDate'])

# sprawdzenie zakresów i wartości
from datetime import datetime
today = pd.to_datetime(datetime.today())

df_customers['RegistrationDate'] = pd.to_datetime(df_customers['RegistrationDate'], errors='coerce')
bad_registration_dates = df_customers[df_customers['RegistrationDate'].isna()]
future_registration_dates = df_customers[df_customers['RegistrationDate'] > today]

# zapis oczyszczonych danych do plików csv
df_sales.to_csv('data/processed/sales.csv', index=False)
df_customers.to_csv('data/processed/customers.csv', index=False)
df_products.to_csv('data/processed/products.csv', index=False)


