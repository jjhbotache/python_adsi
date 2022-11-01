""" 
3. Escriba un programa en Python que acepte un país (como «string») y muestre por
pantalla su bandera (como «emoji»). Puede restringirlo a un conjunto limitado de
países (solución).
Entrada: Italia
Salida: 􀀀􀀀
"""

""" from tkinter import *
root = Tk()
root.geometry("500x500")
root.resizable(False,False)
#root.config(bg="#000000")

frame = Frame(root).pack()
country = Entry(frame,borderwidth=2).place(relx = 0.5, rely = 0.5, anchor = CENTER)
canva = Canvas(frame, width=300, height=300).pack()
image = PhotoImage("C:/Users/jjhue/Pictures/Camera Roll/WIN_20221021_11_25_25_Pro.jpg")
image.create_image(height=40, width=40, img=image) 

root.mainloop() """

from tkinter import *
from PIL import ImageTk, Image

#this should open the img in a tk window
root=Tk()
img = ImageTk.PhotoImage("mydraw.png")
Label(root,image=img).pack()
root.mainloop()

""" 
I've couldn't make it
u cannot pring flags in the console
then I'm trying using tkinter to show it as an img
but cannot accept for some reason relative paths
"""




