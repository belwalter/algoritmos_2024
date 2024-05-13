

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

# personajes_star_wars = [
#     {'nombre': 'Luke Skywalker', 'especie': 'Humano', 'altura': 172},
#     {'nombre': 'Princesa Leia', 'especie': 'Humano', 'altura': 150},
#     {'nombre': 'Han Solo', 'especie': 'Humano', 'altura': 180},
#     {'nombre': 'Darth Vader', 'especie': 'Humano', 'altura': 202},
#     {'nombre': 'Yoda', 'especie': 'Desconocida', 'altura': 66},
#     {'nombre': 'Obi-Wan Kenobi', 'especie': 'Humano', 'altura': 182},
#     {'nombre': 'Chewbacca', 'especie': 'Wookiee', 'altura': 228},
#     {'nombre': 'R2-D2', 'especie': 'Droide', 'altura': 96},
#     {'nombre': 'C-3PO', 'especie': 'Droide', 'altura': 167},
#     {'nombre': 'Padmé Amidala', 'especie': 'Humano', 'altura': 165}
# ]

# nuevo_personaje = {'nombre': 'Boba Fett', 'especie': 'Humano', 'altura': 178}
#! insertar con posicion
# personajes_star_wars.insert(8, nuevo_personaje)
#! insertar sin posicion
# nuevo_personaje_2 = {'nombre': 'Mace Windu', 'especie': 'Humano', 'altura': 190}
# personajes_star_wars.append(nuevo_personaje_2)

#! tamanio
# print(len(personajes_star_wars))

#! criterios de orden
def by_name(item):
    return item['nombre']

def by_hegiht(item):
    return item['altura']

#! ordenar elementos simples
# personajes_star_wars.sort(key=by_name)

#! busqueda elementos simples
# buscado = 'Yoda'
# criterio = 'nombre'

def search(list_values, criterio, value):
    for index, personaje in enumerate(list_values):
        if personaje[criterio] == value:
            return index

# print(f'Yoda esta en la posicion {search(personajes_star_wars, criterio, buscado)}')

#! eliminar un elemento de la lista
def remove(list_values, criterio, value):
    index = search(list_values, criterio, value)
    if index is not None:
        return list_values.pop(index)

# eliminar = 'R2-D2'
# result_delete = remove(personajes_star_wars, criterio, eliminar)
# print(f'Eliminar {eliminar} resultado: {result_delete}')
#! barrido
def show_list(title, list_values):
    print()
    print(f"{title}")
    for index, elemento in enumerate(list_values):
        print(index, elemento)
    print()


super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."
  }
]
