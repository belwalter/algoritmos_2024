
from grafo import Graph


letras = ['A', 'B', 'C', 'F', 'X', 'Z', 'T']


grafo = Graph()
for letra in letras:
    nodo = {
        'value': letra,
        'aristas': [],
        }
    grafo.insert_vertice(letra)



grafo.show_graph()

grafo.insert_arista('A', 'F', 23)
grafo.insert_arista('A', 'X', 11)
grafo.insert_arista('A', 'Z', 18)
grafo.insert_arista('F', 'C', 5)
grafo.insert_arista('X', 'T', 12)
grafo.insert_arista('Z', 'X', 10)
grafo.insert_arista('Z', 'F', 10)

# A F C X T Z
# A F X Z C T

grafo.show_graph()
# delete_value = grafo.delete_arista('A', 'X')
# print(delete_value)
# grafo.delete_vertice('X')
# grafo.show_graph()

# grafo.mark_as_not_visited()
# print('primero')
# grafo.deep_show('Z')
# print('segundo')
# grafo.deep_show('Z')
grafo.amplitude_show('Z')
