"""
Escriba un programa en Python que acepte una lista de palabras y las agrupe por su
letra inicial usando un diccionario (solución).
Entrada: [ “mesa”, “móvil”, “barco”, “coche”, “avión”, “bandeja”, “casa”,
“monitor”, “carretera”, “arco”]
Salida: {“m”: [“mesa”, “móvil”, “monitor”], “b”: [“barco”, “bandeja”], “c”:
[“coche”, “casa”, “carretera”], “a”: [“avión”, “arco”]}
"""

entry=[]
for time in range(6):
    entry.append(input(f"Introduce your entry {time} "))

dictionary = {}
print(dictionary)
for word in entry:
    if word[0] in dictionary:
        dictionary[word[0]].append(word)
    else:
        dictionary[word[0]]=[word]
print(dictionary)