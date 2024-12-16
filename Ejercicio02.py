#Escribir una función que pida un número entero entre 1 y 10,
#  lea el fichero tabla-n.txt con la tabla de multiplicar de 
# ese número, donde n es el número introducido, y la muestre 
# por pantalla. Si el fichero no existe debe mostrar un mensaje
#  por pantalla informando de ello.
import os
def verificar(nombre):
    """La funcion recibe un nombre de un fichero, verifica si existe
    Parámetros:
...   - nombre: nombre del fichero
... Salida:
    -si exsiste: lo muestra por pantalla
    -no existe: muestra error"""

    nombre = ("tabla-" + str(n) + ".txt")
    if os.path.isfile(nombre):
        file = open(nombre, "r")
        print(file.read())
        file.close()
    else:
        print("¡El fichero", nombre, "no existe!")
n = int(input("Introduce un numero entero del 1 al 10: "))
verificar(n)
