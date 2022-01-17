#Manejo de string
cadena = "programación en python"
print(cadena[6])

# Longitud
print(len(cadena))
print(cadena[21])
i = len(cadena)-1
print(cadena[i])
print(i)
print(cadena[len(cadena)-1])

# Rebanada
print(cadena[0:10])
print(cadena[10:])
print(cadena[:10])
print(cadena[:13])
print(cadena[:13:2])
print(cadena[::2])
print(cadena[::-1])
print(cadena[-1:])

# Empezar subcadena (find)
print(cadena.find("python"))
print(cadena.find("p"))
print(cadena.find("z"))
print(cadena.find("z") == -1)

# Inclusion (in)
print("python" in cadena)

# Cadena numerica a tipo numerico (int)
precio = "40"
print(int(precio))
print(type(int(precio)))

# Conversion a mayusculas (upper) o a minusculas (lower)
print(cadena.upper())
print(cadena.lower())
print(cadena.title())
print(cadena.capitalize())

# Eliminar espacios al principio y final (strip)
a = "     hola"
print(a.strip())
a = "     hola   chau    "
print(a.strip())

# Contar ocurrencias de subcadena (count)
print(cadena.count("p"))
print(cadena.count("o"))

# Reemplazar subcadena (replace)
print(cadena.replace("python", "***"))