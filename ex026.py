import os
os.system("cls")

name = str(input("Enter a name: "))

name2 = name.split()
length = len(name2)

print("")
print("First name: ", name2[0])
print("Last name: ", name2[length - 1])