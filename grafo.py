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