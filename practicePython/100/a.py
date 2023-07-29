import json

cadena='''
{
    "codigo":"1",
    "descripcion":"papa",
    "precio":"13.45"
}'''

print(cadena)
diccionario=json.loads(cadena)
print(diccionario)