import mysql.connector 

conexion1=mysql.connector.connect(host="localhost", user="root", password="A0910z", database="db1")

cursor1=conexion1.cursor()

sql="insert into articulos (codigo, descripcion, precio) values (%s,%s,%s)"

datos=(1, "naranjas", 23.50)
cursor1.execute(sql, datos)

datos=(2, "peras", 34)
cursor1.execute(sql, datos)

datos=(3, "bananas", 25)
cursor1.execute(sql, datos)

conexion1.commit()
conexion1.close()