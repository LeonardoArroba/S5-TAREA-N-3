# Un empresario que se dedica al espectaculo necesita un programa que le ayude a hacer ciertos cálculos cada vez que organiza un concierto en 
# un estadio deportivo.
# Lo primero que necesita saber es qué capacidad de público tendra cada concierto, para saber cuántas entradas o boletos tienen que imprimirse.
# Para eso, cuando contrata un estadio deportivo, pregunta cuántos metros cuadrados tiene. Él sabe que, por metro cuadrado. caben 4 personas. 
# También sabe que siempre hay un espacio con gradas y que normalmente éstas ocupan un 20% de los metros cuadrados totales. En cada estadio las
# gradas pueden ser diferentes, así que el empresario consulta cuánta gente cabe en ellas.
# Cuando contrata a la banda que dará el concierto, ésta le indica qué porcentaje del espacio disponible necesitan ellos para montar su escenario.
# Con estos datos, debe calcularse cuánta gente va a caber en el estadio para un concierto determinado. El empresario, cada vez que use el programa, 
# va a ingresar la cantidad de metros cuadrados que tiene el estadio que contrató, la cantidad de gente que cabe en las gradas y el porcentaje de 
# espacio ocupado por el escenario.
# Luego, él quiere saber cuánto dinero ingresaría si vende todas las entradas disponibles, sabiendo que el 30% de las entradas vendidas seran 
# "a precio especial" y el resto son "a precio comun". El empresario ingresa el precio de cada tipo de entrada cuando usa el programa.
CAPACIDADM2 = 4
PORCENTAJEGRADAS = 0.2
PORCENTAJEESPECIALES = 0.3
PORCENTAJECOMUNES = 0.7

dimensiones = float(input("Dimensiones del estadio en (m2): "))
personasengradas = int(input("Cantidad de personas que caben en las gradas: "))
porcentajeescenario = int(input("Porcentaje que ocupa el escenario: "))
m2gradas = dimensiones * PORCENTAJEGRADAS
m2escenario = dimensiones * (porcentajeescenario/100)
m2disponibles = dimensiones - m2gradas - m2escenario
personastotales = (m2disponibles * 4) + personasengradas
print("Caben",personastotales, "personas")
precioentradaespecial = float(input("Precio entrada especial: $"))
precioentradacomun = int(input("Precio entrada comun: $"))
print("Ingreso total de ventas: $",
      (personastotales*PORCENTAJEESPECIALES)*precioentradaespecial + 
      (personastotales*PORCENTAJECOMUNES)*precioentradacomun)
