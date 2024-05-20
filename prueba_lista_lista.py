from lista import by_name, show_list, search, show_list_list, by_temp, remove

estaciones = [
    {'nombre': 'A', 'state': 'Entre rios', 'id': 123},
    {'nombre': 'Z', 'state': 'Salta', 'id': 456},
    {'nombre': 'G', 'state': 'Mendoza', 'id': 789},
    {'nombre': 'C', 'state': 'Misiones', 'id': 101},
    {'nombre': 'T', 'state': 'Neuquen', 'id': 112},
]

lista_estaciones = []

mediciones = [
    {'temp': 25, 'hum': 80, 'fecha': '20-5-2024', 'station_id': 789},
    {'temp': 25, 'hum': 80, 'fecha': '19-5-2024', 'station_id': 123},
    {'temp': 30, 'hum': 75, 'fecha': '17-5-2024', 'station_id': 456},
    {'temp': 30, 'hum': 75, 'fecha': '19-5-2024', 'station_id': 456},
    {'temp': 25, 'hum': 80, 'fecha': '20-5-2024', 'station_id': 456},
]

for estacion in estaciones:
    estacion.update({'sublist': []})
    lista_estaciones.append(estacion)

# lista_estaciones.sort(key=by_name)

for medicion in mediciones:
    pos = search(lista_estaciones, 'id', medicion['station_id'])
    if pos is not None:
        lista_estaciones[pos]['sublist'].append(medicion)
    else:
        print('la estacion no esta en la lista')

# show_list_list('Lista de Estaciones', 'Lista de Mediciones', lista_estaciones)

# pos = search(lista_estaciones, 'id', 456)
# if pos is not None:
#     remove(lista_estaciones[pos]['sublist'], 'fecha', '20-5-2024')
#     print('medicion eliminada')
# else:
#     print('la estacion no esta en la lista')

# pos = search(lista_estaciones, 'id', 456)
# if pos is not None:
#     pos_med = search(lista_estaciones[pos]['sublist'], 'fecha', '17-5-2024')
#     if pos_med is not None:
#         print(f"esta {lista_estaciones[pos]['sublist'][pos_med]}")
#     else:
#         print('no esta')

# else:
#     print('la estacion no esta en la lista')

# pos = search(lista_estaciones, 'id', 456)
# if pos is not None:
#     pos_med = search(lista_estaciones[pos]['sublist'], 'fecha', '17-5-2024')
#     if pos_med is not None:
#         lista_estaciones[pos]['sublist'][pos_med]['temp'] = 27
#     else:
#         print('no esta')
# else:
#     print('la estacion no esta en la lista')

new_medicion = {'temp': 40, 'hum': 100, 'fecha': '10-5-2024', 'station_id': 456}

pos = search(lista_estaciones, 'id', 456)
if pos is not None:
    lista_estaciones[pos]['sublist'].insert(1, new_medicion)
else:
    print('la estacion no esta en la lista')

pos = search(lista_estaciones, 'id', 456)
if pos is not None:
    lista_estaciones[pos]['sublist'].sort(key=by_temp)
    for medicion in lista_estaciones[pos]['sublist']:
        print(medicion)
else:
    print('la estacion no esta en la lista')