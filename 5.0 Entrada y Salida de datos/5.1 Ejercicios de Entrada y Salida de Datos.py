# Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada N.
# A continuacion se debe mostrar en pantalla el texto "Ahora estas en la matriz. [usuario]", donde 
# [usuario] se reemplazara por el nombre que el usuario haya ingresado.
N = input("Tú nombre: ")
print("Ahora estas en la matrix,",N)


# Hacer un programa que solicite al usuario cuánto cósto una cena en un restaurante. A ese valor,
# sumarle un 6.2% en concepto de servicio y un 10% de propina.
# Imprimir en pantalla el monto final a pagar.
costo = float(input("Costo de la cena: $"))
servicio = costo*0.062
propina = costo*0.1
print("Costo total de la comida: $",costo+servicio+propina)


# Solicitar al usuario que ingrese el dia, mes y año de su nacimiento y almacenar cada uno de ellos en una 
# variable numérica (en total, tres ariables diferentes). Finanmente, mostrar la fecha en formato dd/mm/aa.
# Hacer otra version del programa, pero esta vez almacenando todo en una única variable numérica, en la 
# forma DDMMAAAA. ¿I si la variable fuera de tipo string?
dia = int(input("Dia tu nacimiento: "))
mes = int(input("Mes tu nacimiento: "))
anio = int(input("Año tu nacimiento: "))
print(str(dia) + "/" + str(mes) + "/" + str(anio))

fecha = int(input("Ingrese una fecha en formato ddmmaaaa: "))
anio = fecha % 10000
dia= fecha // 1000000
mes= (fecha // 10000) % 100
print(str(dia) + "/" + str(mes) + "/" + str(anio))

fecha = input("Ingrese una fecha en formato ddmmaaaa: ")
dia = fecha[:2]
mes= fecha[2:4]
anio= fecha[4:]
print(dia + "/" + mes + "/" + anio)


# Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto,para saber 
# cuántos tanques de combustible consumira el viaje entero.
# Para eso deben ingresar cuántos kilómetros puede recorrer su moto con 1 litro de combustible,qué capacidad 
# (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
# Hacer un programa que solicite los datos necesarios y luego inferme la cantidad de tanques de combustible 
# necesarios.
capacidad = float(input("Capacidad del tanque: "))
kmlx = float(input("Rendimiento (Km por litro: "))
recorrido = float(input("Km totales a recorrer: "))
kmxtanque = capacidad * kmlx
print("Seran necesarios",recorrido/kmxtanque, "tanques.")



