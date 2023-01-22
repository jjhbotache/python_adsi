"""
Escriba un programa en Python que acepte una lista de listas representando una matriz
numérica y compute la suma de los elementos de la diagonal principal (solución).
Entrada: [[4, 6, 1], [2, 9, 3], [1, 7, 7]]
Salida: 20
"""
entry=[[4, 6, 1], [2, 9, 3], [1, 7, 7]]
accumulated = 0
for number in range(len(entry)):
    accumulated+=entry[number][number]  
print(f"The total is: {accumulated}") 