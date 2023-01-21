"""
Escriba un programa en Python que acepte un diccionario cuyos valores son listas y
borre el contenido de dichas listas (solución).
Entrada: {"C1": [10, 20, 30], "C2": [20, 30, 40], "C3": [12, 34]}
Salida: {"C1": [], "C2": [], "C3": []}
"""
dictionary={"C1": [10, 20, 30], "C2": [20, 30, 40], "C3": [12, 34]}

for key in dictionary.keys():
    dictionary[key]=[]
print(dictionary)