import pandas as pd
from pathlib import Path

def load_sales_data():
    """Load and return the final processed sales data."""
    final_path = Path(r'Data\processed\sales_data_final.csv')
    df = pd.read_csv(final_path, encoding='ISO-8859-1')
    return df


def total_sales_by_year(df_sales):
    """Calculate total sales grouped by year"""
    result = df_sales.groupby('YEAR_ID')['SALES'].sum().reset_index()
    result.columns = ['Year', 'Total Sales']
    print("== Total Sales By Year: ==")
    print(result)


def total_sales_by_quarter(df_sales):
    """Calculate total sales grouped by quarter"""
    result = df_sales.groupby('QTR_ID')['SALES'].sum().reset_index()
    result.columns = ['Quarter', 'Total Sales']
    print("== Total Sales By Quarter: ==")
    print(result)


def total_sales_by_month(df_sales):
    """Calculate total sales grouped by month"""
    result = df_sales.groupby('MONTH_ID')['SALES'].sum().reset_index()
    result.columns = ['Month', 'Total Sales']
    print("== Total Sales By Month: ==")
    print(result)


def top_selling_products(df_sales):
    """Display top 10 products by total sales"""
    result = df_sales.groupby('PRODUCTCODE')['SALES'].sum().reset_index()
    result = result.sort_values(by='SALES', ascending=False)
    print("== Top Selling Products: ==")
    print(result.head(10))


def sales_by_product_line(df_sales):
    """Calculate total sales per product line"""
    result = df_sales.groupby('PRODUCTLINE')['SALES'].sum().reset_index()
    result = result.sort_values(by='SALES', ascending=False)
    print("== Sales by Product Line: ==")
    print(result.to_string())


def avg_price_vs_msrp(df_sales):
    """Compare average selling price vs MSRP per product line"""
    df_temp = df_sales.copy()
    df_temp['AVG_PRICE'] = df_temp['SALES'] / df_temp['QUANTITYORDERED']
    result = df_temp.groupby('PRODUCTLINE').agg({
        'AVG_PRICE': 'mean',
        'MSRP': 'mean'
    }).reset_index()
    result.columns = ['Product Line', 'Avg Selling Price', 'Avg MSRP']
    print("== Average Selling Price vs. MSRP by Product Line ==")
    print(result.sort_values(by='Product Line'))


def top_customers_by_sales(df_sales):
    """Show top 10 customers by total sales"""
    result = df_sales.groupby('CUSTOMERNAME')['SALES'].sum().reset_index()
    result.columns = ['Customer Name', 'Total Sales']
    result = result.sort_values(by='Total Sales', ascending=False)
    print("== Top Customers by Sales: ==")
    print(result.head(10))


def orders_count_per_customer(df_sales):
    """Count orders per customer"""
    result = df_sales.groupby('CUSTOMERNAME')['ORDERNUMBER'].nunique().reset_index()
    result.columns = ['Customer Name', 'Order Count']
    result = result.sort_values(by='Order Count', ascending=False)
    print("== Orders Count per Customer: ==")
    print(result.head(10))


def sales_trend_over_time(df_sales):
    """Show sales trend by year and month"""
    result = df_sales.groupby(['YEAR_ID', 'MONTH_ID'])['SALES'].sum().reset_index()
    result.columns = ['Year', 'Month', 'Total Sales']
    result = result.sort_values(by=['Year', 'Month'])
    result['Total Sales'] = result['Total Sales'].round(2)
    print("== Sales Trend Over Time: ==")
    print(result)


def average_order_value(df_sales):
    """Calculate average value per order"""
    total_sales = df_sales['SALES'].sum()
    num_orders = df_sales['ORDERNUMBER'].nunique()
    avg_order_value = total_sales / num_orders
    print("== Average Order Value: ==")
    print(f"Average Order Value: {avg_order_value:.2f}")


def most_common_status(df_sales):
    """Find most common order status"""
    status_counts = df_sales['STATUS'].value_counts()
    most_common = status_counts.idxmax()
    count = status_counts.max()
    print(f"Most common status: {most_common} with {count} occurrences")


def sales_by_deal_size(df_sales):
    """Total sales by deal size"""
    result = df_sales.groupby('DEALSIZE')['SALES'].sum().reset_index()
    result.columns = ['DEALSIZE', 'Total Sales']
    result = result.sort_values(by='Total Sales', ascending=False)
    print("== Total Sales By DEALSIZE: ==")
    print(result)


def top_cities_by_sales(df_sales):
    """Top 10 cities by sales"""
    result = df_sales.groupby('CITY')['SALES'].sum().reset_index()
    result.columns = ['CITY', 'Total Sales']
    result = result.sort_values(by='Total Sales', ascending=False)
    print("== Top Selling By CITY: ==")
    print(result.head(10))


def productline_sales_ratio(df_sales):
    """Calculate percentage sales ratio per product line"""
    sales_per_productline = df_sales.groupby('PRODUCTLINE')['SALES'].sum().reset_index()
    total_sales = sales_per_productline['SALES'].sum()
    sales_per_productline['Sales Ratio (%)'] = (sales_per_productline['SALES'] / total_sales) * 100
    result = sales_per_productline.sort_values(by='Sales Ratio (%)', ascending=False)
    print("== Product Line Sales Ratio: ==")
    print(result[['PRODUCTLINE', 'Sales Ratio (%)']])


def repeat_order_customers(df_sales):
    """Show customers with more than one order"""
    orders_per_customer = df_sales.groupby('CUSTOMERNAME')['ORDERNUMBER'].nunique().reset_index()
    orders_per_customer.columns = ['Customer', 'Order Count']
    repeat_customers = orders_per_customer[orders_per_customer['Order Count'] > 1]
    print("== Customers with Repeat Orders: ==")
    print(repeat_customers.sort_values(by='Order Count', ascending=False))


def all_analysis():
    """Run all analysis functions in sequence"""
    df_sales = load_sales_data()
    
    print("\n" + "="*50)
    print("STARTING DATA ANALYSIS")
    print("="*50 + "\n")
    
    total_sales_by_year(df_sales)
    total_sales_by_quarter(df_sales)
    total_sales_by_month(df_sales)
    top_selling_products(df_sales)
    sales_by_product_line(df_sales)
    avg_price_vs_msrp(df_sales)
    top_customers_by_sales(df_sales)
    orders_count_per_customer(df_sales)
    sales_trend_over_time(df_sales)
    average_order_value(df_sales)
    most_common_status(df_sales)
    sales_by_deal_size(df_sales)
    top_cities_by_sales(df_sales)
    productline_sales_ratio(df_sales)
    repeat_order_customers(df_sales)
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETED")
    print("="*50)