import random
import os
os.system("cls")

n1 = str(input("Enter first name: "))
n2 = str(input("Enter second name: "))
n3 = str(input("Enter third name: "))
n4 = str(input("Enter forth name: "))

names = [n1, n2, n3, n4]
print("\n",random.choice(names))