import pandas as pd
import re

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

#1. Column Conversions
print(df.columns)
print(df.columns.tolist())
print(list(df.columns))


#Convert to Uppercase
df.columns = df.columns.str.upper()
print(list(df.columns))

#Convert to Lowercase
df.columns = df.columns.str.lower()
print(list(df.columns))


#Convert to Title Case
# Title Case: Each word capitalized
df.columns = df.columns.str.title()
print(list(df.columns))

#Convert to Capitalize First Letter
# Capitalize only the first letter of each column
df.columns = df.columns.str.capitalize()
print(list(df.columns))

#Convert to Snake Case (e.g., 'Customer Name' → 'customer_name')
def to_snake_case(s):
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s) # Handle CamelCase
    s = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s) # Handle transition like "HTMLParser"
    return s.replace(" ", "_").lower()

df.columns = [to_snake_case(col) for col in df.columns]
print(list(df.columns))

#2. Rename Columns
#Rename a Single Column
# Rename one column
df.rename(columns={'customer_name': 'customer name'}, inplace=True)
print(list(df.columns))

#Rename Multiple Columns with a Dictionary
df.rename(columns={
                    'order_date': 'date_of_order',
                    'payment_method': 'pay_mode',
                    'shipping_city': 'city'
                  },
        inplace=True)
print(list(df.columns))

#You can use predefined dictionary to rename columns
columns_renaming_dictionary = {
                    'date_of_order': 'order_date',
                    'pay_mode': 'payment_method',
                    'city': 'shipping_city'
                  }
df.rename(columns=columns_renaming_dictionary, inplace=True)
print(list(df.columns))


# Dynamic Renaming (e.g., remove 'status', add 'col_', etc.)
# Add 'col_' prefix to each column
df.columns = ['col_' + col for col in df.columns]
print(list(df.columns))

# Or remove specific substring like 'status' from column names
df.columns = [col.replace('col_', '') for col in df.columns]
print(list(df.columns))
