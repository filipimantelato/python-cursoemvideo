import os
os.system("cls")

wage = float(input("Enter the wage: "))

if wage > 1250.00: 
    new_wage = wage * 1.10
else:
    new_wage = wage * 1.15
    
print(f"New wage: {new_wage}")