import pandas as pd

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

#Delete Columns – Approaches
#1. Using drop() with axis=1d
# Delete a single column
df.drop('payment_method', axis=1)
print(df)

# 2. In-place deletion
df.drop('payment_method', axis=1, inplace=True)
print(df)

# Drop multiple columns:
df = pd.read_excel("ecommerce_sales_data.xlsx")
df.drop(['payment_method', 'shipping_city'], axis=1)
print(df)

#Drop columns using list comprehension
# Drop all string-type columns
cols_to_drop = [col for col in df.columns if df[col].dtype == 'object']
df.drop(columns=cols_to_drop)
print(df)

#Drop columns based on condition (e.g., more than 50% NaN)
df.dropna(thresh=len(df)*0.5, axis=1)
print(df)

#Drop columns with zero variance
print(df.loc[:, df.nunique() != 1])


# Delete Rows – Approaches
#1.Drop by index
df.drop(index=0)
print(df)

#2. In-place:
df.drop(index=0, inplace=True)
print(df)

#Drop rows where a column equals a value
print(df[df['delivery_status'] != 'Pending'])

# Drop rows where a column is null
print(df.dropna(subset=['shipping_city']))

# Drop rows based on multiple conditions
print(df[~((df['quantity'] < 5) & (df['total_price'] > 3000))])

#Drop duplicate rows
df.drop_duplicates(subset=['customer_name', 'product'])
print(df)

#Drop rows using index from another condition:
indexes_to_drop = df[df['unit_price'] > 1000].index
df.drop(index=indexes_to_drop)