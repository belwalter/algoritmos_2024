
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