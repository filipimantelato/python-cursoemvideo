import os
os.system("cls")

phrase = str(input("Enter a frase: ")).upper().strip()

print("")
a_amount = phrase.count("A")
print("A amount: ", a_amount)

a_index = phrase.find("A")
print("A position: ", a_index)

a_lastindex = phrase.rfind("A")
print("Last A position: ", a_lastindex)

