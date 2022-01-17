# Ejercicio#1
# Escribir una función que, dado un número de DNI,
# retorne True si el número es válido y False si
# no lo es. Para que un número de DNI sea válido
# debe tener entre 7 y 8 dígitos.
def DNIvalido(dni):
    cantidad=0
    while dni!=0:
        cantidad=cantidad+1
        dni=dni//10
    return cantidad==7 or cantidad==8
print(DNIvalido(3598))
print(DNIvalido(2596348))

# Ejercicio#2
# Escribir una función que, dado un número de DNI,
# retorne True si el número es válido y False si no
# lo es. Para que un número de DNI sea válido debe
# tener entre 7 y 8 dígitos.
def lenUltimaPalabra(cadena):
    longitud = len(cadena)
    if longitud==0:
        return 0
    cantidad=0
    for i in range(longitud):
        if cadena[i]!=' ':
            cantidad=cantidad+1
        else:
            if cadena[i]==" " and i<(longitud-1) and cadena[i+1]!=' ':
                cantidad=0
    return cantidad

# Ejercicio#3
# Escribir un programa que permita al usuario obtener un
# identificador para cada uno de los socios de un club.
# Para eso ingresará nombre completo y número de DNI de
# cada socio, indicando que finalizará el procesamiento
# mediante el ingreso de un nombre vacío.
# Precondición: el formato del nombre de los socios será:
# nombre apellido. Podría ingresarse más de un nombre,
# en cuyo caso será: nombre1 nombre2 apellido. Si un socio
# tuviera más de un apellido, el usuario sólo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos.
# En caso contrario, el programa debe dejar al usuario en
# un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único,
# el cual estará formado por: el primer nombre, la cantidad
# de letras del apellido y los primeros 3 dígitos de su DNI.
# Ejemplo:
# Nombre: Alba María Linares
# DNI: 25834910
# Alba7258

# Usamos las dos funciones anteriormente resueltas
def primerosTresDigitos(numero):
    while numero >= 1000:
        numero = numero / 10
    return int(numero)

def obtenerIdentificador(nombre, dni):
    nombre=nombre.strip()
    i=nombre[0:nombre.find(" ")]
    i=i+str(lenUltimaPalabra(nombre))
    i=i+str(primerosTresDigitos(dni))
    return i

#programa principal
nombre=input("Nombre del socio: ")
while nombre!="":
    dni=int(input("DNI del socio: "))
    while not(DNIvalido(dni)):
        print("Número inválido.")
        dni=int(input("DNI del socio: "))
    identificador = obtenerIdentificador(nombre,dni)
    print("El identificador del socio es: ",identificador)
    nombre=input("Nombre del socio: ")
