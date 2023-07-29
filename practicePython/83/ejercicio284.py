import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", password="A0910z")

cursor1=conexion1.cursor()

sql="drop database if exists db2"
cursor1.execute(sql)

sql="create database db2"
cursor1.execute(sql)

sql="use db2"
cursor1.execute(sql)

sql="""create table usuarios (
        nombre varchar(30) primary key,
        clave varchar(30)
        )"""
cursor1.execute(sql)

conexion1.commit()
conexion1.close()