nombres=['juan', 'pablo', 'luis', 'mauro', 'hector']

nombres_compuestos=[[nombre1, nombre2] for nombre1 in nombres for nombre2 in nombres if nombre1!=nombre2]

print(nombres_compuestos)