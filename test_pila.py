from pila import Stack
from random import randint

pila = Stack()
pila_aux = Stack()

for i in range(10):
    pila.push(randint(1, 99))


while pila.size() > 0:
    data = pila.pop()
    if data % 2 == 0:
        pila_aux.push(data)
    
while pila_aux.size() > 0:
    pila.push(pila_aux.pop())


print()
print(pila.size())


class Peli:

    def __init__(self, nombre, anio, traje):
        self.nombre = nombre
        self.anio = anio
        self.traje = traje

    def __str__(self):
        return f'{self.nombre} - {self.anio} - {self.traje}'


peliculas = [
    Peli('avengers', 2000, 'Mark V'),
    Peli('avengers Era de Ultron', 2006, 'Mark VIII'),
]


for pelicula in peliculas:
    pila_aux.push(pelicula)

while pila_aux.size() > 0:
    print(pila_aux.pop().traje)