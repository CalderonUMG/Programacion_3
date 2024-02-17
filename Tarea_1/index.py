from graphviz import Digraph

##Clase menu
class Menu:
    def __init__(self):
        self.lista= LDE()
    
    def menuOption(self):
        menu= '''
            ***** Menú *****
            1.- Insertar al principio
            2.- Insertar al final
            3.- Eliminar por valor
            4.- Mostrar lista
            5.- Salir         
            '''
        option=''
        while(option!= '5'):
            print(menu) 
            option= input('Ingrese el número de la opción a utilizar: ')
            self.selectedOption(option)

    def selectedOption(self, option):
        
        if option == '1':
            name= input('Ingrese Nombre: ')
            lastName= input('Ingrese Apellido: ')
            carnet= input('Ingrese Carnet: ')
            self.lista.insertBeginning(name, lastName, carnet)
        elif option == '2':
            name= input('Ingrese Nombre: ')
            lastName= input('Ingrese Apellido: ')
            carnet= input('Ingrese Carnet: ')
            self.lista.insertBeginning(name, lastName, carnet)
        elif option == '3':
            carnet= input('Ingrese Carnet para Eliminar: ')
            self.lista.deleteByValue(carnet)
        elif option == '4':
            self.lista.showList()
            self.lista.graphviz()



##Clase Nodo
class Nodo:
    def __init__(self,nombre, apellido, carnet):
        self.nombre=nombre
        self.apellido=apellido
        self.carnet=carnet
        self.siguiente = None
        self.anterior = None

##Clase lista doblemente enlazada
class LDE:

    def __init__(self):
        self.primer_nodo = None
        self.ultimo_nodo = None

    def insertBeginning(self,name, lastName, carnet):
        newNodo= Nodo(name, lastName, carnet)

        if self.checkEmpty():
            self.primer_nodo = newNodo
            self.ultimo_nodo = newNodo
        else:
            newNodo.anterior=self.primer_nodo
            self.primer_nodo.siguiente=newNodo
            self.primer_nodo=newNodo


    def insertEnd(self, name, lastName, carnet):
        newNodo= Nodo(name, lastName, carnet)

        if self.checkEmpty():
            self.primer_nodo = newNodo
            self.ultimo_nodo = newNodo
        else:
            newNodo.anterior=self.ultimo_nodo
            self.ultimo_nodo.siguiente=newNodo
            self.ultimo_nodo=newNodo

    def showList(self):
        temporal = self.primer_nodo

        print("None <- ", end="")
        while(temporal != self.ultimo_nodo):
            print(temporal.carnet+" <-> ", end="")
            temporal=temporal.anterior
            
        print(self.ultimo_nodo.carnet+" -> None", end="")
        print()

    def checkEmpty(self):
        if self.primer_nodo==None and self.ultimo_nodo == None:
            empty=True
        else:
            empty=False
        
        return empty
    
    def deleteByValue(self, carnet):
        temporal = self.primer_nodo

        while(temporal != self.ultimo_nodo):
            if carnet == temporal.carnet:
                if temporal == self.primer_nodo:
                    self.primer_nodo = temporal.siguiente
                if temporal == self.ultimo_nodo:
                    self.ultimo_nodo == temporal.anterior
                else:
                    temporal.anterior.siguiente=temporal.anterior
                    temporal.siguiente.anterior = temporal.anterior
            
            temporal=temporal.anterior

        if temporal == self.ultimo_nodo:
                    self.ultimo_nodo = temporal.anterior
    
    def graphviz(self):
        dot = Digraph(comment="Lista Doblemente Enlazada")

        temporal = self.primer_nodo
        dot.node(str(temporal.carnet))
        while(temporal != self.ultimo_nodo):
            if temporal.anterior:
                dot.edge(str(temporal.anterior.carnet), str(temporal.carnet), dir="back")
                dot.edge(str(temporal.carnet), str(temporal.anterior.carnet), dir="back")
            
            temporal=temporal.anterior
        
        dot.render("Imagen_Lista", format="png", cleanup=True)
        print("Se ha generado el gráfico")
        print()
    

mostrar=Menu()
mostrar.menuOption()