""" 
4. Escriba un programa en Python que acepte 3 códigos de teclas y muestre por pantalla
la acción que se lleva a cabo en sistemas Ubuntu Linux (solución).
Entrada: tecla1=Ctrl; tecla2=Alt; tecla3=Del;
Salida: Log out

""" 
import keyboard  # using module keyboard


shortcuts = {}
with open("C:/Users/jjhue/Documents/python/Ejercicios_Python_Juan_Jose_Huertas_Botache/Capitulo 4/DB/linux_shortcuts.txt") as f:
    #from de txt file, get and organize the information of the linux shortcuts 
    data_list=f.readlines()
    for line in range(0, len(data_list)-1, 2):
        shortcuts[data_list[line].strip().replace(" ","").lower()]=data_list[line+1].strip()
    # print(shortcuts)
    
# wait for a hotkey
hotkey_introduced = str(keyboard.read_hotkey())#;print(hotkey_introduced)
if "+mayusculas" in hotkey_introduced:
    hotkey_introduced = hotkey_introduced.replace("+mayusculas", "")#;print(hotkey_introduced)
    hotkey_introduced = hotkey_introduced[:-2] + "+shift" + hotkey_introduced[-2:]
    hotkey_introduced = hotkey_introduced.lower()
print(hotkey_introduced)


# if it exists, says what it does, or says that it doesn't exists
if hotkey_introduced.lower() in [s.lower() for s in shortcuts.keys()]:
    print(f"The {hotkey_introduced} in linux has this functions: \n{shortcuts[hotkey_introduced]}")
else:
    print(f"The {hotkey_introduced} in linux hasn't function")
    # print(f"{hotkey_introduced} != {shortcuts.keys()}")