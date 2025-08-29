import pandas as pd

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

print(df.set_index('customer_name'))
print(df.set_index('customer_name', inplace=True))

print(df.reset_index())
print(df.reset_index(drop=True))
print(df.reset_index(inplace=True))
print(df.reset_index(drop=True, inplace=True))

print(df.set_index(['customer_name', 'product']))
print(df.reset_index(drop=True, inplace=True))
print(df.reset_index().drop(columns='index'))
print(df.reset_index().drop(columns='index', inplace=True))
print(df.reset_index(inplace=True).drop(columns='index'))