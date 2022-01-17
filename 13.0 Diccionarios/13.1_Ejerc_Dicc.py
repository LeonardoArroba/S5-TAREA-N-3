# Ejercicio#1
# Escribir un programa que procese strings ingresados
# por el usuario. La lectura finaliza cuando se hayan
# procesado 50 strings. Al finalizar, informar la
# cantidad total de ocurrencias de cada carácter, en
# todos los strings ingresados. Ejemplo: 
# "r":5
# "%":3
# "a":8
# "9":1.
# ¿Cómo se podrían informar las ocurrencias de las
# letras del alfabeto únicamente, incluyendo el valor 0
# para las letras que no aparecieron?
contadores={}
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
for letra in alfabeto+alfabeto.upper():
    contadores[letra]=0
for i in range(50):
   cadena=input("Cadena de caracteres: ")
   for caracter in cadena:
       if caracter.lower() in alfabeto:
           contadores[caracter]+=1
for caracter, cantidad in contadores.items():
   print(caracter, ": ", cantidad)
   
# Ejercicio#2
