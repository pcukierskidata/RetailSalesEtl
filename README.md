# Retail Sales ETL Pipeline

This project demonstrates a full **ETL pipeline** for retail sales data using Python and Pandas, including data extraction, cleaning, transformation, integration, feature engineering, and visualization. The notebook walks step by step through the process of preparing raw data for business analysis and reporting.

---

## Project Overview

The project is structured around the following stages:

### 1. Data Cleaning (ETL - Extract & Clean)

- **Extract data** from a local SQL Server database.
- **Handle missing values**:
  - `'City'` → replaced with `'Nieznane'`
  - `'RegistrationDate'` → replaced with current date if missing
- **Remove duplicates and convert data types**:
  - `'SaleDate'` and `'RegistrationDate'` → converted to `datetime`
- **Validate dates**:
  - Detect invalid dates
  - Flag registration dates in the future
- **Save cleaned data** to `data/processed` as CSV files.

---

### 2. Data Integration

- Load cleaned CSV files: `sales.csv`, `customers.csv`, `products.csv`.
- **Merge tables**:
  - `sales + customers` (LEFT JOIN on `CustomerID`)
  - Result + `products` (LEFT JOIN on `ProductID`)
- Save the integrated dataset as `main.csv`.

> The final table includes both transactional data and detailed customer/product information.

---

### 3. Feature Engineering

- Add new columns to support analysis:
  - `YearMonth` (year and month of sale)
  - `DayName` (day of the week)
  - `Quarter` (sales quarter)
  - `TotalValue` (`UnitPrice * Quantity`)
- Save updated dataset for visualization.

---

### 4. Visualizations

Multiple charts are created to explore and present data trends:

- **Monthly Sales Trend** (line chart)  
- **Quarterly Sales** (bar chart)  
- **Sales by Day of the Week** (bar chart)  
- **Top 10 Best-Selling Products** (bar chart with legend)  
- **Product vs. Quarter Heatmap** (heatmap of sales value)

Charts can be displayed in **two modes**:  
- **Technical** → basic plots for data inspection  
- **Business** → visually enhanced plots for reporting

--- 

## Notebook Access

You can view the full Jupyter Notebook for this project at:

[RetailSalesEtl/RetailSalesEtl/Notebooks/ETL_report.ipynb](RetailSalesEtl/RetailSalesEtl/Notebooks/ETL_report.ipynb)
