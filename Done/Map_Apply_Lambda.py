import pandas as pd
import numpy as np

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

# .map() Examples
# Works only on a Series (single column).
# Capitalize all shipping city names
df['shipping_city'] = df['shipping_city'].map(lambda x: x.upper())

# Tag expensive orders (unit_price > 1000)
df['expensive'] = df['unit_price'].map(lambda x: 'Yes' if x > 1000 else 'No')

# Map delivery_status to numeric codes
status_map = {'Pending': 0, 'Shipped': 1, 'Delivered': 2}
df['status_code'] = df['delivery_status'].map(status_map)

df['status_code'] = df['delivery_status'].map(status_map).fillna(-1)

# .apply() Examples
# Works on a Series OR DataFrame
# On Series: behaves like map().
# On DataFrame: applies function along rows/columns.

# Length of customer name
df['name_length'] = df['customer_name'].apply(len)

# Calculate total_price manually using quantity * unit_price
df['calc_price'] = df.apply(lambda row: row['quantity'] * row['unit_price'], axis=1)

df = pd.read_excel("ecommerce_sales_data.xlsx")
df['status_code'] = df.apply(lambda x:status_map.get(x['delivery_status'], -1) ,axis=1)

# Check if order was placed on a weekend
df['is_weekend'] = df['order_date'].apply(lambda x: x.weekday() >= 5)

# Combined .map() , .apply() , and lambda
# Create a tag for premium customers: total_price > 4000 and payment via Net Banking
df['premium_tag'] = df.apply(lambda row: 'Premium' if row['total_price'] > 4000 and row['payment_method'] == 'Net Banking'
else 'Regular', axis=1)

# Normalize price per item, then bucket into 'Low', 'Medium', 'High'
def price_bucket(x):
    if x < 500:
        return 'Low'
    elif x < 1500:
        return 'Medium'
    else:
        return 'High'
    
df['price_bucket'] = df['unit_price'].apply(price_bucket)

# applymap()
# Works elementwise on an entire DataFrame (only on DataFrames).d
# Convert everything to string type (just an example)
df_str = df[["quantity", "unit_price"]].applymap(lambda x: str(x))

