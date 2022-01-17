# Ejercicio#1
# 1) Solicitar al usuario que ingrese números, los cuales
# se guardarán en una lista. Finalizar al ingresar el
# número 0, el cual no debe guardarse.
# 2) A continuación, solicitar al usuario que ingrese un
# número y, si el número está en la lista, eliminar su
# primera ocurrencia. Mostrar un mensaje si no es posible
# eliminar.
# 3) Imprimir la sumatoria de todos los números de la lista.
# 4) Solicitar al usuario otro número y crear una lista con
# los elementos de la lista original que sean menores que el
# número dado. Imprimir esta nueva lista, iterando por ella.
# 5) Generar e imprimir una nueva lista que contenga como
# elementos a tuplas de dos elementos, cada una compuesta
# por un número de la lista original y la cantidad de veces
# que aparece en ella. Por ejemplo, si la lista original es
# [5,16,2,5,57,5,2] la nueva lista contendrá:
# [(5,3), (16,1), (2,2), (57,1)]
def sumatoria(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma

def numerosMenores(lista, limite):
    nueva=[]
    for n in lista:
        if n < limite:
            nueva.append(n)
    return nueva

def frecuencias(lista):
    nueva=[]
    for n in lista:
        if [n, lista.count(n)] not in nueva:
            nueva.append([n, lista.count(n)])
    return nueva

#1
numeros=[]
nro=int(input("Número: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Número: "))

#2
eliminar=int(input("Número a eliminar: "))
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese número no está entre los ingresados")

#3
print("Sumatoria de los números:", sumatoria(numeros))

#4
limite=int(input("Filtrar números menores a: "))
for n in numerosMenores(numeros, limite):
    print(n)

#5
print("Frecuencias:")
for tupla in frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces.")

