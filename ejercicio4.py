# Realizar un algoritmo que permita descomponer un número en sus factores primos.
# Análisis
# Vamos hacer un proceso iterativo, por el que se lle un número y se comprueba
# si es primo.
# Si es primo, se imprime y se termina el algoritmo.
# Si no es primo, se calcula el primer divisor, se muestra
# y se actuliza el número (numero / divisor) y se va a la siguiente iteración.

# import math
# num = int(input("Ingrese el numero: "))
# print("Factorizacion: ")
# factorizar = True
# # Mientras se pueda seguir factorizando y el número sea mayor que 1
# while factorizar and num > 1:
#     div = 1
# 	# Supongo que el número es primo, no se puede factorizar
#     factor_primo = True
#     # Compruebo si es primo
#     while div<=math.sqrt(num) and factor_primo:
#         div = div+1
# 		# Si se puede dividir por un número entre 2 y la raíz cudadrada del número
#         if num % div == 0:
# 			# Significa que no es primo
#             factor_primo = False
# 	# Si el número es primo, lo imprimo y hemos terminado
#     if factor_primo:
#         print(int(num))
#         factorizar = False
#     else: # Si no es primo, cáculo el nuevo número (num/div)y muestro el divisor
# 		# Y vuelvo a intentar factorizar
#         print(div)
#         num = num/div
#         factor_primo = True


# Mejora: hemos usado una función recursiva
import math
 
def factorizar(num):
    if num <= 1:
        return  # Detiene la recursión si el número es 1 o menor
    div = 2  # Inicializa el divisor en 2
    while div <= math.sqrt(num):  # Itera hasta la raíz cuadrada del número
        if num % div == 0:  # Verifica si el número es divisible por el divisor actual
            print(div)
            return factorizar(num // div)  # Llamada recursiva con el cociente de la división entera
        div += 1  # Incrementa el divisor en 1 para probar el siguiente número
    print(num)  # Si no se encontraron divisores, el número actual es primo y se imprime


num = int(input("Ingrese el número: "))  # Solicita al usuario ingresar un número
print("Factorización:")
factorizar(num)  # Llama a la función factorizar con el número ingresado
