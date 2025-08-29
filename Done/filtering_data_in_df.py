import pandas as pd

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

#Boolean Indexing
#Boolean indexing means filtering rows based on True/False conditions.
#You write a condition, and Pandas returns the rows where the condition is True .

#FILTERING DATA
#Simple Condition
#Syntax: df[df['col'] operator value]
#Filter rows unit price less than 300
print(df[df['unit_price'] < 300])

# Filter rows where product is 'Laptop'
print(df[df['product'] == 'Laptop'])

#Filter the orders of the year 2024
print(df[df['order_date'].dt.year == 2024])


#Value List
#Syntax: df[df['col'].isin([...])]
# Filtering with isin()
#Filter rows where city is either London or Paris
print(df[df['payment_method'].isin(['PayPal', 'Net Banking'])])

#Multiple Conditions
# Syntax: df[(cond1) & (cond2)]
#Filter rows where Age > 25 AND score > 80
print(df[(df['category'] == 'Accessories') & (df['quantity'] <=2)])
print(df[(df['payment_method'] == 'Net Banking') & (df['delivery_status'] == 'Cancelled') & (df['unit_price'] < 500)])

# OR Condition
# Syntax: df[(cond1) | (cond2)]
#Filter rows where Age < 30 OR city is 'London'
print(df[(df['delivery_status'] == 'Cancelled') | (df['shipping_city'].isin(['Port Roy', 'Michaelburgh', 'New Diane']))])

#NOT Condition
#Syntax: df[~(cond)]
# Filtering with ~ (NOT)
#Exclude rows where city is 'London'
print(df[~(df['product'] == 'Laptop')])


#String Condition
# Syntax: df[df['col'].str.startswith('substring')]
#String filtering with .str
#Names that start with 'A'
print(df[df['customer_name'].str.startswith('A')])

#Names that contain 'a' (case-insensitive)
# Syntax: df[df['col'].str.contains('substring')]
print(df[df['customer_name'].str.contains('a', case=False)])

#Range Condition
#Syntax: df[df['col'].between(a, b)]
#Between two values
#Filter rows where Score between 80 and 90
print(df[df['unit_price'].between(300, 400)])

# Filter and select specific columns
# Show names and scores of people from Paris
print(df[df['product'] == 'Laptop'][['customer_name', 'quantity']])

#Get the total_price for rows where category =='Electronics'
print(df.loc[df['category'] == 'Gadgets', 'customer_name'])

#: Get customer_name where delivery_status == 'Pending' and quantity > 2
print(df.loc[(df['delivery_status'] == 'Pending') & (df['quantity'] > 2), 'customer_name'])


#Combine Filtering Approaches
# Example combining AND, OR, and String
print(
        df[
            (df['category'] == 'Electronics') &
            (df['product'].str.contains('Lap', case=False)) |
            (df['total_price'] > 4000)
        ]
)