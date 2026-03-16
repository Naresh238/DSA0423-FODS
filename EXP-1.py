prices = [50, 30, 20]
quantities = [2, 3, 1]

discount_rate = 10
tax_rate = 5

subtotal = 0
for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

discount = subtotal * discount_rate / 100
tax = (subtotal - discount) * tax_rate / 100

total_cost = subtotal - discount + tax

print("Total Cost:", total_cost)
