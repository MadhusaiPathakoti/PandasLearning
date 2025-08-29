import pandas as pd

# Load dataset
df = pd.read_excel("ecommerce_sales_data.xlsx")

# 1. Using groupby()
# Get total quantity ordered per category
df.groupby('category')['quantity'].sum()

# Get average unit price per product and payment method
df.groupby(['product', 'payment_method'])['unit_price'].mean()

# For each city and category, get total orders, total revenue, and average quantity per
# order
df.groupby(['shipping_city', 'category']).agg(
total_orders=('product', 'count'),
total_revenue=('total_price', 'sum'),
avg_quantity=('quantity', 'mean')
)

# 2. Using pivot_table()
# Useful when you want a matrix-style summary with automatic aggregation.
# Total quantity by payment method and category
df.pivot_table(values='quantity', index='payment_method', columns='category', aggfunc='sum')

# Average unit price by product across cities
df.pivot_table(values='unit_price', index='shipping_city', columns='product', aggfunc='mean')

# Create a 3D pivot (multi-index) table of total revenue by city, payment method, and
# product
df.pivot_table(
values='total_price',
index=['shipping_city', 'payment_method'],
columns='product',
aggfunc='sum',
fill_value=0
)

# 3. Using agg() without groupby
# Get sum of quantity and total price for entire DataFrame
df.agg({'quantity': 'sum', 'total_price': 'sum'})

# Get multiple aggregations for unit_price and quantity
df.agg({
'unit_price': ['min', 'max', 'mean'],
'quantity': ['sum', 'mean']
})

# Apply custom lambda to calculate weighted average unit price
weighted_avg = (df['unit_price'] * df['quantity']).sum() / df['quantity'].sum()

# 4. Using apply() on groupby
# Gives more flexibility with row-wise logic inside groups.
# Get total revenue per customer
df.groupby('customer_name')['total_price'].sum()

# Get top-spending product per city
df.groupby('shipping_city').apply(lambda g: g.loc[g['total_price'].idxmax()][['product', 'total_price']])

# Within each category, get revenue percent share of each product
def product_share(g):
    total = g['total_price'].sum()
    g['revenue_share'] = g['total_price'] / total * 100
    return g
df.groupby('category').apply(product_share)
