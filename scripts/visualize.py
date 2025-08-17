import sys
import matplotlib.pyplot as plt
import mplcursors
import matplotlib.ticker as mtick
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors

# --- Configuration ---
MODE = "technical"
if len(sys.argv) > 1:
    MODE = sys.argv[1].lower()
    if MODE not in ["technical", "business"]:
        MODE = "technical"

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

def add_hover_highlight(fig, bars, highlight_color="gold", fade_alpha=0.6):
    def on_hover(event):
            for bar in bars:
                if bar.contains(event)[0]:
                    bar.set_alpha(1.0)
                    bar.set_edgecolor(highlight_color)
                    bar.set_linewidth(2)
                else:
                    bar.set_alpha(fade_alpha)
                    bar.set_edgecolor("black")
                    bar.set_linewidth(1)
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", on_hover)

# --- Chart functions ---
def draw_monthly_sales(df):
    monthly_sales = df.groupby(df['SaleDate'].dt.to_period('M'))['TotalValue'].sum()
    
    if MODE == "business":
        ax = monthly_sales.plot(kind='line', figsize=(12,6), color="royalblue", linewidth=2.5, marker="o")
    else:
        ax = monthly_sales.plot(kind='line', figsize=(12,6))

    format_axis_as_millions(ax)
    finalize_plot(ax, xlabel='Sales Year and Month', ylabel='Monthly Sales Trend',
                  title='Monthly Sales Trend')

def draw_quarter_sales(df):
    quarter_sales = df.groupby('Quarter')['TotalValue'].sum()
    
    if MODE == "business":
        fig, ax = plt.subplots(figsize=(12,6))
        cmap = mcolors.LinearSegmentedColormap.from_list("", ["seagreen", "lightgreen"])
        colors = [cmap(i/len(quarter_sales)) for i in range(len(quarter_sales))]
        bars = ax.bar(quarter_sales.index, quarter_sales.values, color=colors, edgecolor="black")

        add_hover_highlight(fig, bars)
    else:
        ax = quarter_sales.plot(kind='bar', figsize=(12,6))
    
    format_axis_as_millions(ax)
    add_interactive_cursor(ax)
    finalize_plot(ax, xlabel='Sales Quarter', ylabel='Total Sales Value', title='Quarterly Sales')

def draw_days_of_week_sales(df):
    day_sales = df.groupby('DayName')['TotalValue'].sum()
    day_sales = day_sales.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    if MODE == "business":
        fig, ax = plt.subplots(figsize=(12,6))
        cmap = mcolors.LinearSegmentedColormap.from_list("", ["seagreen", "lightgreen"])
        colors = [cmap(i/len(day_sales)) for i in range(len(day_sales))]
        bars = ax.bar(day_sales.index, day_sales.values, color=colors, edgecolor="black")

        add_hover_highlight(fig, bars)
    else:
        ax = day_sales.plot(kind='bar', figsize=(12,6))

    format_axis_as_millions(ax)
    add_interactive_cursor(ax)
    finalize_plot(ax, title='Sales by Day of The Week')

def draw_top_products(df):
    top_products = df.groupby('ProductName')['TotalValue'].sum().sort_values(ascending=False).head(10)

    if MODE == "technical":
        ax = top_products.plot(kind='bar', figsize=(12,6))
    else:
        colors = plt.cm.tab10(range(len(top_products)))
        ax = top_products.plot(kind='bar', figsize=(12,6), color=colors)

        handles = [
            mpatches.Patch(color=c, label=label)
            for c, label in zip(colors, top_products.index)
        ]

        ax.legend(
            handles=handles,
            title="Products",
            bbox_to_anchor=(1.02, 1),
            loc="upper left",
            borderaxespad=0.0
        )

        ax.set_xticklabels([])
        plt.tight_layout(rect=[0, 0, 0.8, 1])

    format_axis_as_millions(ax)
    add_interactive_cursor(ax)
    finalize_plot(ax, title='Top 10 Best-Selling Products (value in millions)', xlabel='')
