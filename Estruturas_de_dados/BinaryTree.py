# Classe do nó de árvore
class Tnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


# Classe da árvore binária
class BinaryTree:
    # Essa função inicializa a classe, criando uma raíz que pode ser Nulo, ou ser o valor digitado pelo usuário
    def __init__(self, data=None):
        node = Tnode(data)
        if node:
            self.root = node
        else:
            self.root = None

    # Percurso em pós ordem
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        
        if node.left:
            self.postorder_traversal(node.left)

        if node.right:
            self.postorder_traversal(node.right)

        print(node)


            
tree = BinaryTree()
node1 = Tnode(5)
node2 = Tnode(3)
node3 = Tnode(6)
node4 = Tnode(9)
node5 = Tnode(7)

tree.root = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

tree.postorder_traversal() # Printa 9 - 7 - 3 - 6 - 5
