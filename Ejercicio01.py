def tablamultiplicar(n):
    """La funcion recibe un número y crea un fichero con la 
    tabla de multiplicar del mismo
    Parámetros:
...   - numero: Un numero entero del 1 al 10
... Salida:
      - el fichero con la tabla de multiplicar """

    nombre = ("tabla-" + str(n) + ".txt")
    with open(nombre, "w") as file:
        for i in range(1, 11):
            file.write(str(i)+ "x"+ str(n)+ "="+ str(i * n) + "\n")
        return file
n = int(input("Introduce un numero entero del 1 al 10: "))
tablamultiplicar(n)
