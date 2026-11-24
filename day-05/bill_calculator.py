# Shopping bill calculator

item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

total = item1 + item2 + item3

discount_percentage = float(input("Enter discount percentage: "))

discount = total * discount_percentage / 100

final_amount = total - discount

print("\n----- SHOPPING BILL -----")
print(f"Original total: ₹{total:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final amount: ₹{final_amount:.2f}")