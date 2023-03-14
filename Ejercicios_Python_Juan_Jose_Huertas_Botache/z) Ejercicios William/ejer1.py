import os
import random
print("Juguemos a adivinar un numero del 1 al 100")
numero_buscado = random.randint(1, 100)
intentos = int(input("¿Cuántos intentos quieres tener para adivinar el número? "))
print("~"*50)
for vez in range(1, intentos + 1):
    intento = int(input(f"Intento número {vez}: ¿Qué número crees que es? "))
    if intento == numero_buscado:
        print(f"¡Adivinaste el número en {vez} intentos!")
        break
    elif intento < numero_buscado:
        print(f"El número buscado es mayor que {intento}")
    else:
        print(f"El número buscado es menor que {intento}")

print("El número buscado era: ", numero_buscado)
