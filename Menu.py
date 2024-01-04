import pygame, sys, random, time, math
from Juego import start_Juego

pygame.init()

# crear ventana
screen = pygame.display.set_mode([800,450])
pygame.display.set_caption("Asteroid War")

Player_img = pygame.image.load("Imagenes/Cohete.png").convert() #cargar la imagen
fondo = pygame.image.load("Imagenes/Espacio.jpg").convert_alpha()
musica_fondo = pygame.mixer.music.load("Sonidos/Crash Bandicoot 2 - Dr2.wav")
pygame.mixer.music.stop()
pygame.mixer.music.play(-1) #Se TOCA INDEFINIDAMENTE

def New_Boton(screen, boton, texto, color_text, color1,color2):
    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, color1, boton, 0)
    else:
        pygame.draw.rect(screen, color2, boton, 0)
    
    text_rend = Text_B.render(texto, True, color_text)
    Play_X = boton.x + (boton.width-text_rend.get_width())/2
    Play_Y = boton.y + (boton.height-text_rend.get_height())/2
    screen.blit(text_rend,(Play_X,Play_Y))


#definir colores
BLACK   = (     0,      0,      0)
WHITE   = (     255,    255,    255)
GREEN   = (     0,      255,    0)
RED     = (     255,    0,      0)
BLUE    = (     0,      0,    255)
ORANGE  = (     255,     125,    25)

Text_B = pygame.font.SysFont('comicsans', 30, True)
Text_Ins = pygame.font.SysFont('comicsans', 20, True)

Button_Play = pygame.Rect(400-100, 250, 200, 50)
Button_Inst = pygame.Rect(400-100, 320, 200, 50)
Button_salir = pygame.Rect(400-100, 390, 200, 50)
Button_atras = pygame.Rect(800-100, 10, 60, 30)

Player_img.set_colorkey(BLACK)

def S_Menu():
    Instrucciones = False
    while True:
        screen.blit(fondo,[0,0])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Button_Play.collidepoint(pygame.mouse.get_pos()):
                    
                    start_Juego()
                    print("Click")
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Button_Inst.collidepoint(pygame.mouse.get_pos()):
                    Instrucciones = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Button_salir.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Button_atras.collidepoint(pygame.mouse.get_pos()):
                    Instrucciones = False

        if not Instrucciones:

            screen.blit(Player_img,((800-Player_img.get_width())/2,80))

            New_Boton(screen,Button_Play,"PLAY",WHITE,ORANGE,GREEN)
            New_Boton(screen,Button_Inst,"Instrucciones",WHITE,ORANGE,GREEN)
            New_Boton(screen,Button_salir,"Salir",WHITE,ORANGE,GREEN)
        else:
                New_Boton(screen,Button_atras,"X",BLACK,RED,WHITE)

                text_rend = Text_B.render("INTRUCCIONES", True, GREEN)
                screen.blit(text_rend,(325,50))
                text_rend = Text_Ins.render("La tierra afronta una lluvia de asteroides, ¡Necesitamos tu ayuda! ¡Destruyelos!", True, WHITE)
                screen.blit(text_rend,(15,150))
                text_rend = Text_Ins.render("- La nave se mueve horizontalmente siguiendo la posición del mouse", True, WHITE)
                screen.blit(text_rend,(75,220))
                text_rend = Text_Ins.render("- Para disparar presiona el boton derecho del mouse", True, WHITE)
                screen.blit(text_rend,(75,260))
                text_rend = Text_Ins.render("- Pierdes al dejar pasar hatsa 3 asteroides", True, WHITE)

                screen.blit(text_rend,(75,300))
        pygame.display.flip()      
        pygame.display.update()

# Mantener el Juego en Ejecucion
S_Menu()