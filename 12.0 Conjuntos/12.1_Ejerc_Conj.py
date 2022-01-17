# Ejercicio#1
# Solicitar al usuario que ingrese los nombres
# de pila de los alumnos de nivel primario de
# una escuela, finalizando al ingresar “x”.
# A continuación, solicitar que ingrese los
# nombres de los alumnos de nivel secundario,
# finalizando al ingresar “x”.
# 1. Informar los nombres de todos los alumnos
# de nivel primario y los de nivel secundario,
# sin repeticiones.
# 2. Informar qué nombres se repiten entre los
# alumnos de nivel primario y secundario.
# 3. Informar qué nombres de nivel primario no
# se repiten en los de nivel secundario.
def cargarNombres(alumnos):
    nombre=input("Nombre: ")
    while nombre!="x":
        alumnos.add(nombre)
        nombre=input("Nombre: ")
    return alumnos

 
primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

 
print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria|secundaria:
   print(nombre)

 
print("NOMBRES COMUNES:")
for nombre in primaria&secundaria:
   print(nombre)

 
print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria:
   print(nombre)
   
#Ejercicio#2
# Suponer una lista con datos de las compras hechas por
# clientes de una empresa a lo largo de un mes, la cual
# contiene tuplas con información de cada venta: (cliente,
# día del mes, monto, domicilio del cliente). Ejemplo:
# [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
# ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa",
# 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez",
# 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958,
# "Mirasol 218")]
# Escribir una función que reciba como parámetro una lista
# con el formato mencionado anteriormente y retorne los
# domicilios de cada cliente al cual se le debe enviar una
# factura de compra. Notar que cada cliente puede haber hecho
# más de una compra en el mes, por lo que la función debe
# retornar una estructura que contenga cada domicilio una
# sola vez.
def direcciones(ventas):
    domicilios=set()
    for venta in ventas:
       domicilios.add(venta[3])
    return domicilios