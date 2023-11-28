item_prices = []
for i in range(3):
    price = float(input(f"Enter the price of item {i+1}: "))
    item_prices.append(price)
quantities = []
for i in range(3):
    quantity = int(input(f"Enter the quantity of item {i+1}: "))
    quantities.append(quantity)
discount_rate = float(input("Enter the discount rate (%): "))
tax_rate = float(input("Enter the tax rate (%): "))
subtotal = sum(price * quantity for price, quantity in zip(item_prices, quantities))
discount = (discount_rate / 100) * subtotal

total_after_discount = subtotal - discount

tax = (tax_rate / 100) * total_after_discount

final_total_inr = total_after_discount + tax
print(f"The total cost including discounts and taxes is: ₹{final_total_inr:.2f}")
