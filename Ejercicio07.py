import csv
import os

def leer_calificaciones(fichero):
    """Lee las calificaciones desde un fichero y las devuelve como una lista de diccionarios"""
    if os.path.isfile(fichero):
        with open(fichero, "r") as file:
            lector = csv.DictReader(file)
            lista = sorted([dict(row) for row in lector], key=lambda x: x["Apellido"])
            return lista
    else:
        print("El fichero no existe.")
        return []

def calcular_notas_finales(lista_alumnos):
    """Calcula la nota final de cada alumno y la añade al diccionario"""
    for alumno in lista_alumnos:
        parcial1 = float(alumno["Parcial1"])
        parcial2 = float(alumno["Parcial2"])
        practicas = float(alumno["Practicas"])
        alumno["Nota Final"] = round(parcial1 * 0.3 + parcial2 * 0.3 + practicas * 0.4, 2)
    return lista_alumnos

def clasificar_alumnos(lista_alumnos):
    """Clasifica a los alumnos en aprobados y suspensos"""
    aprobados = []
    suspensos = []
    for alumno in lista_alumnos:
        asistencia = int(alumno["Asistencia"])
        if (asistencia >= 75 and
                float(alumno["Parcial1"]) >= 4 and
                float(alumno["Parcial2"]) >= 4 and
                float(alumno["Practicas"]) >= 4 and
                float(alumno["Nota Final"]) >= 5):
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    return aprobados, suspensos


fichero = "calificaciones.csv"
if os.path.isfile(fichero):
    alumnos = leer_calificaciones(fichero)
    alumnos = calcular_notas_finales(alumnos)
    aprobados, suspensos = clasificar_alumnos(alumnos)

    print("Aprobados:")
    for a in aprobados:
        print(a)

    print("\nSuspensos:")
    for s in suspensos:
        print(s)
else:
    print("El fichero calificaciones.csv no existe.")