archi1=open("datos.txt", "r+")
contenido=archi1.read()

print(contenido)

archi1.write("Otra linea 1\n")
archi1.write("Otra linea 2\n")

archi1.close()