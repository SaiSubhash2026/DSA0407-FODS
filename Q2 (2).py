import pandas as pd
data = {
    'Customer ID': [1, 2, 1, 3, 2],
    'Order Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Product Name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'Order Quantity': [5, 3, 2, 1, 4]
}
order_data = pd.DataFrame(data)

orders_per_customer = order_data.groupby('Customer ID').size()

average_quantity_per_product = order_data.groupby('Product Name')['Order Quantity'].mean()

earliest_order_date = order_data['Order Date'].min()
latest_order_date = order_data['Order Date'].max()
print("Total number of orders made by each customer:")
print(orders_per_customer)
print("\nAverage order quantity for each product:")
print(average_quantity_per_product)
print(f"\nEarliest order date: {earliest_order_date}")
print(f"Latest order date: {latest_order_date}")
