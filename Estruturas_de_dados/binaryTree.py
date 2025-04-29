class Tnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
class BinaryTree:
    # Essa função inicializa a classe, criando uma raíz que pode ser Nulo, ou ser o valor digitado pelo usuário
    def __init__(self, data=None):
        node = Tnode(data)
        if node:
            self.root = node
        else:
            self.root = None


    '''
    Esse método tem como objetivo inserir um valor na árvore. Caso a árvore esteja vazia, o valor seria inserido na raíz.
    Caso não esteja, o método auxiliar _inserir vai encontrar recursivamente o local certo para inserir o novo valor
    '''
    def inserir(self, value):
        if self.root is None:
            self.root = Tnode(value)
        else:
             self._inserir(self.raiz, value)

    
    def _inserir(self, atual, valor):
        if valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = Tnode(valor)
            else:
                self._inserir(atual.esquerda, valor)
        else:
            if atual.direita is None:
                atual.direita = Tnode(valor)
            else:
                self._inserir(atual.direita, valor)


    def em_ordem(self, node):
        if node is not None:
            self.em_ordem(Tnode.esquerda)
            print(Tnode.valor)
            self.em_ordem(Tnode.direita)


tree = BinaryTree()
n1 = Tnode(5)
tree.root = n1
