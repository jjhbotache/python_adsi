"""
5. Escriba un programa en Python que acepte una palabra en castellano y calcule una
métrica que sea el número total de caracteres de la palabra multiplicado por el número
total de vocales que contiene la palabra (solución).
Entrada: ordenador
Salida: 36

"""


from tkinter import E


def get_vowels(word:str):
    """
    return the number of vowels that has a word

    Args:
        word (str): the word used to find the number of vowels
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    number_of_vowels = 0
    for letter in word:
        for vowel in vowels:
            if letter == vowel:number_of_vowels+=1;break    
    return number_of_vowels

word = input("Insert the word")
print(int(get_vowels(word))*len(word))

