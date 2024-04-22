

class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def attention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None
    
    def move_to_end(self):
        element = self.attention()
        if element is not None:
            self.arrive(element)



# cola_1 = Queue()

# cola_1.arrive(1)
# cola_1.arrive(2)
# cola_1.arrive(3)
# cola_1.arrive(4)
# cola_1.arrive(5)
# cola_1.attention()
# cola_1.attention()
# print(cola_1.size())
# print(cola_1.on_front())
# cola_1.move_to_end()
# cola_1.move_to_end()
# print()
# for i in range(cola_1.size()):
#     print(cola_1.on_front())
#     cola_1.move_to_end()
# print()
# print(cola_1.size())