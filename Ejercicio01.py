n = int(input("Introduce un numero entero del 1 al 10: "))
with open("tabla-" + str(n) + ".txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i)+ "x"+ str(n)+ "="+ str(i * n) + "\n")