# Mejora:
# Función validarLimites:
# Comprueba que el limite inferior sea realmente inferior

def validarLimites(liminf, limsup):
	if liminf > limsup:
		print('El límite inferior no puede ser mayor que el límite superior :/')
		nuevo_liminf = int(input("Límite inferior:"))
		nuevo_limsup = int(input("Límite superior:"))
		return validarLimites(nuevo_liminf, nuevo_limsup)
	else:
		return liminf, limsup



# Función devolverNumero: Recibe un intervalo (límite inferior y superior) y 
# devuelve el número intermedio como posible número que tiene que acertar.
# Parámetro de entrada: Límite inferior y superior del intervalo.
# Dato devuelto: Número intermedio del intervalo.

def devolverNumero(liminf,limsup):
	return (liminf+limsup)//2

# Función LeerOpcion: Recibe un intervalo (límite inferior y superior) y el número 
# que ha propuesto como solución y devuelve la opción escogida:
# 'S', si es correcto.
# 'A', si es más alto que el número a adivinar.
# 'B', si es más bajo. Al finalizar el programa, se deberá escribir el número de 
# intentos realizados para acertar el número.
# Si la opción es A, se modifica el límite inferior con el número propuesto.
# Si la opción es B, se modifica el límite superior con el número propuesto.
# Parámetro de entrada: Número propuesto
# Dato devuelto: Opción escogida, límite inferior y superior

def LeerOpcion(num,liminf,limsup):
	while True:
		print("¿Es correcto?")
		print("Pulsa S: si es correcto.")
		print("Pulsa A: si es más alto que el número a adivinar.")
		print("Pulsa B: si es más bajo.")
		opcion = input()
		if opcion.upper() == "S" or opcion.upper() == "A" or opcion.upper() == "B":
			break
		# Mejora: muestra un mensaje de error si la opción no es correcta
		else:
			print('La opción no es correcta\nVuelve a introducir:')
	if opcion.upper() == "A":
		return opcion,num,limsup
	if opcion.upper() == "B":
		return opcion,liminf,num
	return opcion,liminf,limsup

# Diseñar un programa que permita adivinar al ordenador un determinado número
# entero y positivo para lo cual se deben leer los límites en los que está 
# comprendido dicho número.
					

intentos = 0
print("Piensa un número...")
# Se pide el primer intervalo
print("Necesito saber el intervalo donde se encuentra el número:")

# Mejora: llamada a la función validarLimites
while True:
	try:
		limite_inferior, limite_superior = validarLimites(int(input("Límite inferior:")), int(input("Límite superior:")))
		break
	except ValueError:
		print('Debes introducir un número')

# Se va repitiendo hasta que se acierte el número
while True:
	# Escribimos el número propuesto (qué sera el número intermedio del intervalo)
	minumero = devolverNumero(limite_inferior,limite_superior)
	print("¿Has pensando en el número?:", minumero)
	# Incrementamos el número de intentos
	intentos = intentos+1
	# Leemos la opción, si no ha acertado se modifica algunos de los límites y se vuelve a proponer un nuevo número
	opcion, limite_inferior, limite_superior = LeerOpcion(minumero,limite_inferior,limite_superior)
	if opcion.upper()=="S":
		break
# Se escribe los intentos que ha necesitado para acertarlo
print("Lo he acertado en",intentos,"intentos.")