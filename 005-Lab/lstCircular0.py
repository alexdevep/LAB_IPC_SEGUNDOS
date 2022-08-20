class Node(object):
    # Crear una clase de nodo
    def __init__(self, data):
        self.data = data
        self.next = None
 
class circular_simple(object):
    # Crear una clase que cree una lista circular vinculada
    
    def __init__(self):
        self.head = None
 
    def estaVacia(self):
        # Determine si la lista circular está vacía
        return self.head is None
 
    def agregarInicio(self, data):
        # Agregar un nodo en la cabeza
        node = Node(data)
        if self.estaVacia():
            self.head = node
            node.next = self.head
        else:
            aux = self.head
            # Mueva el puntero al nodo de cola
            while aux.next is not self.head:
                aux = aux.next
            # El nodo de cola apunta al nuevo nodo
            aux.next = node
            # El nuevo nodo apunta al nodo principal original
            node.next = self.head
            # Luego dele el título del nodo principal al nuevo nodo
            self.head = node
 
    def agregarFinal(self, data):
        # Agregar un nodo al final
        node = Node(data)
        if self.estaVacia():
            self.head = node
            node.next = self.head
        else:
            aux = self.head
            # Mueve el puntero al final
            while aux.next is not self.head:
                aux = aux.next
            # El nodo de cola apunta al nuevo nodo
            aux.next = node
            # El nuevo nodo apunta al nodo principal
            node.next = self.head
 
    def recorrer(self):
        # Recorriendo la lista vinculada
        if self.estaVacia():
            return
        aux = self.head
        print(aux.data)
        while aux.next != self.head:
            aux = aux.next
            print(aux.data)


 
lists = circular_simple()
lists.agregarFinal(2)
lists.agregarInicio(1)
lists.agregarInicio(0)
lists.agregarFinal(3)
lists.recorrer()