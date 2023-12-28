import os
os.system("cls")

city = str(input("Enter a city: ")).upper()
index = city.find("SANTO")

print("")
if index == 0:
    print("The city's name starts with Santo")
else:
    print("The city's name don't starts with Santo")
