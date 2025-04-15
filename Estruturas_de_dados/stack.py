from node import Node

# Importante sabermos inserir na pilha
# remover na pilha
# observar o topo da pilha
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        # Método que insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        # remove um elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node
        raise IndexError('The stack is empty')


    def peek(self):
        # retorna o topo da pilha sem removê-lo
        if self._size > 0:
            return self.top.data
        raise IndexError('The stack is empty')


    def __len__(self):
        return self._size


    def __repr__(self):
        r = ''
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + '\n'
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()
    

pilha = Stack()
pilha.push(5)
pilha.push(2)
pilha.push(4)
pilha.push(7)
print(pilha)