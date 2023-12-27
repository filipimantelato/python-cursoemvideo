import os
from math import radians, sin, cos, tan
os.system("cls")

angle = float(input("Enter an angle: "))

sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))

print(f"\nCos {angle}°: {cos:.2f} \nSin {angle}°: {sin:.2f} \nTan {angle}°: {tan:.2f}")