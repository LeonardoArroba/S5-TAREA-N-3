# Ejercicio#1
# Escribir un programa que solicite el ingreso de
# una cantidad indeterminada de números mayores que 1,
# finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.
# Note: Un número primo es un número natural mayor que 1
# que tiene únicamente dos divisores distintos: Él mismo
# y el 1.
cantidad=0
n=int(input("Número: "))
while n!=0:
    primo=True
    for i in range(2,n):
        if n%i==0:
            primo=False
            break
    if primo:
        cantidad+=1
    n=int(input("Número: "))
print("primos: ", cantidad)

# Ejercicio#2
# Escribir un programa que permita el usurio ingresar dos años
# y luego imprima todos los años en ese rango, que sean bisiestos
# y multiplos de 10.
# Nota: Para que un años sea biseesto debe ser divisible por 4 y
# no debe ser divisible por 100, excepto que tambiín sea disible
# por 400.
anioInicio=int(input("Año inicial:"))
anioFin=int(input("Año final:"))
for anio in range(anioInicio, anioFin+1):
    if not anio%10==0:
        continue
    if not anio%4==0:
        continue
    if anio%100!=0 or anio%400==0:
        print(anio)

