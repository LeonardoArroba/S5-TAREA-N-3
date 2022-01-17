# while condicion:
# bloque a repetir
total=0
nro=int(input("Número: "))
while nro != 0:
    total += nro
    nro = int(input("Número: "))
print("Total: ",total)


# Segundo Ejercicio
positivos = 0
n = int(input("Número (0 para terminar): "))
while n != 0:
    if n > 0:
        positivos += 1
    n = int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", positivos)


# Tercer Ejercicio
mayor = -1
n = int(input("Número positivo: "))
while n >= 0:
    if n > mayor:
        mayor = n
    n = int(input("Número positivo: "))
print("Mayor número ingresado:",mayor)


# Cuarto Ejercicio
suma = 0
n = int(input("Número positivo: "))
while n != 0:
    digito = n % 10
    suma += digito
    n = n // 10
print("Suma de los dígitos:",suma)


# Quinto Ejercicio
pares = 0
n = int(input("Número (-1 para terminar el programa): "))
while n != -1:
    if n % 2 == 0:
        pares += 1
    suma = 0
    while n != 0:
        digito = n % 10
        suma += digito
        n = n// 10
    print("Suma de sus dígitos:",suma)
    n=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron",pares,"números pares")