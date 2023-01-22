""" 
Escriba una función en Python que determine si una cadena de texto es un palíndromo
(solución).
Entrada: ana lava lana
Salida: True

""" 
def is_palindrome(string):
    return string.replace(" ","") == string[::-1].replace(" ","")

print(is_palindrome(input("Introduce a string to identify if it's a palindrome: ")))