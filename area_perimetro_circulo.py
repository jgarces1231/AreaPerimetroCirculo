import math

# input
print("-----------------------------")
r = input("ingrese el valor del radio del circulo: ")
r = int(r) 

# processing 
a = math.pi*r*r
p = 2*math.pi*r 

# output
print("-----------------------------")
print("EL area es: " + str(a))
print("EL perimetro es: " + str(p))
print("-----------------------------")