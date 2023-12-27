from random import shuffle
import random
import os
os.system("cls")

numbers_norepeat = []
names_norepeat = []
numbers_norepeat = []
names = []

for i in range(4):
    input_names = input(f"Enter the {i+1}° name: ")
    names.append(input_names)


for i in range(5):
    while len(numbers_norepeat) < 4:
        r = (random.randint(1, 4))  
        if r not in numbers_norepeat:
            numbers_norepeat.append(r)

    while len(names_norepeat) < 4:
        n = (random.choice(names))
        if n not in names_norepeat:
            names_norepeat.append(n)

print("\n\n-Sequence-\n")

for i in range(4):
    print(f"{numbers_norepeat[i]}- {names_norepeat[i]}")
    
    
#Jeito mais prático sem numeração, sem cuidar da repeticao, etc..

#n1 = str(input("Enter first name: "))
#n2 = str(input("Enter second name: "))
#n3 = str(input("Enter third name: "))
#n4 = str(input("Enter forth name: "))

#names = [n1, n2, n3, n4]
#shuffle(names)
#print(names)
    
