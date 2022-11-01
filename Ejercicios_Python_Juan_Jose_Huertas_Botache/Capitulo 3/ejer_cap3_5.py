"""
5. Escriba un programa en Python que calcule la distancia euclídea entre dos puntos
(𝑥1, 𝑦1) y (𝑥2, 𝑦2) (solución).
Entrada: (𝑥1 = 3, 𝑦1 = 5); (𝑥2 = −7, 𝑦2 = −4)
Salida: 13.45362404707371
"""
import math


# d=r( (x2-x1)^2 (y2-y1)^2 )
x1=int(input("insert X1 : "))
x2=int(input("insert X2 : "))
y1=int(input("insert y1 : "))
y2=int(input("insert y2 : "))

print(math.sqrt( ((x2-x1)**2)+((y2-y1)**2) ))


