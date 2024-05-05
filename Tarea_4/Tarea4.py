import csv
from graphviz import Digraph

class Menu:
    def __init__(self):
        self.matriz= Matriz()
    
    def menuOption(self):
        menu= '''
            ***** Menú *****
            1.- Ingresar Ruta de Archivo
            2.- Ver Graphiviz
            3.- Salir         
            '''
        option=''
        while(option!= '3'):
            print(menu) 
            option= input('Ingrese el número de la opción a utilizar: ')
            self.selectedOption(option)

    def selectedOption(self, option):
        
        if option == '1':
            name= input('Ingrese Direccion del archivo: ')
            self.matriz.lectura(name)
        elif option == '2':
            self.matriz.recorrido()
            self.matriz.recorridoMatriz()
            self.matriz.graphviz()

class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.siguiente = None
        self.abajo = None

class Matriz:
    def __init__(self):
        self.primeraC=None
        self.primeraF=None
        self.ultimaC=None
        self.ultinaF=None
        self.temporalC=None
        self.temporalF=None

        self.notes=''
        self.contador=0
        self.concat=''

        self.dot = Digraph(comment="Matriz dispersa")

    def lectura(self, direccion):
        with open(direccion, newline='') as f:
            data= csv.reader(f, delimiter=';')
            self.notes= list(data)

    def recorrido(self):
        for i in range(1, len(self.notes)):
            lista1=self.notes[i]

            for j in range(len(lista1)):
                lista2=lista1[j] #separa en listas
                lista3=lista2.split(",")#separa por comas

                for k in range(len(lista3)): 
                    if(lista3[k]!='0'):
                        nuevo=Nodo(lista3[k])

                        if(k==0):

                            if(self.contador==0):
                                self.primeraF=nuevo
                                self.ultinaF=nuevo
                                self.temporalF=nuevo 
                                self.primeraC=nuevo
                                self.temporalC=nuevo
                                self.ultimaC=nuevo
                                nom=str(k)+str(self.contador)
                                self.dot.node(str(lista3[k]), id=nom)
                                self.concat=self.concat+lista3[k]
                                
                            if(self.contador!=0):
                                self.ultinaF=nuevo
                                self.temporalF.abajo=self.ultinaF
                                self.temporalF=self.ultinaF

                                self.primeraC=self.ultinaF
                                self.temporalC=self.primeraC
                                
                                self.concat=self.concat+'\n'+"V"+'\n'
                                self.concat=self.concat+lista3[k]
                        else:
                            self.ultimaC=nuevo
                            self.temporalC.siguiente=self.ultimaC
                            self.temporalC= self.ultimaC
                            self.concat=self.concat+"->"+lista3[k]
                            nom1=str(k)+str(self.contador)
                            nom2=str(k-1)+str(self.contador)
                            self.dot.edge(nom2, nom1, dir="back")

                self.contador=self.contador+1            

  

    def recorridoMatriz(self):
        print(self.concat)


    
    def graphviz(self):
        self.dot.render("Imagen_Matriz", format="png", cleanup=True)
        print("Se ha generado el gráfico")
        print()
   

mostrar=Menu()
mostrar.menuOption()
