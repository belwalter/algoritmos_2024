print("Hola Mundo!!", 'Desde Python')


#! VARIABLES y CONSTANTES

VALOR = 10

numero = 19
print(type(numero))
numero = 19.8
print(type(numero))
numero = True
print(type(numero))
numero = "HOLA"
print(type(numero))
numero = None
print(type(numero))

# numero = input('ingrese un numero: ')
# print('dato ingresado:', numero)

#! Operacion aritmeticas

print(2 + 1)
print(2 - 1)
print(2 * 1)
print(5 / 2)
print(5 // 2)
print(5 % 2)
print(2 ** 5)


#! Conversion int(), str(), flot(), bool()
# numero = int(input('ingrese un numero: '))
# print('resultado:', numero * 2)

#! cotrol de flujo, estructuras de control condicionales, bucles, funciones

#! Condicionales if, if-else, if-anidados
#! Oeradores de control > < >= <= == != 
#! Operadores logicos and or ^ not

numero = 0
# if numero == 10:
#     print('el numero es 10')
# print('fuera del bloque')


# if numero == 10:
#     print('el numero es 10')
# else:
#     print('no es 10')
# print('fuera del bloque')

if numero > 0:
    print('el numero es positivo')
elif numero < 0:
    print('es numero es negativo')
else:
    print('es 0')


#! Bucles finitos (for) condicionados (while)

# numero = 0 
# while numero < 10:
#     print(numero)
#     numero += 1 # numero = numero + 1

# for i in range(10):
#     print('valor', i)

#! COMPLETAR FOR

#! funciones   (parametros variables y valor) --> primitivos valor | no primitivo referencia
def suma_resta(num1, num2):
    num1 = 100
    return num1 + num2

suma = suma_resta(5, 9)
print('la suma es:', suma)


#! Estructuras de datos variable, array, list, tuple, dic, class

# lista_num = [0] * 5
lista_num = []
lista_num.append(1)
lista_num[0] = 3
lista_num.append(10)
lista_num.append(5)
lista_num.insert(1, 4)
lista_num.insert(7, 10)
# print(lista_num)
# print(lista_num.sort(reverse=True))
# print(lista_num.pop())
# print(lista_num)

def mi_funcion_prueba(lista):
    lista.append(7)
    lista.append(90)
    lista[0] = 49


lista_test = [1, 7, 2, 33, 99]
lista_test.insert(3, 99)
# mi_funcion_prueba(lista_test)
# print(lista_test)
# print(len(lista_test))

# for i in range(len(lista_test)):
#     print('valor', lista_test[i])
# print()
# for numero in lista_test:
#     print(numero)

dic = {'1': 'hola', '2': 'chau', 0: 'asdsad'} #! key -> value
# dic['3'] = 49

# print(dic.get('7'))

# for key, value in dic.items():
#     print(key, value)

#! MODULOS -> librerias

# import mi_libreria
from mi_libreria import suma, resta
import mi_libreria as ml

print(suma(1, 1))
print(resta(1, 1))

print(ml.producto(2, 2))

from math import factorial

print(factorial(5))