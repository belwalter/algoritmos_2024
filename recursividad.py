
def factorialI(numero):
    if numero == 0:
        return 1
    factorial = 1
    for i in range(1, numero+1):
        factorial *= i
    return factorial

#! N * N-1!
def factorialR(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorialR(numero-1)

print(factorialR(5))



#! N + N-1    | N0 = 0
#! ejercicio 2
def sumatoria(numero):
    if numero == 0:
        return 0
    else:
        return numero + sumatoria(numero-1)

print(sumatoria(10))

#! 5 * 3 = 5 + 5 + 5 = N * M = N + (N * M-1)
#! ejercicio 3
def producto(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1 + producto(num1, num2-1)

print(producto(2, 10))

#! 2 ^ 3 = 2 * 2 * 2 = B * (B * Ex-1)
#! ejercicio 4 
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

print(potencia(2, 10))

#! ejercicio 6  'hola' --> 'aloh'
def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

cadena = 'hola'
print(invertir_cadena(cadena))

#! ejercicio 7  = 1/n + (1/n-1...1)
def sumatoria_serie(numero):
    if numero == 1:
        return 1
    else:
        return 1/numero + sumatoria_serie(numero-1)

print(sumatoria_serie(5))

#! ejercicio 8 
def convert_to_binary(numero):
    if numero <= 1:
        return str(numero)
    else:
        return convert_to_binary(numero // 2) + str(numero % 2)

print(convert_to_binary(13))

#! ejercicio 10

def count_digit(numero):
    if numero < 10:
        return 1
    else:
        return 1 + count_digit(numero//10)

print(count_digit(123))

#! ejercicio 11
def invert_number(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) * 10 ** len(str(numero//10)) + invert_number(numero//10)


print(invert_number(1234567))


#! ejercicio 14
def sumar_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + sumar_digitos(numero//10)

print(sumar_digitos(71791))


# names = ['jaun', 'maria', 'pepito', 'ana']

# def barrido(lista):
#     if len(lista) == 1:
#         print(lista[0])
#     else:
#         print(lista[-1])
#         barrido(lista[:-1])


# barrido(names)

#! 
def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)



def fibonacci_iter(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        fibn_1 = 1
        fibn_2 = 0
        # fib_actual = None
        for i in range(2, numero+1):
            # # fib_actual = fibn_1 + fibn_2
            # fibn_2 = fibn_1
            # fibn_1 = fib_actual
            fibn_2, fibn_1 = fibn_1, fibn_1 + fibn_2
        return fibn_1

# print(fibonacci(7))
# print(fibonacci_iter(7))


numeros = [1, 2, 3, 7, 10, 23, 45]

def bb_recursiva(lista, buscado, primero, ultimo):
    medio = (primero + ultimo) // 2
    if primero > ultimo:
        return None
    elif buscado == lista[medio]:
        return medio
    else:
        if buscado < lista[medio]: 
            return bb_recursiva(lista, buscado, primero, medio-1)
        else:
            return bb_recursiva(lista, buscado, medio+1, ultimo)


pos = bb_recursiva(numeros, 7, 0, len(numeros)-1)
print(f"posicion {pos}")
if pos is not None:
    print(pos, numeros[pos])

numeros = [100, 23, 0, 5, 53, 7, 70, 2, 60, 90, 3, 46, 45]

def quicksort(lista, primero, ultimo):
    """Método de ordenamiento quicksort."""
    izquierda = primero
    derecha = ultimo-1
    pivote = ultimo
    print('indices', izquierda, derecha, lista[pivote])

    while (izquierda < derecha):

        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha):
            izquierda += 1
            print('deplazamineto izquierda', lista, izquierda)
            a = input()

        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda):
            derecha -= 1
            print('deplazamineto derecha', lista, derecha)
            a = input()

        if(izquierda < derecha):
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            print('intercambio interno', lista)
            a = input()

    if(lista[pivote] < lista[izquierda]):
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]
        print('intercambio pivote', lista)
        a = input()

    print('llamdas recursivas')
    if(primero < izquierda):
        quicksort(lista, primero, izquierda-1)
    if(ultimo > izquierda):
        quicksort(lista, izquierda+1, ultimo)


# quicksort(numeros, 0, len(numeros)-1)




#! raiz 25 = 5 * 5

def raiz_cuadarada(numero, valor=1):
    if numero == 0 or numero == 1:
        return numero
    else:
        resultado = valor * valor
        if resultado == numero:
            return valor
        elif resultado > numero:
            return valor -1
        else:
            return raiz_cuadarada(numero, valor+1)

print(raiz_cuadarada(15))

