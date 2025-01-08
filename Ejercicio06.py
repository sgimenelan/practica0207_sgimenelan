#Escribir un programa para gestionar un listín telefónico con los 
#nombres y los teléfonos de los clientes de una empresa. 
#El programa debe  incorporar funciones para crear el fichero
#con el listín si no existe, para consultar el teléfono de un
#cliente, añadir el teléfono de un nuevo cliente y eliminar el 
#teléfono de un cliente. El listín debe estar guardado en el fichero
#de texto listin.txt donde el nombre del cliente y su teléfono
#deben aparecer separados por comas y cada cliente en una línea distinta.
import os

def crear():
    if not os.path.isfile("listin.txt"):
        with open("listin.txt", "w") as file:
            print("Fichero creado correctamente.")
    else:
        print("El fichero ya existe.")

def numerotelefono(nombre):
    if os.path.isfile("listin.txt"):
        with open("listin.txt", "r") as file:
            clientes = file.readlines()
            for cliente in clientes:
                if cliente.startswith(nombre + ","):
                    print(f"Teléfono de {nombre}: {cliente.split(',')[1].strip()}")
                    return
            print(f"Cliente {nombre} no encontrado.")
    else:
        print("El fichero listin.txt no existe.")

def anadirtelefono(nombre, telefono):
    with open("listin.txt", "a") as file:
        file.write(f"{nombre},{telefono}\n")
    print(f"Cliente {nombre} añadido con éxito.")

def eliminartelefono(nombre):
    if os.path.isfile("listin.txt"):
        with open("listin.txt", "r") as file:
            clientes = file.readlines()
        with open("listin.txt", "w") as file:
            eliminado = False
            for cliente in clientes:
                if not cliente.startswith(nombre + ","):
                    file.write(cliente)
                else:
                    eliminado = True
            if eliminado:
                print(f"Cliente {nombre} eliminado.")
            else:
                print(f"Cliente {nombre} no encontrado.")
    else:
        print("El fichero listin.txt no existe.")


menu=""
while True:
    menu = int(input("(1)Crear listín \n(2)Consultar telefono \n(3)Añadir cliente \n(4)Eliminar cliente \n"))
    if menu == 1:
        print("***Creando listin...***")
        crear()

    if menu == 2:
        print("***Consultar telefono***")
        numerotelefono(input("Dime el nombre: "))

    if menu == 3:
        print("***Añadir cliente***")
        anadirtelefono((input("Dime el nombre: ")),(input("Dime el telefono:")))

    if menu == 4:
        print("***Eliminar cliente***")
        eliminartelefono(input("Dime el nombre: "))
