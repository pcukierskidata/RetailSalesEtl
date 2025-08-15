import matplotlib.pyplot as plt
import mplcursors
import matplotlib.ticker as mtick

def draw_monthly_sales(df):
    monthly_sales = df.groupby(df['SaleDate'].dt.to_period('M'))['TotalValue'].sum()
    monthly_sales.plot(kind='line', figsize=(12,6), title='Monthly Sales Trend')
    plt.xlabel('Sales Year and Month')
    plt.ylabel('Monthly Sales Trend')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def draw_quarter_sales(df):
    quarter_sales = df.groupby('Quarter')['TotalValue'].sum()
    ax = quarter_sales.plot(kind='bar', figsize=(12,6), title='Quarterly Sales')
    
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x/1e6:.1f} mln'))

    add_cursor_for_plot(ax)
    
    plt.xlabel('Sales Quarter')
    plt.ylabel('Total Sales Value')
    plt.show()

def draw_days_of_week_sales(df):
    day_sales = df.groupby('DayName')['TotalValue'].sum()
    day_sales = day_sales.reindex(['Monday', 'Thursday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    ax = day_sales.plot(kind='bar', figsize=(12,6), title='Sales by Day of the Week')

    plt.xticks(rotation=90, ha='right', fontsize=8)
    plt.tight_layout()

    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x/1e6:.1f} mln'))

    add_cursor_for_plot(ax)

    plt.show()

def draw_top_products(df):
    top_products = df.groupby('ProductName')['TotalValue'].sum().sort_values(ascending=False).head(10)
    ax = top_products.plot(kind='bar', figsize=(12,6), color='skyblue', edgecolor='black')

    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.tight_layout()

    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x/1e6:.1f} mln'))

    for bar in ax.patches:
        bar.set_linewidth(0.5)
        bar.set_edgecolor('gray')
        bar.set_alpha(0.9)  

    add_cursor_for_plot(ax)

    plt.title("Top 10 Best-Selling Products (value in millions)", fontsize=14)
    plt.show()

def add_cursor_for_plot(ax):
    cursor = mplcursors.cursor(ax, hover=True)
    @cursor.connect("add")
    def on_add(sel):
        sel.annotation.set_text(f"{sel.target[1]:,.2f} zł")
        sel.annotation.get_bbox_patch().set(fc="white", alpha=0.8)
