import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", password="A0910z", database="db1")

cursor1=conexion1.cursor()

sql="insert into articulos (descripcion, precio) values (%s,%s)"

datos=("naranjas", 23.50)
cursor1.execute(sql, datos)

conexion1.commit()

print("Valor del ultimo codigo de articulo generado: ", cursor1.lastrowid)

conexion1.close()