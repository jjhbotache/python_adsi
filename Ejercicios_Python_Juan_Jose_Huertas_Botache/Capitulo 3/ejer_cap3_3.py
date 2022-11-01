""" Escriba un programa en Python que acepte la base y la altura de un triángulo y
    compute su área 
 """

""" 
FORMULA : BASE X HEIGHT / 2
"""

""" Base input """
base = float(input("Enter the base of your triangle: "))
""" Height input """
height = float(input("Enter the height of your triangle: "))

""" Procedure """

result = int((base * height)/2) 

""" Print the area """

print("The area of your triangle is: " , result)
