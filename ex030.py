import os
os.system("cls")

distance = int(input("Enter the distance of a trip: "))

if distance < 201: 
    value = distance * 0.5
    print("$",value)
else:
    value = distance * 0.45
    print("$",value)