from urllib import request
from urllib import error

try:
    pagina=request.urlopen("http://www.scratchya.com.ar/pythonya/ejercicio336/pagianx.html")
    datos=pagina.read().decode("utf-8")
    print(datos)
except error.HTTPError as err:
    print(f"Codigo de respuesta HTTP devuelto por el servidor {err.code}")
    print(f"No existe el recurso {err.filename}")