


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
                print('crear nodo')
                return BinaryTree.__Node(value)
            elif value < root.value:
                print('insertar izquierda')
                root.left = __insert(root.left, value)
            else:
                print('insertar derecha')
                root.right = __insert(root.right, value)
            return root

        self.root = __insert(self.root, value)



tree = BinaryTree()
tree.insert_node(19)
tree.insert_node(7)
tree.insert_node(31)
tree.insert_node(11)

print(tree.root.value, tree.root.left, tree.root.right)
