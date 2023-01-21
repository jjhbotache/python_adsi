"""
Escriba un programa en Python que acepte una lista de valores numéricos y obtenga
su valor máximo sin utilizar la función «built-in» max() (solución).
Entrada: [6, 3, 9, 2, 10, 31, 15, 7]
Salida: 2
"""
numbers = []
max=0
for number in range(10):
    numbers.append(int(input("Introduce your number: ")))
    try:
        if numbers[-1]>max:max=numbers[-1]
    except:
        pass
    

print(f"The higher number is: {max}")