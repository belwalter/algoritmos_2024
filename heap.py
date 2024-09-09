

class Heap():

    def __init__(self):
        self.elements = []
    
    def add(self, value):
        self.elements.append(value)
        self.flotar(len(self.elements)-1)

    def remove(self):
        if len(self.elements) > 0:
            self.intercambio(0, len(self.elements)-1)
            value = self.elements.pop()
            self.hundir(0)
            return value
        else:
            return None

    def intercambio(self, index_1, index_2):
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def flotar(self, index):
        print('llamada flotar')
        padre = (index-1) // 2
        while index > 0 and self.elements[index] > self.elements[padre]:
            print('flotandoooo')
            self.intercambio(index, padre)
            index = padre
            padre = (index-1) // 2

    def hundir(self, index):
        print('llamar hundir')
        hijo_izq = (index * 2) + 1
        control = True
        while control and hijo_izq < len(self.elements)-1:
            print('intentando hundir')
            hijo_der = (index * 2) + 2
            mayor = hijo_izq
            if hijo_der < len(self.elements)-1:
                if self.elements[hijo_der] > self.elements[hijo_izq]:
                    mayor = hijo_der
            if self.elements[index] < self.elements[mayor]:
                self.intercambio(index, mayor)
                index = mayor
                hijo_izq = (index * 2) + 1
            else:
                control = False


h = Heap()
h.add(17)
h.add(3)
h.add(20)
h.add(1)
h.add(15)
h.add(30)
print(h.elements)
a = input()
while len(h.elements) > 0:
    print(h.elements, h.remove())
    a = input()