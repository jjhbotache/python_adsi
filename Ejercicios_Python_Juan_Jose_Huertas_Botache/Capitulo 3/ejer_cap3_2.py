""" 
2. Escriba un programa en Python que acepte el radio de una esfera y obtenga su volumen
(solución).
Entrada: 5
Salida: 523.3333333333334
"""

"""
this finds a volume of a circle
"""
#4/3 pi r^3
radious = int(input("insert the radious: "))
pi = 3.141592
print("Your circle volume is: ",((4/3)*(pi)*(radious**3)))