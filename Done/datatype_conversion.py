import pandas as pd
import numpy as np

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

# Using astype()
print(df.info())
print(df['quantity'].dtype)
df['quantity'] = df['quantity'].astype(str)
print(df['quantity'].dtype)
print(df.info())

#Multiple Columns
df[['quantity', 'unit_price']] = df[['quantity', 'unit_price']].astype({'quantity': float, 'unit_price': int})
print(df.info())

conversion_dict = {'quantity': int, 'unit_price': float}
df[['quantity', 'unit_price']] = df[['quantity', 'unit_price']].astype(conversion_dict)
print(df.info())

for col in df.columns:
    if df[col].dtype == 'float64':
        try:
            df[col] = df[col].astype(int)
        except ValueError:
            continue
print(df.info())

#Using pd.to_numeric()
print(df['quantity'].dtype)
df['quantity'] = df['quantity'].astype(str)
print(df['quantity'].dtype)
df['quantity'] = pd.to_numeric(df['quantity'])
print(df['quantity'].dtype)

print(df['order_date'].dtype)
df['order_date'] = df['order_date'].astype(str)
print(df['order_date'].dtype)
df['order_date'] = pd.to_datetime(df['order_date'])
print(df['order_date'].dtype)

