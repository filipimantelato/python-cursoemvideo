import os
from datetime import date
os.system("cls")

#year = date.today().year
year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")