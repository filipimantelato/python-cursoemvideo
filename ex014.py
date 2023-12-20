import os
os.system("cls")

days = int(input("Enter the days: "))
km = float(input("Enter the kilometers(km/h): "))

priceDay = days * 60
priceKm = km * 0.15
total = priceDay + priceKm

print(f"\nTotal: ${total:.2f}")
