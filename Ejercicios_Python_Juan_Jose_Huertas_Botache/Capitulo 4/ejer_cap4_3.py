""" 
3. Escriba un programa en Python que acepte un país (como «string») y muestre por
pantalla su bandera (como «emoji»). Puede restringirlo a un conjunto limitado de
países (solución).
Entrada: Italia
Salida: 􀀀􀀀

------------------------------------------------

Flag emojies aren't avaliable for all the fonts in all the OS. 
That's why, I'm using simple emojies instead of using flag emojies.
""" 

import emoji

animals = {
    "cat": ":grinning_cat:",
    "dog": ":dog_face:",
    "monkey": ":monkey_face:",
    "lion": ":lion:",
    "tiger": ":tiger_face:",
    "pig": ":pig_face:",
    "mouse": ":mouse_face:",
    "frog": ":frog:"
}

print("""Animales disponibles: """)
for key in animals.keys():print(key)

animal = input("Ingresa el nombre de un animal: ")

if animal in animals:print(emoji.emojize(animals[animal]))
else:print("Lo siento, ese animal no esta en la lista")