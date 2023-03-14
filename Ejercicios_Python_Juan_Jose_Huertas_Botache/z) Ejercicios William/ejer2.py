from random import randint
from os import system

# nombre/puntajeTotal/puntajeActual
jugador1=["",0,0]
jugador2=["",0,0]

jugador1[0] = input("Cual es el nombre del jugador 1 ")
jugador2[0] = input("Cual es el nombre del jugador 2 ")


puntos_para_ganar = int(input("introduzca los puntos para ganar: "))
while puntos_para_ganar < 50:
  print("El puntaje no puede ser menor a 50")
  puntos_para_ganar = int(input("introduzca un valor mayor a 50: "))

# variable global
total = 0

def turno():
  global total
  input("\n Presiona para jugar un turno...")
  system("cls")
  print("Se juega un turno")
  # tiro los dados (eleccion aleatoria del 1-6
  jugador1[2] = randint(1,6)
  jugador2[2] = randint(1,6)
  
  print(f"El jugador {jugador1[0]} saco: {jugador1[2]}")
  print(f"El jugador {jugador2[0]} saco: {jugador2[2]}")
  
  # sumo los puntos de cada tirada de dados
  total += jugador1[2] + jugador2[2]
  
  # decido quien gana los puntos
  if jugador1[2] > jugador2[2]: 
    print("Jugador 1 gano")
    jugador1[1]+= total
    total = 0
  elif jugador1[2] < jugador2[2] :
    print("Jugador 2 gano")
    jugador2[1]+= total
    total = 0
  print(f"El jugador 1 tiene: {jugador1[1]} puntos")  
  print(f"El jugador 2 tiene: {jugador2[1]} puntos")  
  
#MIENTRAS     ptns de pntaje total sean menores...
while         (jugador1[1] < puntos_para_ganar) and (jugador2[1] < puntos_para_ganar):
  turno()
  
  
if jugador1[1] > jugador2[1]:
  print(f"{jugador1[0]} ha ganado la partida")
else:
  print(f"{jugador2[0]} ha ganado la partida")
