try:
    valor1=int(input("Ingrese dividiendo: "))
    valor2=int(input("Ingrese divisor: "))
    division=valor1/valor2
    print("El resultado de la division es ", division)
except ZeroDivisionError:
    print("No se puese dividir por cero.")