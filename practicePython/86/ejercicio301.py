try:
    archi1=open("datos.txt","w")
    archi1.write("Primer linea.\n")
    archi1.write("Segunda linea.\n")
    archi1.write("Tercer linea.\n")
    archi1.write(3334)
except TypeError:
    print("No se puede grabar un entero con write.")
finally:
    archi1.close()
    print("Se cerro el archivo.")