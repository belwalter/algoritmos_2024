


class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert_node(self, value):
        def __insert(root, value):
            if root is None:
                return BinaryTree.__Node(value)
            elif value < root.value:
                root.left = __insert(root.left, value)
            else:
                root.right = __insert(root.right, value)
            return root

        self.root = __insert(self.root, value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    # print('lo encontre')
                    return root
                elif key < root.value:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, key)
            # else:
            #     print('no hay nada')
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                # a = input()
                # print(f'izquierda de {root.value}')
                __preorden(root.left)
                # print(f'derecha de {root.value}')
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                print('seguir buscando nodo par remplazar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    if root.left is None:
                        # print('a la izquierda no hay nada')
                        return root.right, value_delete
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        return root, value_delete
                
            return root, value_delete

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, value)
        return delete_value

tree = BinaryTree()

tree.insert_node(19)
tree.insert_node(7)
tree.insert_node(31)
tree.insert_node(11)
tree.insert_node(10)
tree.insert_node(45)
tree.insert_node(22)
tree.insert_node(27)

# pos = tree.search(27)
# if pos:
#     print('lo encontre', pos.value)
# else:
#     print('no esta')

tree.delete_node(7)
tree.delete_node(11)
tree.delete_node(31)
# tree.delete_node(27)
# tree.delete_node(45)
# tree.delete_node(22)
# tree.delete_node(19)
# tree.delete_node(10)
# tree.insert_node(27)

print(tree.delete_node(100))
tree.preorden()
