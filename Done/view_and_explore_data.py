import pandas as pd

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

#1. head() – View Top Rows
print(df.head()) #Default: Top 5 rows
print(df.head(10)) #Top 10 rows

#2. tail() – View Bottom Rows
print(df.tail()) # Default: last 5 rows
print(df.tail(3)) # Last 3 rows

#3. info() – Data Summary
print(df.info())

#4. shape – Dimensions of Data
print(df.shape)

#5. dtypes – Column Data Types
print(df.dtypes)

#6. describe() – Statistical Summary
print(df.describe())
print(df.describe(include='all')) # Includes object (string) columns too
