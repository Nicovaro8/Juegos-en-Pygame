import pygame, sys, random, time, math


pygame.init()

def start_Juego():
    # crear ventana
    screen = pygame.display.set_mode([800,450])

    #crear reloj
    clock = pygame.time.Clock()

    #definir colores
    BLACK   = (     0,      0,      0)
    WHITE   = (     255,    255,    255)

    #Definir variables auxiliares
    score = 0
    Vidas_Act = 3

    pygame.display.set_caption("Asteroid War")
    fondo = pygame.image.load("Imagenes/Espacio.jpg").convert()
    Player_img = pygame.image.load("Imagenes/Cohete.png").convert() #cargar la imagen
    Player_F = pygame.image.load("Imagenes/Cohete_Muerte.png").convert() #cargar la imagen
    GameOver = pygame.image.load("Imagenes/GameOver.png").convert() #cargar la imagen
    WorldOver = pygame.image.load("Imagenes/WorldOver.png").convert() #cargar la imagen
    pygame.mouse.set_visible(False)

    musica_fondo = pygame.mixer.Sound("Sonidos/Crash Bandicoot 2 - Dr2.wav")
    Sonido_Disparo_laser = pygame.mixer.Sound("Sonidos/Disparo_Laser.wav")
    Sonido_Meteoro = pygame.mixer.Sound("Sonidos/MeteoroLLega.wav")
    Sonido_GameOver = pygame.mixer.Sound("Sonidos/game-over-38511.wav")
    Sonido_Meteoro_Choque = pygame.mixer.Sound("Sonidos/low-impactwav-14905.wav")

    

    ## --------------- CARGAR IMAGENES EXPLOSIÓN -------------------------- ##
    meteor_images = []
    meteor_list = ["Imagenes/A_Exploción/expl1.png", "Imagenes/A_Exploción/expl2.png", "Imagenes/A_Exploción/expl3.png",
                    "Imagenes/A_Exploción/expl4.png","Imagenes/A_Exploción/expl5.png", "Imagenes/A_Exploción/expl6.png",
                    "Imagenes/A_Exploción/expl7.png", "Imagenes/A_Exploción/expl8.png","Imagenes/A_Exploción/expl0.png"]
    for img in meteor_list:
        meteor_images.append(pygame.image.load(img).convert())

    explosion_anim = []

    for i in range(9):
        file = "Imagenes/A_Exploción/expl{}.png".format(i) #Selecciona la imagen
        img = pygame.image.load(file).convert() #cargar la imagen
        img.set_colorkey(BLACK) #quitar fondo negro
        img_scale = pygame.transform.scale(img, (70, 70))
        explosion_anim.append(img_scale)

    #CLASES
    class Meteoro(pygame.sprite.Sprite): #se crea la clase meteoro la cual es subclase de la clase sprite
        def __init__(self):     #se inicializa la clase
            super().__init__()  #se inicializa la superclase
            self.image = pygame.image.load("Imagenes/Meteoro.png").convert() #cargar la imagen
            
            self.image.set_colorkey(BLACK) #quitar fondo negro
            
            self.rect = self.image.get_rect() #obtener rectangulo de coordenadas del sprite

        def update(self):
            self.rect.y += 2

            if self.rect.y > 450:
                self.rect.y = -100
                self.rect.x = random.randrange(800)

    class NewMeteoro(pygame.sprite.Sprite):
        def __init__(self):     #se inicializa la clase
            super().__init__()  #se inicializa la superclase

            meteoro.rect.x = random.randrange(700) + 30
            meteoro.rect.y = random.randrange(100) - 50

            meteoro_list.add(meteoro)
            all_sprite_list.add(meteoro)

    class Game_Over(pygame.sprite.Sprite): 
        def __init__(self):     #se inicializa la clase
            super().__init__()  #se inicializa la superclase

            self.image = GameOver
            self.image.set_colorkey(BLACK) #quitar fondo negro
            self.rect = self.image.get_rect() #obtener rectangulo de coordenadas del sprite

    class World_Over(pygame.sprite.Sprite): 
        def __init__(self):     #se inicializa la clase
            super().__init__()  #se inicializa la superclase

            self.image = WorldOver
            self.image.set_colorkey(BLACK) #quitar fondo negro
            self.rect = self.image.get_rect() #obtener rectangulo de coordenadas del sprite

    class Player(pygame.sprite.Sprite): 
        def __init__(self):     #se inicializa la clase
            super().__init__()  #se inicializa la superclase
            
            self.image = Player_F
            self.image.set_colorkey(BLACK) #quitar fondo negro
            self.rect = self.image.get_rect() #obtener rectangulo de coordenadas del sprite

            self.image = Player_img
            self.image.set_colorkey(BLACK) #quitar fondo negro
            self.rect = self.image.get_rect() #obtener rectangulo de coordenadas del sprite
            self.vidas = 3
            
        def update(self):
            mouse_pos = pygame.mouse.get_pos()
            player.rect.x = mouse_pos[0]
            player.rect.y = 450-130

    class Disparo(pygame.sprite.Sprite): 
        def __init__(self):     #se inicializa la clase
            super().__init__()  #se inicializa la superclase
            self.image = pygame.image.load("Imagenes/Bala.PNG").convert() #cargar la imagen
            self.image.set_colorkey(BLACK) #quitar fondo negro
            self.rect = self.image.get_rect() #obtener rectangulo de coordenadas del sprite

        def update(self):
            self.rect.y += -1

    class Explosion(pygame.sprite.Sprite):
        def __init__(self, center):
            super().__init__()
            self.image = explosion_anim[0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 50 # Tiempo entre animaciones

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim):
                    self.kill() 
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center


    meteoro_list = pygame.sprite.Group()
    disparo_list = pygame.sprite.Group()
    all_sprite_list = pygame.sprite.Group() #lista donde se almacenan todas las instancias



    #creando los 5 meteoros
    for i in range(5):
        meteoro = Meteoro()
        NewMeteoro()

    #creando las demas instancias
    player = Player()
    disparo = Disparo()
    Game_OVER = Game_Over()
    World_OVER = World_Over()

    #Configurando el texto
    all_sprite_list.add(player)
    puntos_texto = pygame.font.SysFont('comicsans', 30, True)
    img = pygame.image.load("Imagenes/Cohete.png").convert() #cargar la imagen

    #3 vidas del juego
    Vida3=Player_img
    Vida2=Player_img
    Vida1=Player_img

    done = False
    while not done:
        screen.blit(fondo,[0,0])
        all_sprite_list.draw(screen)

        for event in pygame.event.get():
                if event.type == pygame.QUIT: done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    disparo = Disparo()
                    disparo.rect.x = player.rect.x + 5
                    disparo.rect.y = player.rect.y -20

                    disparo_list.add(disparo)
                    all_sprite_list.add(disparo)

                    Sonido_Disparo_laser.play()

        if Vidas_Act > 0:
        
            #Crea una lista con todos los objetos colisionando
            all_sprite_list.update()

            for disparo in disparo_list:
                meteoro_hit_list = pygame.sprite.spritecollide(disparo, meteoro_list, True) #Elimina los sprite colisionado (True)

                # suma en score la cantidad de valores que hay en la lista actual de colisiones
                for meteoro in meteoro_hit_list:
                    score += 1
                    all_sprite_list.remove(disparo)
                    disparo_list.remove(disparo)
                    
                    meteoro = Meteoro()
                    NewMeteoro()
                    Sonido_Meteoro_Choque.play()

                    explosion = Explosion(disparo.rect.center)
                    all_sprite_list.add(explosion)

                if disparo.rect.y < -10:
                    all_sprite_list.remove(disparo)
                    disparo_list.remove(disparo)

            for meteoro in meteoro_list:
                if meteoro.rect.y > 400:
                    Sonido_Meteoro.play()
                    all_sprite_list.remove(meteoro)
                    meteoro_list.remove(meteoro)
                    meteoro = Meteoro()
                    NewMeteoro()

                    Vidas_Act = Vidas_Act - 1
                    

                    if Vidas_Act == 2:
                        Vida1 = Player_F
                    if Vidas_Act == 1:
                        Vida2 = Player_F
                    if Vidas_Act == 0:
                        Vida3 = Player_F
                        

            puntos = puntos_texto.render('Puntaje: '+ str(score), 1, WHITE)

            
            screen.blit(puntos, (350,10))
            muerte_3 = screen.blit(pygame.transform.scale(Vida3, (40,70)), (10,15))
            muerte_2 = screen.blit(pygame.transform.scale(Vida2, (40,70)), (60,15))
            muerte_1 = screen.blit(pygame.transform.scale(Vida1, (40,70)), (110,15))
            pygame.display.flip()
            clock.tick(60)
        else:
            time.sleep(0.2)
            screen.blit(fondo,[0,0])   

            all_sprite_list.add(Game_OVER)
            all_sprite_list.add(World_OVER)

            screen.blit(pygame.transform.scale(WorldOver, (250,200)),(275,50))
            screen.blit(pygame.transform.scale(GameOver, (250,200)),(275,225))
            
            pygame.display.flip()
            all_sprite_list.draw(screen)

            Sonido_GameOver.play()
            time.sleep(4)
            pygame.mouse.set_visible(True)
            Vidas_Act=3
            pygame.mixer.music.stop()
            from Menu import S_Menu
            S_Menu()
            
    
        
    pygame.quit()

# Ejecutar el juego si se llama directamente este script
if __name__ == "__main__":
    start_Juego()