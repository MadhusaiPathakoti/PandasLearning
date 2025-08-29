import pandas as pd

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

# 1. [] - Column Access (Easiest)
#  Access a single column:
print(df['product'])

# Access multiple columns:
print(df[['product', 'quantity']])

#Projections
columns_required = ['product', 'quantity']
print(df[columns_required])

# 2. .loc[] - Label-based access (Flexible and powerful)
#  Access a row by index label:
print(df.loc[0])
# Access a specific value:
print(df.loc[0, 'product'])
# Access multiple rows and columns:
print(df.loc[0:2, ['product', 'quantity']])

# 3. .iloc[] - Position-based access (Fast)
#  Access row by position:
print(df.iloc[0])
# Access a specific cell:
print(df.iloc[0, 5])   # 6th column (zero-based)
# Slice rows and columns:
print(df.iloc[0:3, 4:7])

# 4. .at[] - Fast access for single value by label
# One row, one column by label (like .loc, but faster):
print(df.at[0, 'customer_name'])

# 5. .iat[] - Fast access for single value by position
# One row, one column by integer index:
print(df.iat[0, 1])

# From Easy to Advanced Queries:
#  Easy: Get all product values
print(df['product'])

# Medium: Get the total_price for rows where category == 'Electronics'
print(df.loc[df['category'] == 'Electronics', 'total_price'])
# Hard: Get customer_name where delivery_status == 'Pending' and quantity > 2
print(df.loc[(df['delivery_status'] == 'Pending') & (df['quantity'] > 2), 'customer_name'])