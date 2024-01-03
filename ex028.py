import os
os.system("cls")

kilometers = int(input("Enter the km/h: "))

if kilometers > 80: 
    print(f"You were fined. The value is: ${(kilometers-80)*7:.2f}")
