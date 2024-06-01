import cola
from graphviz import Digraph
##queue = cola.Cola()
class Nodo:
    def __init__(self, ponderacion, ganador, queue):
        self.ponderacion = ponderacion
        self.ganador = ganador
        self.queue = queue
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def vacio(self):
        return self.tamano == 0
    
    def agregarInicio(self, ponderacion, ganador, queue):
        nuevo = Nodo(ponderacion, ganador, queue)

        if (self.vacio()):
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo

        self.tamano += 1

    def tamanioLista(self):
        return self.tamano
    
    def imprimir(self):
        temporal = self.primero

        while temporal:
            print(temporal.ganador+"||"+str(temporal.queue.imprimir())+"||"+str(temporal.ponderacion))
            temporal = temporal.siguiente

    def obtener(self):
        temporal = self.primero
        while temporal:
            #print(temporal.ganador+"||"+str(temporal.ponderacion))
            if(temporal.ganador == "o"):
                pass
            temporal.queue.imprimir()
            temporal = temporal.siguiente

    def obtenerMinimo(self):
        if (self.vacio()):
            return None
        minPonde = self.primero.ponderacion
        retornar = self.primero
        temporal = self.primero.siguiente

        while temporal:
            if temporal.ponderacion < minPonde:
                minPonde = temporal.ponderacion
                retornar = temporal
            temporal = temporal.siguiente
        return retornar

        
    def pintar(self):
        dot = Digraph(comment="Lista Doblemente Enlazada")
        temporal = self.primero
        i=0
        while temporal:
            with dot.subgraph(name='cluster_'+str(i)) as c:
                c.attr(style='filled', color='lightgrey')
                c.node_attr.update(style='filled', color='white')

                temporalQ = temporal.queue.primero
                j=0
                while(temporalQ):
                    textoQ = "|"+str(temporalQ.posicionX)+"-"+str(temporalQ.posicionY)+"|"+temporalQ.simbolo
                    nodoNombre= 'sub'+str(i)+str(j)
                    c.node(nodoNombre, label=textoQ)
                    nombre ='sub'+str(i)+str(j)
                    nombre2= 'sub'+str(i)+str(j+1)
                    c.edge(nombre, nombre2)

                    j = j+1
                    temporalQ=temporalQ.siguiente

                nameTitulo="Ganador: "+temporal.ganador+" | Ponderacion: "+str(temporal.ponderacion)
                c.attr(label=nameTitulo)
            i = i+1
            temporal = temporal.siguiente

        #print(dot)
        with open('grafo.dot', 'w') as file:
            file.write(str(dot))
        dot.render("Imagen_Lista", format="png", cleanup=True)
        print("Se ha generado el gráfico")




    