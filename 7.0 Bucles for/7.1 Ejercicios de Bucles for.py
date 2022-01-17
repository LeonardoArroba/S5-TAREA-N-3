# Ejercicios de Bucles for
# Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.
# ¿Qué modificación habria que hacer si ahora sólo se deben sumar los números que sean 
# multiplod de 3.
total = 0
for i in range(101):
    if i % 3 == 0:
        total = total + i
print("Sumatoria:", total)


# Dado un numero entero positivo, mostrar su factorial.
# El factorial de un número se obtiene multiplicando todos los números enteros positivos 
# que hay entre el 1 y ese número.
# El factorial de 0 es 1.
numero=int(input("Número:"))
f=1
if numero != 0:
    for i in range(1,numero+1):
        f = f * i
print("Factorial:",f)


# Crear un algoritmo que muestre los primeros 10 múmeros de la suceción fibonacci. 
# La suceción comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la 
# suma de los dos números anterioes en la secuencia.
n1=0
n2=1
print(n1)
print(n2)
for i in range(8):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3


# Escribir un programa que permita al usuario ingresar 6 numeros enteros, que pueden 
# ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos 
# y el promedio de los positivos.
# No olvides que no es posible dividir por cero, por lo que es necesario evitar que el 
# programa arroje un error si no se ingresaron números positivos. 
sumaNegativos = 0
sumaPositivos = 0
cantidadPositivos = 0
for i in range(6):
    nro = int(input("Número: "))
    if nro >= 0:
        cantidadPositivos += 1
        sumaPositivos += nro
    else:
        sumaNegativos += nro
print("Sumatoria de los negativos: ",sumaNegativos)
if cantidadPositivos != 0:
    print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
else:
    print("No se ingresaron números positivos")