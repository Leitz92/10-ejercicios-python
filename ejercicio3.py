# Función CalcularVuelta: Recibe el dinero que hay que devolver y el valor de un
# billete o una moneda, devuelve el número de billetes o monedas de esa cantidad
# que hay que devolver y actualiza el dinero que queda por devolver.
# Parámetros de entrada: cantidad: valor del billete o la moneda
# Dato devuelto: vuelta: Número de billetes o monedas que hay que devolver y
# cantidad que queda por devolver

def calcular_vuelta(cambio: float, valor_monedillete) -> tuple:
    '''
    Función calcular_vuelta: Recibe el dinero que hay que devolver y el valor de un billete o moneda, devuelve el número de billetes o monedas de esa cantidad que hay que devolver y actualiza el dinero que queda por devolver.

    Parámetros de entrada: Cantidad -> Valor del billete o la moneda.

    Dato devuelto: Número de billetes o monedas que hay que devolver y la cantidad que queda por devolver.
    '''
    # Es necesario hacer un round() a cambio para evitar errores de precisión en los cálculos
    cambio = round(cambio, 2)
    # Hacemos la división entera para calcular el número de billetes necesarios
    num_monedilletes = int(cambio/valor_monedillete)
    # Actualizamos el valor del cambio después de restarle la cantidad necesaria
    vuelta = cambio - num_monedilletes*valor_monedillete
    return vuelta, num_monedilletes


def inicializar_billetes_monedas() -> tuple():
    '''
    Función inicializar_billetes_monedas: Recibe un vector "cantidades" donde vamos a guardar el valor de los billetes y monedas de mayor a menor.

    Valor devuelto: cantidades
    '''
    # Inicializamos una tupla con los valores de nuestros billetes y monedas de Euro
    # Utilizamos una tupla ya que es inmmutable y más rápida que una lista al operar con ella
    return (500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01)


def escribir_vuelta(num_monedilletes: int, valor_monedillete):
    '''
    Función escribir_vuelta: Recibe la cantidad de billetes o monedas y su valor y los imprime por pantalla.
    Se imprime si hay que devolver de ese billete o moneda, es decir, si la vuelta > 0.
    Si la cantidad > 2 se devuelven billetes (euros), si no se devuelven monedas y si la cantidad es >= 1 se devuelven euros, si no céntimos.
    '''
    # Solo imprimirá si hay al menos 1 monedillete
    if num_monedilletes > 0:
        # Si el monedillete és mayor a 2, significa que será un billete
        if valor_monedillete > 2:
            print(f'{num_monedilletes} billete/s de {valor_monedillete}€')
        # En este caso, solo puede imprimir monedas de 2€ o 1€
        elif valor_monedillete >= 1:
            print(f'{num_monedilletes} moneda/s de {valor_monedillete}€')
        # En cualquier otro caso imprime las monedas de céntimos (multiplicadas por 100 para que queden bonitas)
        else:
            print(f'{num_monedilletes} moneda/s de {int(valor_monedillete*100)} céntimo/s')


def run():
    '''
    Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad que se ha entregado.
    La aplicación debe calcular el cambio correspondiente con el menor número de monedas y/o billetes posibles
    '''
    try:
        # Datos de entrada del usuario
        total_a_pagar = validar_input(float(input('Introduce el total a pagar: ')))
        cantidad_entregada = validar_input(float(input('Introduce la cantidad entregada: ')))

    # Con el except comprobamos que el valor introducido es un número
    except ValueError:
        print('Error: La cantidad ingresada debe ser un número')
    else: 
        # Si la cantidad entregada es inferior a la total, finalizamos el programa.
        if cantidad_entregada < total_a_pagar:
            print('Te falta dinero por pagar, guapo\nFinalizando programa.')
            return
        
        # Si llegamos hasta aqui, calculamos el cambio correspondiente
        cambio = cantidad_entregada - total_a_pagar
        print(f'El cambio es de: {cambio:.2f}€')
        
        # Inicializamos el vector de monedas y billetes
        monedas_billetes = inicializar_billetes_monedas()

        # Recorremos todos los valores de la tupla inicializada
        for monedillete in monedas_billetes:
            # Invocamos a la función 'calcular_vuelta' y asignamos a dos variables los resultados de la función
            # Devuelve el cambio actualizado y el Nº de monedilletes necesarios
            cambio, num_monedilletes = calcular_vuelta(cambio, monedillete)

            # Invocamos a la función escribir_vuelta() para mostrar los resultados
            escribir_vuelta(num_monedilletes, monedillete)


# Función que valida la entrada de datos y comprueba que no sea negativo.
# Sigue pidiendo un valor hasta que sea correcto
def validar_input(entrada: float) -> float:
    if entrada < 0:
        print('Error: No se pueden introducir cantidades negativas')
        nueva_entrada = float(input('Vuelve a introducir: '))
        return validar_input(nueva_entrada)
    else:
        return entrada

if __name__ == '__main__':    
    run()