import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", password="A0910z", database="db1")

cursor1=conexion1.cursor()
cursor1.execute("select codigo, descripcion, precio from articulos")

for fila in cursor1:
    print(fila)

conexion1.close()