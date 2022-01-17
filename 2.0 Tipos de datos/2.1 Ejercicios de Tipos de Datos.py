# ¿De que tipo es cada uno de los siguientes datos?
print(100/5)
print(type(100/5))
print(7/2)
print(type(7/2))
print(7//2)
print(type(7//2))
print(7 % 2)
print(type(7 % 2))
print("a")
print(type("a"))
print("tiza" + ".")
print(type("tiza" + "."))
print("hola"[1+1])
print(type("hola"[1+1]))
print(len("hola"))
print(type(len("hola")))
print(int("145"))
print(type(int("145")))
print(float("145"))
print(type(float("145")))
print(str(32))
print(type(str(32)))
print(1 + 2 != 3)
print(type(1 + 2 != 3))
print(177 % 2 == 0)
print(type(177 % 2 == 0))
print(len("nube") <= 20)
print(type(len("nube") <= 20))

# ¿Qué guardan las variables luego de cada operacion?
n = 167 / 10
print(n)
n = 167 // 10
print(n)
n = 167 % 10
print(n)

letra = "a"
print(letra)
print(type(letra))
saludo = "hola" + letra
print(saludo)
C = saludo[0]
print(C)
C = saludo[1+3]
print(C)
L = len(saludo)
print(L)
C = saludo[len(saludo)-1]
print(C)
menor = "a" < "b"
print(menor)
D = 1!=1
print(D)
D = "cinta" >= "canto"
print(D)
c = "z" + "a" + "paz" [0]
print(c)
x = c[0] == "z"
print(x)

# Cuáles de las siguientes operaciones arrojan error?
a = 11 - ( 4 % 2 + 10 )
print(a)
b = "30" + 2
c = "30" + "2"
d = "hola" [len("hola")]
e = len(124)
f = "hola" [len("fin")]
g = "hola" [11 - ( 4 % 2 + 10 )]
h = int("4")
i = int(4)
j = int("z")
k = int("4.")
l = 4 < "f"
# m = "palabra" = "rama"
n = "palabra" == "rama"

