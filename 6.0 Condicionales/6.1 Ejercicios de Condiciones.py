# Escribir un programa que, dado un número entero, muestre su valor absoluto.
# Nota: para los número positivos su valor absoluto es igual al número 
# (el valor absoluto de 52 es 52),mientras que, para los negativos, su valor 
# absoluto es el numero multuplicado por -1 (el valor absoluto de -52 es 52).
numero = int(input("Ingrese un numero: "))
if numero < 0:
    numero = numero*-1
print("El valor absoluto es ",numero)

nombre1=input("Un nombre: ")
nombre2=input("Otro nombre: ")
indice_final_nombre1 = len(nombre1)-1
indice_final_nombre2 = len(nombre2)-1
if nombre1[0] == nombre2[0] or nombre1[indice_final_nombre1] == nombre2[indice_final_nombre2]:
    print("Coincidencia")
else:
    print("No hay coincidencia")


# Crear un programa que permita al usuario elegir un candidato por el cual votar. 
# Las posibilidades son: cancidato A por el partido rojo, candidato B por el 
# partido verde, candidato C por el partido azul.
# Según el candidato elegido (A, B o C) se le debe imprimir el mensaje "Usted ha 
# votado por el partido [color que corresponda al candidato elegido"]
# Si el usuario ingresa una opcion que no corresponde a ninguno de los candidatos
# disponibles, indicar "Opcion errónea"
candidato=input("Candidato elegido: ")
if candidato.upper()=="A":
    print("Usted ha votado por el partido rojo")
elif candidato.upper()=="B":
    print("Usted ha votado por el partido verde")
elif candidato.upper()=="C":
    print("Usted ha votado por el partido azul")
else:
    print("Opcion erronea")


# Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre
# el mensaje "es vocal".
# Se debe validar que el usuario ingrese sólo un caracter. Si ingresa un string de 
# más de un caracter, informarle que no se puede procesar el dato.
letra = input("Ingrese una letra: ")
if len(letra)!=1:
    print("Debe ser solo una letra")
else:
    if letra.lower() in "aeiou":
        print("Es vocal")
        
        
# Hacer un programa que permita saber si un año es bisiesto. Para que un año sea 
# bisiesto debe sir divisible por 4 y no debe ser divisible por 100, excepto que 
# también sea divisible por 400.
anio = int(input("Ingrese el Año: "))
if anio % 4 != 0:
    print("No es bisiesto")
else:
    if anio % 100 != 0 or anio % 400 == 0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")
