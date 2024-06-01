class Nodo:
    def __init__(self, posicionX, posicionY, simbolo, tamano):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.simbolo = simbolo
        self.tamano = tamano
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def vacio(self):
        return self.tamano == 0
    
    def agregar(self, posicionX, posicionY, simbolo):
        nuevo = Nodo(posicionX, posicionY, simbolo, self.tamano)

        if(self.tamano == 0):
            self.primero = nuevo
        else:
            self.ultimo.siguiente = nuevo
        
        self.ultimo = nuevo
        self.tamano += 1

    def tamanoCola(self):
        return self.tamano
    
    def imprimir(self):
        temporal = self.primero
        while(temporal):
            print("("+str(temporal.posicionX)+"-"+str(temporal.posicionY)+")"+temporal.simbolo)
            temporal=temporal.siguiente

    def posicion(self, pos):
        temporal = self.primero
        for i in range(pos):
            if (i > temporal.tamano):
                temporal = None
            else:
                temporal=temporal.siguiente
        #print(temporal.simbolo)
        return temporal
    
    def prueba(self, x, y, turno):
        temporal = self.primero
        retorno = None
        while temporal:
            if(x==temporal.posicionX) and (y==temporal.posicionY) and (turno == temporal.simbolo):
                retorno = temporal.siguiente 
                break
            temporal = temporal.siguiente
        return retorno
                



