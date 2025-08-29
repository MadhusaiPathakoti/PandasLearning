import pandas as pd

df = pd.read_excel("ecommerce_sales_data - duplicate.xlsx")
print(df)

# 1. Dropping Duplicate ROWS
# df.drop_duplicates(inplace=True)

# Drop duplicates based on specific subset of columnsd
df.drop_duplicates(subset=['order_date', 'customer_name'], keep='last')

# Keep the latest transaction if duplicates exist
df = df.sort_values(by='order_date').drop_duplicates(subset=['order_date', 'customer_name'], keep='last')

# Drop rows with same product & price but different order_ids
df = df.drop_duplicates(subset=['product', 'unit_price'], keep='first')

# 2. Dropping Duplicate COLUMNS
# Simulating duplicated columns
df['price_duplicate'] = df['unit_price']
df['category_dup'] = df['category']

# Drop fully duplicated columns
df = df.loc[:, ~df.T.duplicated()]

# Normalize column names to lowercase
df.columns = df.columns.str.lower()

df['Unit_Price'] = df['unit_price']
# Drop columns that differ only by case (price vs Price)
df = df.loc[:, ~df.columns.duplicated()]

# Drop columns with almost identical values (e.g., >90% match)
threshold = 0.9
to_drop = []
for i in range(len(df.columns)):
    for j in range(i + 1, len(df.columns)):
        col1, col2 = df.columns[i], df.columns[j]
        match_ratio = (df[col1] == df[col2]).sum() / len(df)
        if match_ratio > threshold:
            to_drop.append(col2)
df.drop(columns=set(to_drop), inplace=True)
