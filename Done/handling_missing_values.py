import pandas as pd

df = pd.read_excel("ecommerce_sales_data - Copy.xlsx")
print(df)

#1. Detect Missing Values
print(df.isnull())

# Detect and count missing values
missing_counts = df.isnull().sum()
print(missing_counts)

# Show only columns with missing values
missing_columns = df.columns[df.isnull().any()]
print(missing_columns)

# Show rows with at least 3 missing values
print(df[df.isnull().sum(axis=1) >= 3])

#2. Fill Missing Values
# Fill missing quantity with 0
df['quantity'] = df['quantity'].fillna(0)

# Fill missing customer names with 'Unknown'
df['customer_name'] = df['customer_name'].fillna('Unknown')

# Fill missing total_price using unit_price * quantity if both are available
df['total_price'] = df['total_price'].fillna(df['unit_price'] * df['quantity'])

#3. Forward/Backward Fill

# Forward fill all columns
df.fillna(method='ffill', inplace=True)

# Backward fill only 'shipping_city'
df['shipping_city'] = df['shipping_city'].fillna(method='bfill')

# Forward fill followed by backward fill to ensure no gaps
df = df.fillna(method='ffill').fillna(method='bfill')


#4. Drop Missing Values
# Drop rows with any missing values
df_cleaned = df.dropna()


# Drop rows where unit_price or total_price is missing
df_cleaned = df.dropna(subset=['unit_price', 'total_price'])

# Drop columns with more than 50% missing values
df = df.loc[:, df.isnull().mean() < 0.5]

