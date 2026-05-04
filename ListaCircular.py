import NodoCircular 

class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def josephus_modificado(self, m):
        if self.head is None:
            return
        current = self.head
        prev= self.head

        while prev.next is not self.head:
            prev = prev.next
        
        while current.next is not current:
            c = 1
            while c < m:
                prev = current
                current = current.next
                c +=1
            
            eliminado = current.data
            prev.next = current.next
            current = current.next

            if eliminado % 5 == 0:
                prev = current 
                current = current.next

