# Ejercicio#1
# Imprime: 9, 10
# Cambiar el nombre de los parámetros no afecta
# en nada, porque el valor retorna por la función
# no se está usando en el programa principal.
def coordenadaZ(x,y):
    x=x+10
    y=y+15
    return x+y

# Pograma principal
x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
    z=coordenadaZ(x,y)
    x=x+1
    y=y+1
print(x," . ",y)

# Ejercicio#2
# El siguiente programa debería imprimir el número
# 2 si se le ingresan como valores x=5, y=1 pero
# en su lugar imprime 5. ¿Qué hay que corregir?

# def maximo(a,b):
#     if x>y:
#         return x
#     else:
#         return y

# def minimo(a,b):
#     if x<y:
#         return x
#     else:
#         return y

# #programa principal
# x=int(input("Un número: "))
# y=int(input("Otro número: "))
# print(maximo(x-3, minimo(x+2, y-5)))

def maximo(a,b):
    if a>b:
        return a
    else:
        return b

def minimo(a,b):
    if a<b:
        return a
    else:
        return b

#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

