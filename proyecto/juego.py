import pygame, sys
import cola
import listaDoble
import random
import boton

class Totito():
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.SCREEN = pygame.display.set_mode((600, 600))
        self.propiedades = pygame.display.set_mode((600, 600))

        pygame.display.set_caption("Proyecto")
        self.turno='x'
        self.gameOver=False
        self.reloj=pygame.time.Clock()

        self.BG = pygame.image.load("static\Background.jpg")
        self.fondo = pygame.image.load('static\pantalla.png')
        self.equis = pygame.image.load('static\equis.png')
        self.circulo = pygame.image.load('static\circulo.png')
        self.propiedadesF = pygame.image.load("static\Background2.jpg")

        self.fondo = pygame.transform.scale(self.fondo, (600, 600))
        self.equis = pygame.transform.scale(self.equis, (110, 110))
        self.circulo = pygame.transform.scale(self.circulo, (105, 105))
        self.propiedadesF = pygame.transform.scale(self.propiedadesF, (600, 600))
        self.BG = pygame.transform.scale(self.BG, (600, 600))

        self.queue = cola.Cola()
        self.doubleList = listaDoble.ListaDoble()

        self.posicion =  [[(125,135),(250,135),(370,135)],
                        [(125,255),(250,255),(370,255)],
                        [(125,380),(250,380),(370,380)]]

        self.jugada = [['','',''],
                        ['','',''],
                        ['','','']]

    def graficar(self):
        self.screen.blit(self.fondo, (0,0))
        for f in range(3):
            for c in range(3):
                if self.jugada[f][c] == 'x':
                    self.pintarX(f,c)
                elif self.jugada[f][c] == 'o':
                    self.pintarO(f,c)

    def pintarX(self, fila, column):
        self.screen.blit(self.equis, self.posicion[fila][column])

    def pintarO(self, fila, column):
        self.screen.blit(self.circulo, self.posicion[fila][column])

    def verificar_ganador(self):
        for i in range(3):
            if self.jugada[i][0] == self.jugada[i][1] == self.jugada[i][2] != '':
                return True
            if self.jugada[0][i] == self.jugada[1][i] == self.jugada[2][i] != '':
                return True
        if self.jugada[0][0] == self.jugada[1][1] == self.jugada[2][2] != '':
                return True
        if self.jugada[0][2] == self.jugada[1][1] == self.jugada[2][0] != '':
            return True
        
        return False

    def iniciarJuego(self):
        self.queue = cola.Cola()
        self.turno = 'x'
        colAnt=0
        filaAnt=0
        turnoAnt=""
        while not self.gameOver:
            self.reloj.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    if(mousex >= 115 and mousex < 445) and (mousey >= 120 and mousey < 450):
                        fila = (mousey - 120) // 110
                        col = (mousex - 115) // 110

                        if self.jugada[fila][col] == '':
                            if self.turno == 'o':
                                #self.IA()
                                self.prueba(filaAnt,colAnt,turnoAnt)
                            else:
                                filaAnt=fila
                                colAnt=col
                                turnoAnt=self.turno
                                self.jugada[fila][col] = self.turno
                                self.queue.agregar(fila,col,self.turno)

                            fin = self.verificar_ganador()
                            if fin:
                                self.doubleList.agregarInicio(self.queue.tamanoCola(), self.turno, self.queue)
                                self.gameOver = True
                                self.menu_victoria(self.turno)
                            self.turno = 'o' if self.turno == 'x' else 'x'


            self.graficar()
            pygame.display.update()
        
    pygame.quit()

    def turnoRandom(self):
        aleatorioX = random.randint(0, 2)
        aleatorioY = random.randint(0, 2)
        
        if(self.jugada[aleatorioX][aleatorioY] == ""):
            self.jugada[aleatorioX][aleatorioY] = self.turno
            self.queue.agregar(aleatorioX,aleatorioY,self.turno)
        else:
            self.turnoRandom()

    def IA(self):
        if self.doubleList.tamanioLista() == 0:
            #self.turnoRandom()
            pass
        else:
            #self.doubleList.prueba(self.queue)
            #self.doubleList.obtenerMinimo()
            #self.prueba()
            pass
        self.turnoRandom()

    def prueba(self, x, y, turno):
        temporal = self.doubleList.primero
        if(self.doubleList.vacio()):
            self.turnoRandom()
        else:
            while temporal:
                if temporal.ganador == "o":
                    resultado = temporal.queue.prueba(x, y, turno)
                    if (resultado != None):
                        #print(resultado.simbolo)
                        self.jugada[resultado.posicionX][resultado.posicionY] = resultado.simbolo
                        self.queue.agregar(resultado.posicionX,resultado.posicionY,resultado.simbolo)
                        break
                else:
                    self.turnoRandom()
                    #break
                temporal = temporal.siguiente


    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("static\letra.ttf", size)

    def menu_victoria(self, ganador):
        while True:
            self.SCREEN.blit(self.BG, (0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(50).render("Ganador: "+ganador, True, "#872079")
            MENU_RECT = MENU_TEXT.get_rect(center=(290, 200))

            PLAY_BUTTON = boton.Button(image=pygame.image.load("static\select.png"), pos=(290, 300), 
                                text_input="MAIN MENU", font=self.get_font(25), base_color="#d7fcd4", hovering_color="White")
            
            
            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.menu_inicio()

            pygame.display.update()

    def menu_inicio(self):
        while True:
            self.SCREEN.blit(self.BG, (0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(50).render("MAIN MENU", True, "#872079")
            MENU_RECT = MENU_TEXT.get_rect(center=(295, 50))

            PLAY_BUTTON = boton.Button(image=pygame.image.load("static\select.png"), pos=(295, 200), 
                                text_input="PLAY", font=self.get_font(25), base_color="#d7fcd4", hovering_color="White")
            RECORD_BUTTON = boton.Button(image=pygame.image.load("static\select.png"), pos=(295, 300), 
                                text_input="HISTORIAL", font=self.get_font(25), base_color="#d7fcd4", hovering_color="White")
            INFORMATION_BUTTON = boton.Button(image=pygame.image.load("static\select.png"), pos=(295, 400), 
                                text_input="INFORMACIÓN", font=self.get_font(25), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = boton.Button(image=pygame.image.load("static\select.png"), pos=(295, 500), 
                                text_input="QUIT", font=self.get_font(25), base_color="#d7fcd4", hovering_color="White")
            
            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, RECORD_BUTTON, INFORMATION_BUTTON, QUIT_BUTTON, ]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.gameOver=False
                        self.jugada = [['','',''],
                                    ['','',''],
                                    ['','','']]
                        self.iniciarJuego()
                    if RECORD_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.grafica()
                        self.historial() 
                    if INFORMATION_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.informacion()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()


    def historial(self):
        miFuente = pygame.font.Font(None, 30)
        self.propiedades.blit(self.propiedadesF, (0,0))
        i=10
        temporal = self.doubleList.primero
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    if(self.doubleList.vacio()):
                        pass
                    else:
                        while temporal:
                            texto = ""
                            texto = "Jugador ganador: "+ temporal.ganador
                            miTexto = miFuente.render(texto, True, "#872079")
                            self.propiedades.blit(miTexto, (200,i))
                            i=i+ 30
                            texto = ""
                            texto = "Turnos Jugados: "+ str(temporal.ponderacion)
                            miTexto = miFuente.render(texto, True, "#872079")
                            self.propiedades.blit(miTexto, (200,i))
                            i=i+ 50
                            temporal = temporal.siguiente
                pygame.display.update()


    def informacion(self):
        miFuente = pygame.font.Font(None, 30)
        self.propiedades.blit(self.propiedadesF, (0,0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    miTexto = miFuente.render("Maria Luisa Fernanda Calderon Molina", True, "#872079")
                    self.propiedades.blit(miTexto, (50,100))
                    
                    miTexto = miFuente.render("Carnet: 9490-23-9993", True, "#872079")
                    self.propiedades.blit(miTexto, (50,200))
                       
            pygame.display.update()

    def grafica(self):
        self.doubleList.pintar()

       

if __name__ == "__main__":

    t =  Totito()
    t.menu_inicio()
    #t.iniciarJuego()




