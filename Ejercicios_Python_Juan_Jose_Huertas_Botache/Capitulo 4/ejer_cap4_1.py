""" 
3. Escriba un programa en Python que acepte un país (como «string») y muestre por
pantalla su bandera (como «emoji»). Puede restringirlo a un conjunto limitado de
países (solución).
Entrada: Italia
Salida: 􀀀􀀀
"""

from tkinter import *
from PIL import ImageTk, Image
#--------------------------------------------------------------------------------------
def logic():
    global country
    print(country);
#--------------------------------------------------------------------------------------
root = Tk()
root.geometry("700x700");

country = Entry(root,borderwidth=2).pack(side=TOP)
enter = Button(root,text="search",command=logic()).pack(padx=50,pady=10)

image1 = Image.open("Capitulo 4/flags/brazil.png") 
test = ImageTk.PhotoImage(image1)
label1 = Label(root,image=test,).pack(padx=150,pady=150)
root.mainloop()


""" 
I've couldn't make it
u cannot pring flags in the console
then I'm trying using tkinter to show it as an img
but cannot accept for some reason relative paths
"""




