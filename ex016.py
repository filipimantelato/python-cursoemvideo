import os
import math
os.system("cls")

cath1 = float(input("Enter the first cathetus: "))
cath2 = float(input("Enter the second cathetus: "))

print(f"\nCathetus 1: {cath1} \nCathetus 2: {cath2} \nHypotenuse: {math.hypot(cath1, cath2):.2f}")