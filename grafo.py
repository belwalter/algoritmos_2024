from cola import Queue

class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print()
        print("nodos")
        for index, nodo in enumerate(self.elements):
            print(nodo['value'])
            print(f"    aristas")
            for second_index, second_element in enumerate(nodo['aristas']):
                print(f'    destino {second_element['value']} peso: {second_element['peso']}')
        print()

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index

    def search_arista(self, vertice_value, value):
        pos_origen = self.search(vertice_value)
        if pos_origen is not None:
            for index, element in enumerate(self.elements[pos_origen]['aristas']):
                if element['value'] == value:
                    return pos_origen, index

    def insert_vertice(self, value):
        nodo = {
        'value': value,
        'aristas': [],
        'visitado': False,
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            # print(origen, destino)
            arista = {
                'value': destino,
                'peso': peso
            }
            self.elements[pos_origen]['aristas'].append(arista)
    
    def delete_arista(self, origen, destino):
        result = self.search_arista(origen, destino)
        if result:
            pos_vertice, pos_arista = result
            value = self.elements[pos_vertice]['aristas'].pop(pos_arista)
            return value
    
    def delete_vertice(self, value):
        pos_vertice = self.search(value)
        if pos_vertice is not None:
            delete_value = self.elements.pop(pos_vertice)
            for nodo in self.elements:
                self.delete_arista(nodo['value'], value)
            return delete_value
    
    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False

    def deep_show(self, origin):
        def __deep_show(graph, origin):
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    print(graph.elements[pos_vertice]['value'])
                    adyacentes = graph.elements[pos_vertice]['aristas']
                    for adyacente in adyacentes:
                        __deep_show(graph, adyacente['value'])
        
        self.mark_as_not_visited()
        __deep_show(self, origin)

    def amplitude_show(self, origin):
        self.mark_as_not_visited()
        cola = Queue()
        pos_vertice = self.search(origin)
        if pos_vertice is not None:
            if not self.elements[pos_vertice]['visitado']:
                cola.arrive(self.elements[pos_vertice])
                while cola.size() > 0:
                    nodo = cola.attention()
                    nodo['visitado'] = True
                    print(nodo['value'])
                    adyacentes = nodo['aristas']
                    for adyacente in adyacentes:
                        pos_adyaecnte = self.search(adyacente['value'])
                        if not self.elements[pos_adyaecnte]['visitado']:
                            cola.arrive(self.elements[pos_adyaecnte])
