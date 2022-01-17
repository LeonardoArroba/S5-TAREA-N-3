# Ejercicio#1
# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
# cortando el ingreso de datos cuando el usuario ingrese el monto 0.
# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto.
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total
# de $1000, se le debe aplicar un 10% de descuento.
total=0
monto=float(input("Monto de una venta: $"))
while monto!=0:
    if monto<0:
        print("Monto no válido.")
    else:
        total+=monto
    monto=float(input("Monto de una venta: $"))
if total>1000:
    total-=total*0.1
print("Monto total a pagar: $", total)

# Ejercicio#2
# Crear un programa que solicite el ingreso de números enteros positivos,
# hasta que el usuario ingrese el 0. Por cada número, informar cuántos
# dígitos pares y cuántos impares tiene.
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares
# leídos en total.
totalPares=0
totalImpares=0
numero=int(input("Número: "))
while numero!=0:
    pares=0
    impares=0
    while numero!=0:
        ultimodigito=numero%10
        if ultimodigito%2==0:
            pares+=1
            totalPares+=1
        else:
            impares+=1
            totalImpares+=1
        numero=numero//10
    print("El número ingresado tiene ",pares," dígitos pares y ",impares," dígitos impares")
    numero=int(input("Otro número: "))
print("Total de dígitos pares:", totalPares)
print("Total de dígitos impares:", totalImpares)

# Ejercicio#3
# Crear un programa que permita al usuario ingresar títulos de libros por teclado,
# finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el
# usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se
# considera que termina una línea.
# Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9)
# aparecieron en total (en todos los títulos delibros que componen en esa línea).
# Finalmente, informar cuántas líneas completas se ingresaron.
# **Ejemplo de ejecución:**
# Libro: Los 3 mosqueteros
# Libro: Historia de 2 ciudades
# Libro: /
# Línea completa. Aparecen 2 dígitos numéricos.
# Libro: 20000 leguas de viaje submarino
# Libro: El señor de los anillos
# Libro: /
# Línea completa. Aparecen 5 dígitos numéricos.
# Libro: 20 años después
# Libro: *
# Fin. Se leyeron 2 líneas completas.
digitosEnLaLinea=0
cantLineas=0
titulo=input("Título del libro: ")
while titulo!="*":
    if titulo =="/" :
        cantLineas+=1
        print("Línea completa. Aparecen ", digitosEnLaLinea, " dígitos")
        digitosEnLaLinea = 0
    else:
        for caracter in titulo:
            if caracter in "0123456789":
                digitosEnLaLinea+=1
    titulo=input("Título del libro: ")
print("Fin. Se leyeron ",cantLineas," líneas completas")