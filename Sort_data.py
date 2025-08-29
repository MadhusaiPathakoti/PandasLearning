import pandas as pd

# Load dataset
df = pd.read_excel("ecommerce_sales_data.xlsx")

print("Original Data Snapshot:")
print(df.loc[0].to_dict())

# 1. Sort by a single column (Order Date ascending)
df_sorted_date = df.sort_values(by='order_date', ascending=True)

# 2. Sort by multiple columns (Category ascending, Total Price descending)
df_sorted_cat_price = df.sort_values(by=['category', 'total_price'],
                                     ascending=[True, False])

# 3. Sort by Customer Name alphabetically, then by Order Date latest first
df_sorted_customer_date = df.sort_values(by=['customer_name', 'order_date'],
                                         ascending=[True, False])

# 4. Sort by Quantity (highest first)
df_sorted_quantity = df.sort_values(by='quantity', ascending=False)

# 5. Sort by Payment Method then Total Price
df_sorted_payment = df.sort_values(by=['payment_method', 'total_price'],
                                   ascending=[True, True])

# 6. Custom Sorting: sort by Delivery Status in defined order
delivery_order = {"Pending": 0, "Shipped": 1, "Delivered": 2, "Cancelled": 3}
df['delivery_sort'] = df['delivery_status'].map(delivery_order)
df_sorted_delivery = df.sort_values(by=['delivery_sort', 'order_date']).drop(columns='delivery_sort')

# 7. Sort by City name length, then alphabetically
df['city_len'] = df['shipping_city'].str.len()
df_sorted_city = df.sort_values(by=['city_len', 'shipping_city']).drop(columns='city_len')

# 8. Sort by Unit Price rounded to nearest hundred
df['unit_price_rounded'] = (df['unit_price'] / 100).round() * 100
df_sorted_price_band = df.sort_values(by=['unit_price_rounded', 'unit_price']).drop(columns='unit_price_rounded')

# Sort by length of customer_name
df.sort_values(by=df['customer_name'].apply(len))

# Sort by last word in customer name
df.sort_values(by=df['customer_name'].apply(lambda x: x.split()[-1]))

# Sort using lambda and assign
df.assign(city_length=df['shipping_city'].apply(len)).sort_values('city_length')
