#program liczący deltę
import math

b = float(input("Podaj wartość b: "))
a = float(input("Podaj wartość a: "))
c = float(input("Podaj wartość c: "))

delta = b**2 - 4*a*c

print("Delta wynosi:", delta)

delta = b**2 - 4*a*c

def delta():
        if delta < 0:
            return[0]
        elif delta == 0:
            x = -b /2*a
            return[x]
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return[x1,x2]



