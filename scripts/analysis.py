import pandas as pd

from visualize import (
    draw_monthly_sales,
    draw_quarter_sales,
    draw_days_of_week_sales,
    draw_top_products
)

df_analysis = pd.read_csv('data/processed/features.csv')
df_analysis['SaleDate'] = pd.to_datetime(df_analysis['SaleDate'], errors='coerce')

if __name__ == "__main__":
    draw_monthly_sales(df_analysis)
    draw_quarter_sales(df_analysis)
    draw_days_of_week_sales(df_analysis)
    draw_top_products(df_analysis)



