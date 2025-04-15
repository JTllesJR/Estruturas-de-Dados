from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        '''Método que insere um elemento na ultima posição da lista'''
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)

        self._size += 1

    def __len__(self):
        '''Método para usar a função len()'''
        return self._size
    
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
            
        if pointer:
            return pointer.data
        else:
            raise IndexError('list index out of range')
        

    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
            
        if pointer:
            pointer.data = elem
        else:
            raise IndexError('list index out of range')


        def index(self, elem):
            '''Retorna o índice do elemento na lista'''
            pointer = self.head
            i = 0
            while pointer:
                if pointer.data == elem:
                    return i
                pointer = pointer.next
                i += 1

            raise ValueError(f'{elem} is not in list')

    def __repr__(self):
        r = ''
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + '->'
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()

lista = LinkedList()
lista.append(5)
lista.append(7)
lista.append(9)
print(lista[5])