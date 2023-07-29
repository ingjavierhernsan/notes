import mysql.connector

try:
    conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
    cursor1=conexion1.cursor()
    cursor1.execute("show databasesqqqqqq")

    for base in cursor1:
        print(base)
except mysql.connector.errors.ProgrammingError:
    print("Error en el comando SQL")
finally:
    conexion1.close()
    print("Se cerro la conexion a la base de datos")