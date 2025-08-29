import pandas as pd
import numpy as np

# How to Create a DataFrame
#1. From a dictionary of lists
data = {
 'name': ['Alice', 'Bob', 'Charlie'],
 'age': [25, 30, 22],
 'city': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)


#2. From a list of dictionaries
data = [
 {'name': 'Alice', 'age': 25, 'city': 'New York'},
 {'name': 'Bob', 'age': 30, 'city': 'London'}
]
df = pd.DataFrame(data)
print(df)


#3. From a list of lists + column names
a = [
 ['Alice', 25, 'New York'],
 ['Bob', 30, 'London']
]
df = pd.DataFrame(data, columns=['name', 'age', 'city'])
print(df)

#4. From a NumPy array
arr = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(arr, columns=['A', 'B'])
print(df)

#5. From Series objects
s1 = pd.Series([1, 2, 3], name='A')
s2 = pd.Series([4, 5, 6], name='B')
df = pd.concat([s1, s2], axis=1)
print(df)

# create a DataFrame from CSV and Excel files using Pandas
# 1. From a CSV File
# Syntax:
# df = pd.read_csv('your_file.csv')
df = pd.read_csv('../sales_data.csv')
# Optional parameters:
pd.read_csv('../sales_data.csv', delimiter=',') # Custom delimiter
pd.read_csv('../sales_data.csv', header=2) # Use second row as column names
pd.read_csv('../sales_data.csv', names=['Product', 'Category', 'Quantity']) # Custom column names
pd.read_csv('../sales_data.csv', index_col=0) # Set first column as index



# 2. From an Excel File
# Requires openpyxl or xlrd library installed.
# Tip: Install dependencies if needed
# pip install openpyxl # for .xlsx files
# Syntax:
# df = pd.read_excel('your_file.xlsx')
df = pd.read_excel('ecommerce_sales_data.xlsx')
pd.read_excel('ecommerce_sales_data.xlsx', sheet_name='Sheet1') # Read specific sheet
pd.read_excel('ecommerce_sales_data.xlsx', index_col=0) # Set index column
pd.read_excel('ecommerce_sales_data.xlsx', usecols="A:D") # Select specific columns
