original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
print("Original Price\tDiscount\tNew Price")

for price in original_prices:
    discount = price * (60 / 100)
    new_price = price - discount
    print(f"${price:.2f}\t\t${discount:.2f}\t\t${new_price:.2f}")