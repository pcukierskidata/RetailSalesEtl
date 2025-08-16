import matplotlib.pyplot as plt
import mplcursors
import matplotlib.ticker as mtick

# --- Helper functions ---
def format_axis_as_millions(ax):
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x/1e6:.1f} mln'))

def add_interactive_cursor(ax):
    cursor = mplcursors.cursor(ax, hover=True)
    @cursor.connect("add")
    def on_add(sel):
        sel.annotation.set_text(f"{sel.target[1]:,.2f} zł")
        sel.annotation.get_bbox_patch().set(fc="white", alpha=0.8)

def finalize_plot(ax, xlabel=None, ylabel=None, title=None, rotate_xticks=None):
    if xlabel: plt.xlabel(xlabel)
    if ylabel: plt.ylabel(ylabel)
    if title: plt.title(title, fontsize=14)
    if rotate_xticks:
        plt.xticks(rotation=rotate_xticks, ha='right', fontsize=8)
    plt.tight_layout()
    plt.show()

# --- Chart functions ---
def draw_monthly_sales(df):
    monthly_sales = df.groupby(df['SaleDate'].dt.to_period('M'))['TotalValue'].sum()
    ax = monthly_sales.plot(kind='line', figsize=(12,6))
    finalize_plot(ax, xlabel='Sales Year and Month', ylabel='Monthly Sales Trend',
                  title='Monthly Sales Trend')

def draw_quarter_sales(df):
    quarter_sales = df.groupby('Quarter')['TotalValue'].sum()
    ax = quarter_sales.plot(kind='bar', figsize=(12,6))

    format_axis_as_millions(ax)
    add_interactive_cursor(ax)
    finalize_plot(ax, xlabel='Sales Quarter', ylabel='Total Sales Value', title='Quarterly Sales')

def draw_days_of_week_sales(df):
    day_sales = df.groupby('DayName')['TotalValue'].sum()
    day_sales = day_sales.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    ax = day_sales.plot(kind='bar', figsize=(12,6))

    format_axis_as_millions(ax)
    add_interactive_cursor(ax)
    finalize_plot(ax, title='Sales by Day of The Week')

def draw_top_products(df):
    top_products = df.groupby('ProductName')['TotalValue'].sum().sort_values(ascending=False).head(10)
    ax = top_products.plot(kind='bar', figsize=(12,6))
    
    format_axis_as_millions(ax)
    add_interactive_cursor(ax)
    finalize_plot(ax, title='Top 10 Best-Selling Products (value in millions)')