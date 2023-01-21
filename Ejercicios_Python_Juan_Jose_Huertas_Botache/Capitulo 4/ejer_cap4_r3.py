""" 
3. Escriba un programa en Python que acepte un número entero 𝑛 y realice el siguiente
cálculo de productos sucesivos (solución):
Π︁𝑛
𝑖=1
𝑥2
𝑖
= 𝑥20
・ 𝑥21
・ 𝑥22
・ ・ ・ ・ ・ 𝑥2
𝑛
""" 


#The exercise is weird & I can't prove that my answer is right
""" 
no_gotten=True
while no_gotten:
    try:
        x=int(input("Introduce an integrer int for x: "))
        n=int(input("Introduce an integrer int for n: "))
        no_gotten=False
    except:
        print('An int entry please!')
    
result = 0
for time in range(n):
    if time==1:result+=(x**2)
    else:result*=(x**2)
print(result)
 """
 
 
n = int(input("Introduce an integrer int for n: "))
print("The result is: ")
 
resultado = 1
for i in range(1, n+1):
    resultado *= i
print(resultado)

