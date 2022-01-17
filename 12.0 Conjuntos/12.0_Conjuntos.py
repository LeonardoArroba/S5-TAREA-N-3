#1. Conjuntos
# Ejercicio#1.1
A=set()  #Conjuto vacio con set
print(type(A)) 

# Ejercicio#1.2
A={1,2,3}
print(A)

# Ejercicio#1.3
B= {1,2,3,1,2,3,1,2,3}   #Presenta sin repitir números
print(B)

# Ejercicio#1.4
print(A == B)

# Ejercicio#1.5
numeros=[1,2,3,2,1,3,2,1,3,2,1,2,3]  #Presenta lista tal como se ingreso y el mismo orden
print(numeros)

# Ejercicio#1.6
C = set(numeros)   #Si crea un conjunto a partir de lista numeros, presenta los numeros sin repetir
print(C)

# Ejercicio#1.7
for n in A:
    print(n)

# 2. Operación con conjuntos
# Ejercicio#2.1
print(len(A))

# Ejercicio#2.2
print(3 in A)

# Ejercicio#2.3
print(4 in A)

# Ejercicio#2.4
print(4 not in A)

# Ejercicio#2.5
print(A)
A.remove(1)   #Eliminar con remove
print(A)

# Ejercicio#2.6
print(B)
B.clear()
print(B)

# Ejercicio#2.7
B.add(8)      #Añadir un valor
B.add(9)
print(A==B)
print(A|B)

# Ejercicio#2.8
print(A&B)
A.add(8)
print(A&B)

# Ejercicio#2.9
# Incluición
print(A,B)
print(A<B)
print(A>B)
print(A==B)
print(B<set([7,8,9]))
print(A-B)
print(B-A)
print(A^B)