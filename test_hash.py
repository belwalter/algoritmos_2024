

# def bernstain(cadena):
#     h = 0
#     for caracter in cadena:
#         h = h * 33 + ord(caracter)
#     return h


# print(bernstain('hole') % 13)
from random import randint, choice


def hash_legion(value):
    return trooper[:2]

def hash_numerica(value):
    return trooper[-3:]


legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

tabla_legiones = {}
table_numerica = {}

for legion in legiones:
    tabla_legiones[legion] = []

for i in range(0, 2000):
    trooper = f'{choice(legiones)}-{randint(1000, 9999)}'
    clave = hash_numerica(trooper)
    if clave not in table_numerica:
        table_numerica[clave] = []

    table_numerica[clave].append(trooper)
    tabla_legiones[hash_legion(trooper)].append(trooper)


#! C FN-2187 traitor
list_187 = table_numerica.get('187', [])
if 'FN-2187' in list_187:
    pos_fn_2187 = list_187.index('FN-2187')
    if pos_fn_2187 > -1:
        print(f'esta en la posicion {pos_fn_2187}')
else:
    print('no esta')
print(len(list_187))
print()

#! D mission_assault 781 mission_explore 537

# mission_assault = table_numerica.get('781', [])
# print('Stromtroopers para mision de asalto')
# for index, trooper in enumerate(mission_assault):
#     print(f'{index} - {trooper}')
# print()
# mission_explore = table_numerica.get('537', [])
# print('Stromtroopers para mision de exploración')
# for index, trooper in enumerate(mission_explore):
#     print(f'{index} - {trooper}')
# print()

#! E hoth CT endor TF
# mission_hoth = tabla_legiones.get('CT', [])
# print('Stromtroopers para mision a hoth')
# for index, trooper in enumerate(mission_hoth):
#     print(f'{index} - {trooper}')
# print()
# mission_endor = tabla_legiones.get('TF', [])
# print('Stromtroopers para mision a hoth')
# for index, trooper in enumerate(mission_endor):
#     print(f'{index} - {trooper}')
# print()