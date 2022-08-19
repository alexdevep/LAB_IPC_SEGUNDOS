
class Nodo():
    def __init__(self, valor, apuntador): 
        self.valor = valor
        self.apuntador = apuntador
        

class ListaSimple():
    Inicio = None

    Nodo2 = Nodo('BBB',None)

    Inicio.valor='AAA'
    Inicio.apuntador=Nodo2


List = [NODO1,NODO2,NODO3,NODO4]

for item in list:
    print(item)
    item.siguiente = item

