
from grafo import Graph


letras = ['R', 'F', 'X', 'Z', 'T']


grafo = Graph(dirigido=False)
for letra in letras:
    nodo = {
        'value': letra,
        'aristas': [],
        }
    grafo.insert_vertice(letra)



# grafo.show_graph()

grafo.insert_arista('X', 'Z', 9)
grafo.insert_arista('X', 'R', 5)
grafo.insert_arista('F', 'X', 2)
grafo.insert_arista('F', 'R', 2)
grafo.insert_arista('T', 'R', 8)
grafo.insert_arista('T', 'F', 3)
grafo.insert_arista('T', 'X', 6)
grafo.insert_arista('Z', 'R', 4)
# grafo.insert_arista('A', 'C', 55)

# A F C X T Z
# A F X Z C T

# grafo.show_graph()
# delete_value = grafo.delete_arista('A', 'C')
# print(delete_value)
# grafo.delete_vertice('X')
grafo.show_graph()

camino = grafo.dijkstra('R')
destino = 'T'
peso_total = None
camino_completo = []
while camino.size() > 0:
    value = camino.pop()
    if value[1][0] == destino:
        if peso_total is None:
            peso_total = value[0]
        camino_completo.append(value[1][0])
        destino = value[1][2]
camino_completo.reverse()
print(f'el camino mas corto es: {'-'.join(camino_completo)} con un costo de {peso_total}')


# print(grafo.exist_path('T', 'Z'))
# grafo.mark_as_not_visited()
# print('primero')
# grafo.deep_show('Z')
# print('segundo')
# grafo.deep_show('Z')
# grafo.amplitude_show('Z')
# grafo.show_graph()
