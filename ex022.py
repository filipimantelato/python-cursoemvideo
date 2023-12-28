import os
os.system("cls")

num = str(input("Enter a number: "))
while(len(num) < 1 or len(num) > 4):
    num = str(input("Type a right number: "))
    
num2 = num.split()

print("")
if len(num) == 4:
    print(f"Milhar: {num[0]}")
    print(f"Centena: {num[1]}")
    print(f"Dezena: {num[2]}")
    print(f"Unidade: {num[3]}")
else:
    if len(num) == 3: 
        print(f"Centena: {num[0]}")
        print(f"Dezena: {num[1]}")
        print(f"Unidade: {num[2]}")
    else:
        if len(num) == 2: 
            print(f"Dezena: {num[0]}")
            print(f"Unidade: {num[1]}")    
        else:
            print(f"Unidade: {num[0]}") 

    
