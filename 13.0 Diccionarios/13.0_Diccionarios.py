# 1. Diccionarios
# Ejercicio#1.1
A=dict()
print(A)

# Ejercicio#1.2
B={}
print(B)

# Ejercicio#1.3
traducciones= {"hola":"hello", "adiós":"bye", "Día":"day", "noche":"night"}
print(traducciones)

# Ejercicio#1.4
calendario = [("enero",1), ("febrero",2), ("marzo",3)]
meses=dict(calendario)
print(meses)
print(type(meses))

# Ejercicio#1.5
equipo={8:["Melina",16,3], 2:["Lucia", 14, 1], 6: ["Karen", 15,2], 9:["Sonia",16,11]}
print(equipo)

# 2. Iteraciones
# Ejercicio#2.1
for clave in traducciones.keys():
    print(clave)

# Ejercicio#2.2
print(traducciones.keys())

# Ejercicio#2.3
for valor in traducciones.values():
    print(valor)
    
# Ejercicio#2.4
for clave in traducciones.keys():
    print(clave,"==>",traducciones[clave])
    
# Ejercicio#2.5
for clave, valor in traducciones.items():
    print(clave, "==>", valor)
    
# Ejercicio#2.6
for par in traducciones.items():
    print(par[0], "---", par[1])
    
# Ejercicio#2.7
for datos in equipo.values():
    print("nombre:", datos[0], "- edad:", datos [1], "- años en el equipo", datos[2])

# 3. Contenedores
# Ejercicio#3.1
print(len(equipo))

# Ejercicio#3.2
print("hola" in traducciones.keys())
print("hola" in traducciones)
print("hello" in traducciones.values())
print ("Sonia" in equipo.values())

# 4. Corchetes[]
# Ejercicio#4.1
print(traducciones["adiós"])
print(type(traducciones["adiós"]))

# Ejercicio#4.2
print(equipo[9])
print(type(equipo[9]))

# Ejercicio#4.3
print(equipo [9][1])

# Ejercicio#4.4
print(traducciones.get("reloj"))
print(traducciones.get("reloj"), "No existe esa palabra")

# Ejercicio#4.5
print(traducciones.get("hola", "hi"))
traducciones["hola"]="hi"
print(traducciones["hola"])

# Ejercicio#4.6
print(equipo)
equipo[2] [1]=15
print(equipo)

# Ejercicio#4.7
traducciones["reloj"]="clock"
print(traducciones)
print(traducciones["reloj"])

# Ejercicio#4.8
traducciones.update({"mesa":"table", "silla":"chair", "sillón":"couch"})
print(traducciones)

# Ejercicio#4.9
equipo[5]= "maría" 
print(equipo)

# Ejercicio#4.10
del equipo[5]
print(equipo)