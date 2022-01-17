#1. LISTAS
# Ejercicio#1.1
numeros = []
print(numeros)
print(type(numeros))

# Ejercicio#1.2
numeros = [1,2,3]
print(numeros)

# Ejercicio#1.3
letras = list()
print(letras)

# Ejercicio#1.4
letras = list("ABC")
print(letras)

# Ejercicio#1.5
print(list("ZXU"))

# Ejercicio#1.6
for i in range(len(letras)):
    print(letras[i])

# Ejercicio#1.7
i = 0
while i < len(letras):
    print(letras[i])
    i+=1

# Ejercicio#1.8
for elemento in letras:
    print(elemento)

#2. OPERACIONES CON LISTAS
# Ejercicio#2.1
dir(list)
numeros + letras
print(numeros)
print(letras)
numeros+list(range(4,10))

# Ejercicio#2.2
C = numeros+[letras]
print(C)
print(len(C))
print(len(numeros+letras))
print(C[1])
print(type(C[1]))
print(C[3])
print(type(C[3]))
print(C[3:])
print(C[::-1])
print(C[3][1])
print(C[len(C)-1])
print(numeros[2])

# Ejercicio#2.3
print(C.index(2))
print(C[3].index("A"))
print("A" in C)
print("A" in C[3])
print(2 in C)
print(C.append([5,6]))

#3. TUPLAS
# Ejercicio#3.1
dir(tuple)
tupla1 = ( )
print(tupla1)

# Ejercicio#3.2
tupla2 = ("ema")
print(tupla2)
print(type(tupla2))

# Ejercicio#3.3
tuple3 = tuple("ema")
print(tuple3)

# Ejercicio#3.4
tuple4 = tuple(C)
print(tuple4)

# Ejercicio#3.5
nueva = tuple("abcdefg")
print(nueva)
nueva = ("A",)+nueva[1:]
print(nueva)

# Ejercicio#3.6
A = [1,2,3]
B = (A,)
print(A)
print(B)
print(A.append(4))
