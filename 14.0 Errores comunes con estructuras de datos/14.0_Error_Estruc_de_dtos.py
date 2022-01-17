# Concatenar una lista con un dato de otro tipo
# lista=[1,2,3,4]
# lista=lista+5
# Ejercicio#1
lista=[1,2,3,4]
lista=lista+[5]
print(lista)
otra =[9,8,7]
lista=lista+otra
print(lista)
a = lista+[otra]
print(a)

#Imprimir una estructura direcmente, sin iterar
#lista=[1,2,3,4]
#print(lista)
# Ejercicio#1
lista = [1,2,3,4]
for elemento in lista:
    print(elemento)

# Ejercicio#2
articulos = { 154: ["jabón en polvo","limpieza", True],
             248: ["talco","cosmética",False],
             199 : ["cera para pisos", "limpieza", True] }
for clave,valor in articulos.items():
    print("Código: ",clave)
    print("Descripción: ", valor[0])
    print("Rubro: ", valor[1])
    if valor [2]:
        print("Hay stock")
    else:
        print("Agotado")
    print("--------------------------------")
    
# No considerar los extremos de una lista o las casos
# "especiales" [como el de lista vacía]
# lista=[1,3,4,4,6,7,7,8,0,9,9,9]
# for i in range(len(lista)):
#     if lista[i]==lista[i+1]:
#         print(lista[i])
# Ejercicio#1
lista=[1,3,4,4,6,7,7,8,0,9,9,9]
for i in range(len(lista)-1):
    if lista [i] == lista[i+1]:
        print(lista[i])

# Buscar en una estructura a un determinado
# elemento que solo puede estar en una 
# estructura anidada
# empleados={ 100: ["Jorge Millás", "Administración"],
#            200: ["Oriana López", "Gerencia"],
#            300: ["Gualupe Ríos", "RR.HH."],
#            400: ["Lionel Campos", "Ventas"]}
# nombre= input("Nombre de empleado: ")
# if nombre not in empleados.values():
#     print("El empleado no se encuentra en la nómina")
# Ejercicio#1
def empledoExiste(empleados, nombre):
    for datos in empleados.values():
        if datos[0] == nombre:
            return True
    return False

empleados={ 100: ["Jorge Millás", "Administración"],
           200: ["Oriana López", "Gerencia"],
           300: ["Gualupe Ríos", "RR.HH."],
           400: ["Lionel Campos", "Ventas"]}

nombre= input("Nombre de empleado: ")
if not empledoExiste(empleados, nombre):
    print("El empleado no se encuentra en la nómina")

# Iterar por un diccionario buscando una clave
# alumnos = { " 121-5": 42752983,
#            "243-9": 39234110,
#            "113-8": 44988782,
#            "324-1": 39110245 }
# legajo=input("Legajo a buscar: ")
# for clave in alumnos.keys():
#     if clave == legajo:
#         print("El DNI es: ", alumnos[clave])
# Ejercicio#1
alumnos = { " 121-5": 42752983,
           "243-9": 39234110,
           "113-8": 44988782,
           "324-1": 39110245 }

legajo=input("Legajo a buscar: ")
if legajo in alumnos.keys():
    print("El DNI es: ", alumnos[legajo])

# Acceder por nombre de variables inexistentes a los datos de una lista
# def cargarDatos(diccionario):
#     dni=int(input("DNI: "))
#     while dni !=0:
#         nombre=input("Nombre: ")
#         domicilio=input("Domicilio: ")
#         telefono=int(input("Teléfono: "))
#         diccionario[dni]=[nombre,domicilio,telefono]
#         dni=int(input("DNI: "))
#     return diccionario
# def imprimirDatos(diccionario):
#     for clave,valor in diccionario.items():
#         print(dni, nombre, domicilio, telefono)
# Ejercicio#1
def cargarDatos(diccionario):
    dni=int(input("DNI: "))
    while dni !=0:
        nombre=input("Nombre: ")
        domicilio=input("Domicilio: ")
        telefono=int(input("Teléfono: "))
        diccionario[dni]=[nombre,domicilio,telefono]
        dni=int(input("DNI: "))
    return 

def imprimirDatos(diccionario):
    for clave,valor in diccionario:
        print("DNI: ",clave, "Nombre: ",valor[0], "Domicilio: ",valor[1], "Teléfono: ",valor[2])

cliente= { 44299132: ["Gastón Quinteros", "Los Tilos 412", 58211972],
          38110223: ["Valeria Giménez", "Almendros 192", 59912834],
          27918006: ["Diego Linares", "Las Fresias 881", 51288390] }
cliente = cargarDatos(cliente)
imprimirDatos(cliente)

# Cargar todos los datos en una misma lista cuando deberían se diferentes
# def cargarMercaderias(mercaderias):
#     articulo=[]
#     codigo=int(input("Código: "))
#     while codigo !=0:
#         descripcion = input("Descripción: ")
#         articulo.append(descripcion)
#         rubro=input("Rubro: ")
#         articulo.append(rubro)
#         mercaderias[codigo]=articulo
#         codigo=int(input("Código: "))
#     return mercaderias
# Ejercicio#1
def cargarMercaderias(mercaderias):
    codigo=int(input("Código: "))
    while codigo !=0:
        articulo=[]
        descripcion = input("Descripción: ")
        articulo.append(descripcion)
        rubro=input("Rubro: ")
        articulo.append(rubro)
        mercaderias[codigo]=articulo
        codigo=int(input("Código: "))
    return mercaderias
productos = {}
productos = cargarMercaderias(productos)
for codigo, datos in productos.items():
    print(codigo, "- Descripción: ", datos[0], "-Rubro: ", datos[1])
    
# Modificar la cantidad de elementos de la estrructura que se está iterando
# a=[1,2,3,4]
# for i in range(len(a)):
#     if i==2:
#         del a[3]
#     print(a[i])
# Ejercicio#1
b={"a":[1,2,3], "b": [], "c":[8,6], "d":[], "e":[4]}
claves = list(b.keys())
for clave in claves:
    if b[clave]==[]:
        del b[clave]
print(b)