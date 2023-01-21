"""
Escriba un programa en Python que acepte un diccionario y elimine los espacios de
sus claves respetando los valores correspondientes (solución).
Entrada: {"S 001": ["Math", "Science"], "S 002": ["Math", "English"]}
Salida: {"S001": ["Math", "Science"], "S002": ["Math", "English"]}
"""
dictionary = {"S 001": ["Math", "Science"], "S 002": ["Math", "English"]}


for key in list(dictionary.keys()):
    new_key=key.replace(" ", "")
    values=dictionary[key]
    
    dictionary.pop(key)
    
    dictionary[new_key]=values
    
print(dictionary)