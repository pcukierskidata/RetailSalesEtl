import matplotlib.pyplot as plt

def draw_monthly_sales(df):
    monthly_sales = df.groupby(df['SaleDate'].dt.to_period('M'))['TotalValue'].sum()
    monthly_sales.plot(kind='line', figsize=(12,6), title='Miesięczny trend sprzedaży')
    plt.xlabel('Rok i miesiąc sprzedaży')
    plt.ylabel('Trend miesięcznej sprzedaży')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def draw_quarter_sales(df):
    quarter_sales = df.groupby('Quarter')['TotalValue'].sum()
    quarter_sales.plot(kind='bar', figsize=(8,5), title='Sprzedaż według kwartałów')
    plt.xlabel('Kwartał sprzedaży')
    plt.ylabel('Suma wartości sprzedaży')
    plt.show()

def draw_days_of_week_sales(df):
    day_sales = df.groupby('DayOfWeekName')['TotalValue'].sum()
    day_sales = day_sales.reindex(['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela'])
    day_sales.plot(kind='bar', figsize=(8,5), title='Sprzedaż wg dni tygodnia')
    plt.show()

def draw_top_products(df):
    top_products = df.groupby('ProductID')['TotalValue'].sum().sort_values(ascending=False).head(10)
    top_products.plot(kind='bar', title='TOP 10 najlepiej sprzedających się produktów')
    plt.show()

