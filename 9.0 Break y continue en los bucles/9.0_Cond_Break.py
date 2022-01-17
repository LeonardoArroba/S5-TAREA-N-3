# Ejercicio#1
# while condición 1:
#     bloque a repetir
#     if condición 2:
#         break
#     resto del bloque
while True:
    print("Opción 1 - comenzar programa")
    print("Opción 2 - imprimir listado")
    print("Opción 3 - finalizar programa")
    opcion=int(input("Opción elegida: "))
    if opcion==1:
        print("¡Comenzamos!")
    elif opcion==2:
        print("Listado:")
        print("Nadia, Esteban, Mariela, Fernanda")
    elif opcion==3:
        print("Hasta la próxima")
        break
    else:
        print("Opción incorrecta. Debe ingresar 1, 2 o 3")

# Ejercicio#2
# while condición 1:
#     bloque a repetir
#     if condición 2:
#         continue
#     resto del bloque
frase=input("Frase: ")
l=input("Letra para buscar su posición: ")
i=0
while i!=len(frase):
    if l!=frase[i]:
        print("No se encontró en la posición", i)
        i+=1
        continue
    print("Se encontró en la posición", i)
    break