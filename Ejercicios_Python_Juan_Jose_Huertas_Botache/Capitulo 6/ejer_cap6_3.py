""" 
Escriba una función en Python que indique si un número es perfecto. Utilice una
función auxiliar que calcule los divisores propios (solución).
Entrada: 8128
Salida: True
""" 
def divisors(n):
    divisors_list = []
    for i in range(1, n):
        if n % i == 0:
            divisors_list.append(i)
    return divisors_list

def is_perfect(n):
    divisors_list = divisors(n)
    divisors_sum = sum(divisors_list)
    if divisors_sum == n:
        return True
    else:
        return False

print(is_perfect(int(input("Introduce a number to identify if it's perfect: "))))
