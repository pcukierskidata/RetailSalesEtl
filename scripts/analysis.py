import pandas as pd

from visualize import (
    draw_monthly_sales,
    draw_quarter_sales,
    draw_days_of_week_sales,
    draw_top_products
)

df_analysis = pd.read_csv('data/processed/features.csv')

def show_basic_stats(df):
    print("Informacje o DataFrame: ")
    print(df.info())
    print("\nPodstawowe statystyki opisowe: ")
    print(df.describe())

def show_unique_counts(df):
    print(f"Liczba unikalnych klientów: {df['CustomerID'].nunique()}")
    print(f"Liczba unikalnych produktów: {df['ProductID'].nunique()}")
    print("\nLiczba zamówień w poszczególnych miesiącach:")
    print(df['MonthNamePL'].value_counts())

if __name__ == "__main__":
    show_basic_stats(df_analysis)
    show_unique_counts(df_analysis)
    draw_monthly_sales(df_analysis)
    draw_quarter_sales(df_analysis)
    draw_days_of_week_sales(df_analysis)
    draw_top_products(df_analysis)



