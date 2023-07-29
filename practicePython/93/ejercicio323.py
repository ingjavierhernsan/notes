def imprimir_si(lista, fn):
    for elemento in lista:
        if fn(elemento):
            print(elemento)

lista1=[9, 20, 70, 60, 19]

print("Valores paras de la lista.")
imprimir_si(lista1, lambda x: x%2==0)

print("Valores multiplos de 3 o de 5")
imprimir_si(lista1, lambda x: x%3==0 or x%5==0)

print("Imprimir valores mayores o iguales a 50")
imprimir_si(lista1, lambda x: x>=50)

print("Imprimir los valores comprendidos entre 1 y 50 o 70 y 100")
imprimir_si(lista1, lambda x: x>=1 and x<=50 or x>=70 and x<=100)

print("Imprimir la lista completa")
imprimir_si(lista1, lambda x: True)