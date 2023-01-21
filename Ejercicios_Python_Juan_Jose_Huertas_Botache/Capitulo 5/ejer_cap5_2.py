"""
2. Escriba un programa en Python que acepte una lista y elimine sus elementos duplicados
(solución).
Entrada: [“this”, “is”, “a”, “real”, “real”, “real”, “story”]
Salida: [“this”, “is”, “a”, “real”, “story”]
"""
entry=[]
for time in range(6):
    entry.append(input(f"Introduce your entry {time} "))
    
print(set(entry))