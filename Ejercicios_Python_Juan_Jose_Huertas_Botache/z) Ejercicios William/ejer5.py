class Estudiante:
    def __init__(self, nombre="", calificaciones=[]):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_media(self):
        return sum(self.calificaciones) / len(self.calificaciones)

def pasaron(estudiantes, umbral):
    aprobados = []
    for estudiante in estudiantes:
        if estudiante.calcular_media() >= umbral:
            aprobados.append(estudiante.nombre)
    return aprobados

def mejores(estudiantes, n=3):
    mejores_estudiantes = sorted(estudiantes, key=lambda x: x.calcular_media(), reverse=True)[:n]
    return [(e.nombre, e.calcular_media()) for e in mejores_estudiantes]

def mostrar_calificaciones(estudiante):
    print(f"Las calificaciones de {estudiante.nombre} son:")
    for i, calificacion in enumerate(estudiante.calificaciones):
        print(f"Calificación {i + 1}: {calificacion}")
    print(f"La media de {estudiante.nombre} es: {estudiante.calcular_media()}")

umbral = float(input("Ingrese el umbral de aprobación (entre 0 y 100): "))

estudiantes = []
num_estudiantes = int(input("¿Cuántos estudiantes desea agregar? "))

for i in range(num_estudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    calificaciones = []
    for j in range(5):
        calificacion = float(input(f"Ingrese la calificación {j + 1} para {nombre}: "))
        calificaciones.append(calificacion)
    estudiantes.append(Estudiante(nombre, calificaciones))

while True:
    print("\n¿Qué desea hacer?")
    print("1. Agregar otro estudiante")
    print("2. Mostrar los mejores")
    print("3. Mostrar la lista de todos los estudiantes y sus notas")
    print("4. Mostrar la nota de un estudiante en especifico")
    print("5. Acabar el programa")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        calificaciones = []
        for j in range(5):
            calificacion = float(input(f"Ingrese la calificación {j + 1} para {nombre}: "))
            calificaciones.append(calificacion)
        estudiantes.append(Estudiante(nombre, calificaciones))

    elif opcion == 2:
        print(f"Los {len(mejores(estudiantes))} mejores estudiantes son:")
        for estudiante in mejores(estudiantes):
            print(f"{estudiante[0]} con media de {estudiante[1]}")

    elif opcion == 3:
        for estudiante in estudiantes:
            mostrar_calificaciones(estudiante)

    elif opcion == 4:
        nombre = input("Ingrese el nombre del estudiante: ")
        for estudiante in estudiantes:
            if estudiante.nombre == nombre:
                mostrar_calificaciones(estudiante)

    elif opcion == 5:
        break

    else:
        print("Opción inválida. Por favor, intente de nuevo.")
