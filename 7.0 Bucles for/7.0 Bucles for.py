# Bucles for
# for variable in cadena:
#    bloque a repetir
for x in range(10):
    print(x)

# range(fin)
for x in range(100,200):
    print(x)

# range(inicio, fin)
for x in range(5,20,3):
    print(x)

# range(inicio, fin, paso)
n=int(input("Número: "))
for x in range(n, n*2):
    print(x)


# Ejercicio Nº 1
c=int(input("Cantidad de números: "))
total=0
for variable in range(c):
    numero=int(input("Número a sumar: "))
    total+=numero
print("Total de la suma:", total)


# Ejercicio Nº 2
frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
    if x in frase:
        print(x)


# Ejercicio Nº 3
frase=input("Frase: ")
cantidad=0
for x in frase:
    if x in "aeiou":
        cantidad+=1
print("Cantidad de vocales:", cantidad)
