"""
1. Escriba un programa en Python que acepte el nombre y los apellidos de una persona
y los imprima en orden inverso separados por una coma. Utilice f-strings para
implementarlo (solución).
Entrada: nombre=Sergio; apellidos=Delgado Quintero
Salida: Delgado Quintero, Sergio
"""

name = input("Name: ")
lastname = input("Lastname: ")
print(f"{lastname}, {name}")
