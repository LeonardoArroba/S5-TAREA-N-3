# ¿Qué sucederia si la condición fuera if not numero == 1000?
numero = int(input("N. de cliente: "))
if numero == 1000:
    print("Ganaste un premio! ")
print("Continúa el programa")


# ¿Qué sucederia si el usuario ingresara a=10 y b=10?
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))
if a < b:
    print("El primero es menor")
else:
    print("El segundo es menor")


# Selección múltiple: if - elif - else
a = int(input("Un numero: "))
b = int(input("Otro numero: "))
if a<b:
    print("El primero es menor")
elif b<a:
    print("El segundo es menor")
else:
    print("Son iguales")

dia = input("Dia de la semana: ")
if dia == "lunes":
    print("Oh, no!")
elif dia == "viernes":
    print("Ya Casi!")
elif dia == "sabado" or dia == "domingo":
    print("Ahora si puede desacansar")
else:
    print("A esperar el fin de semana!")