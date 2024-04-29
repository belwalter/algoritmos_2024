

# lista_de_elementos = [1, 20, 5, 67, 3, 4, -1]

# #! insertar con posicion
# lista_de_elementos.insert(2, 99)
# #! insertar sin posicion
# lista_de_elementos.append(123)

# #! eliminar un elemento de la lista (suponiendo valores unicos y dato simple)
# try:
#     lista_de_elementos.remove(101)
# except ValueError:
#     print('el elemento a eliminar no esta en la lista')
# if 67 in lista_de_elementos:
#     print('eliminar elemento')
#     lista_de_elementos.remove(67)
# else:
#     print('el elemento a eliminar no esta en la lista')

# #! tamanio
# print(len(lista_de_elementos))

# #! ordenar elementos simples
# lista_de_elementos.sort()

# #! busqueda elementos simples
# try:
#     print('posicion', lista_de_elementos.index(20))
# except ValueError:
#     print('el elemento que busca no esta en la lista')

# #! barrido
# print("Listado")
# for elemento in lista_de_elementos:
#     print(elemento)

personajes_star_wars = [
    {'nombre': 'Luke Skywalker', 'especie': 'Humano', 'altura': 172},
    {'nombre': 'Princesa Leia', 'especie': 'Humano', 'altura': 150},
    {'nombre': 'Han Solo', 'especie': 'Humano', 'altura': 180},
    {'nombre': 'Darth Vader', 'especie': 'Humano', 'altura': 202},
    {'nombre': 'Yoda', 'especie': 'Desconocida', 'altura': 66},
    {'nombre': 'Obi-Wan Kenobi', 'especie': 'Humano', 'altura': 182},
    {'nombre': 'Chewbacca', 'especie': 'Wookiee', 'altura': 228},
    {'nombre': 'R2-D2', 'especie': 'Droide', 'altura': 96},
    {'nombre': 'C-3PO', 'especie': 'Droide', 'altura': 167},
    {'nombre': 'Padmé Amidala', 'especie': 'Humano', 'altura': 165}
]

nuevo_personaje = {'nombre': 'Boba Fett', 'especie': 'Humano', 'altura': 178}
#! insertar con posicion
personajes_star_wars.insert(8, nuevo_personaje)
#! insertar sin posicion
nuevo_personaje_2 = {'nombre': 'Mace Windu', 'especie': 'Humano', 'altura': 190}
personajes_star_wars.append(nuevo_personaje_2)

#! tamanio
print(len(personajes_star_wars))

#! criterios de orden
def by_name(item):
    return item['nombre']

def by_hegiht(item):
    return item['altura']

#! ordenar elementos simples
personajes_star_wars.sort(key=by_hegiht)

#! busqueda elementos simples
try:
    print('posicion', personajes_star_wars.index('Yoda'))
except ValueError:
    print('el elemento que busca no esta en la lista')

#! barrido
print("Listado")
for elemento in personajes_star_wars:
    print(elemento['nombre'], elemento['especie'], elemento['altura'])