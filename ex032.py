import os
os.system("cls")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    greater = num1
    if num2 > num3:
        smaller = num3
    else:
        smaller = num2
else:
    if num2 > num1 and num2 > num3:
        greater = num2
        if num1 > num3:
          smaller = num3
        else:
           smaller = num1
    else:
        greater = num3
        if num1 > num2:
            smaller = num2
        else:
            smaller = num1
            
print(f"\nGreater: {greater} and Smaller: {smaller}")
    
