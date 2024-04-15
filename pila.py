
class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)

from random import randint

pila = Stack()
pila_aux = Stack()

for i in range(10):
    pila.push(randint(1, 99))

print(pila.on_top())
print(pila.size())
print()

#! LISTAR
while pila.size() > 0:
    data = pila.pop()
    print(data)
    pila_aux.push(data)

#! RECONSTRUCCION
while pila_aux.size() > 0:
    pila.push(pila_aux.pop())

print()
print(pila.size())
print(pila.on_top())

