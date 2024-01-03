import os
import random
os.system("cls")

choice = 0
m = -1

while(m != choice):
    m = random.randrange(6)

    choice = int(input("Enter a number that you think its correct: "))
    while(choice < 0 or choice > 5):
        choice = int(input("Enter a number between 0 and 5: "))
        
    if choice == m:
        print("\nCongrats, you enter the same number!!")
    else:
        print("\nYou enter the wrong number. Try again!!")
        

