# ganador por cada etapa
# ganador de la vuelta

# son 4 etapas
from random import randint

# lista de ciclistas
ciclistas = [
  "marcos",
  "pablo",
  "david",
  "aldemar"
  ]
print(f"hay los siguientes ciclistas:\n {ciclistas}")
# lsita de 4 etapas por ciclista (todos valen 0)
tiempos_por_tapas = [
  [1,2,3,4], # ciclista 1
  [1,2,3,4], # ciclista 2
  [1,2,3,4], # ciclista 3
  [1,2,3,4], # ciclista 4
] 

# obtengo la cantidad de filas
cant_filas = len(tiempos_por_tapas) # 4 
 
                      # creo una lista del 0 a la cantidad de filas
for numero_de_fila in range(cant_filas): 
  cant_columnas = len(tiempos_por_tapas[numero_de_fila]) # 4
                            # creo una lista del 0 a la cantidad de elementos en cada fila
  for numero_de_columna in range(cant_columnas):
    hora = 3600
    tiempos_por_tapas[numero_de_fila][numero_de_columna]  = randint(hora , hora*2)
    

for ciclista in ciclistas:
  print(f"los tiempos de {ciclista} son (en minutos):")
  for tiempos in tiempos_por_tapas[ciclistas.index(ciclista)]:
    print(tiempos//60,"\t")
    
 

tiempos_etapa1 = []
for fila in range(len(tiempos_por_tapas)):
  total = 0
  for tiempo in fila:
    total+=tiempo
  tiempos_etapa1.append(fila[0])
  
indexMejor = tiempos_etapa1.index(min(tiempos_etapa1))
print(ciclistas[indexMejor]," es el mejor ciclista")

 
  
  
 