import pandas as pd

df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df)

# 1. Lower / Upper / Capitalize
df['customer_name'] = df['customer_name'].str.upper()

# Converts "Brandy Murray" → "BRANDY MURRAY"
df['shipping_city'] = df['shipping_city'].str.capitalize()

# Makes "Laptop" → "Laptop" (already capitalized, but good for consistency)
df['product'] = df['product'].str.title().str.replace('Laptop', '💻 Laptop')

# 2. Contains

# Checks if 'Net' is in "Net Banking" → True
temp = df[df['payment_method'].str.contains('Net')]

# Regex for exact word match ( Murray only)
murray = df[df['customer_name'].str.contains(r'\bMURRAY\b')]
df = pd.read_excel("ecommerce_sales_data.xlsx")

# Filters rows with full names in "Firstname Lastname" format
df[df['customer_name'].str.contains(r'^[A-Z][a-z]+ [A-Z][a-z]+$')]

# 3. StartsWith / EndsWith
# "Port Roy" → True
df[df['shipping_city'].str.startswith('Port')]

# "Net Banking" → True
df[df['payment_method'].str.endswith('Banking')]

# Multiple .str filters combined with conditions
df[df['customer_name'].str.startswith('B') & df['shipping_city'].str.endswith('Roy')]

# 4. Replace Text
# ✅ "Laptop" → "Notebook"
df['product'].str.replace('Laptop', 'Notebook', regex=False)

# "Brandy Murray" → "Brandy Smith"
df['customer_name'].str.replace(r'\bMurray\b', 'Smith', regex=True)

# "Net Banking" → "Net_Banking"
df['modified_payment'] = df['payment_method'].str.replace(r'\s+', '_', regex=True)

# 5. String Length
# "Laptop" → 6
df['length'] = df['product'].str.len()

# "Port Roy" → 10 → True
df[df['shipping_city'].str.len() > 10]

# Filters rows where name is longer than city
df[df['customer_name'].str.len() > df['shipping_city'].str.len()]


# 6. Split Strings
# ✅ "Brandy Murray" → "Brandy"
df['customer_name'].str.split().str[0]

# "Net Banking" → "Banking"
df['payment_method'].str.split().str[-1]

# "Brandy Murray" → "BM"(Initials)
df['initials'] = df['customer_name'].str.split().apply(lambda x: x[0][0] + x[1][0] if len(x) > 1 else '')

# 7. Extract using Regex
# Gets "Brandy"
df['customer_name'].str.extract(r'(\w+)\s')

# Extracts payment mode keywords
df['payment_method'].str.extract(r'(Net|Card)')

# Extracts initials using groups: "Brandy Murray" → B , M
df['customer_name'].str.extract(r'^([A-Z])[a-z]+\s([A-Z])[a-z]+$')

# 8. Strip Whitespace
#  Removes leading/trailing spaces
df['shipping_city'].str.strip()


# Combines strip() and upper()
df['customer_name'].str.strip().str.upper()

# Strips and removes extra inner spaces (if any)
df['customer_name'].apply(lambda x: ' '.join(x.strip().split()))

# 🧠 Bonus Tip:
# Combine multiple .str methods like chaining:
#
# "Brandy Murray" → "brandy_murray"
df['customer_name'].str.strip().str.lower().str.replace(' ', '_')
