try:
    valor1=int(input("Ingrese dividendo: "))
    valor2=int(input("Ingrese divisor: "))
    division=valor1/valor2
    print("El resultado de la division es ", division)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Los valores a ingresar deben ser enteros")