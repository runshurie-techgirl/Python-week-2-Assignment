price = input("Enter the price of one chapati (KES): ")
quantity = input("How many chapati do you want? ")

price = float(price)
quantity = int(quantity)

total = price * quantity

print(f"{quantity} chapati at {price:.2f} each = {total:.2f} KES")
