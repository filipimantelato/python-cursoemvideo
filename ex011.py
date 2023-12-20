import os
os.system("cls")

price = float(input("Enter the price: "))
newPrice = price*0.95

print(f"\nOld price: ${price:.1f} \nNew price: ${newPrice:.1f}")