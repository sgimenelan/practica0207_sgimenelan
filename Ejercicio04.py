#Escribir un programa que acceda al fichero de internet 
#mediante la url indicada y muestre por pantalla el número
# de palabras que contiene.
import urllib.request
url = "http://textfiles.com/adventure/aencounter.txt"
file = urllib.request.urlopen(url)
for line in file:
    x = file.read()
    palabras = len(x.split())
    file.close()
    print(palabras)




