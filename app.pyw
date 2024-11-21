import pygame
import sys
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#bgl pra iniciar o jogo
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((720,480))
clock = pygame.time.Clock()
background = pygame.image.load("background.png").convert_alpha()
click = pygame.mixer.Sound("click.mp3")
cooking = pygame.mixer.Sound("cooking.mp3")
italianfont = pygame.font.Font("Cafe Francoise_D.otf",30)
####################




#massa skin
massa = pygame.image.load("massa.png").convert_alpha()
massa_molho = pygame.image.load("massa_molho.png").convert_alpha()
massa_molho_queijo = pygame.image.load("massa_molho_queijo.png").convert_alpha()
massa_molho_queijo_peperonni = pygame.image.load("massa_molho_queijo_peperonni.png").convert_alpha()
massa_molho_queijo_peperonni_feita = pygame.image.load("massa_molho_queijo_peperonni_feita.png").convert_alpha()
massa_molho_queijo_feita = pygame.image.load("massa_molho_queijo_feita.png").convert_alpha()
nada = pygame.surface.Surface((1,1))

blitter = None
#######

# DINHEIROS
argent = 0



# textos
argent_text = italianfont.render("{:.2f}".format(argent), True, (46, 91, 37))
####


#botões pretty botões
massa_button = pygame.rect.Rect(16,16,80,80)
sauce_button = pygame.rect.Rect(16, 112, 80, 80)
queijo_button = pygame.rect.Rect(16, 208, 80, 80)
linguica_button = pygame.rect.Rect(16, 304, 80, 80)

oven_button = pygame.rect.Rect(592, 351, 112, 113)

send_button = pygame.rect.Rect(592, 304, 112, 33)
########################################





while True:
    #bgl pra fzr o jogo fechar nn mexe, porra
    if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit()
    #########################################

    #OS MOUSE STATES, NN MEXE PORRA
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()
    #############################
    screen.blit(background, [0,0])

    #TEXTOS DE L'ARGENT
    argent_text = italianfont.render("{:.2f}".format(argent), True, (46, 91, 37))
    ###################################


##### BUTOES
    if massa_button.collidepoint(mouse_pos) and any(mouse_clicked) and blitter != massa:
          blitter = massa
          pygame.mixer.Sound.play(click)
    if sauce_button.collidepoint(mouse_pos) and any(mouse_clicked) and blitter == massa:
          blitter = massa_molho
          pygame.mixer.Sound.play(click)
    if queijo_button.collidepoint(mouse_pos) and any(mouse_clicked) and blitter == massa_molho:
        blitter = massa_molho_queijo
        pygame.mixer.Sound.play(click)
    if linguica_button.collidepoint(mouse_pos) and any(mouse_clicked) and blitter == massa_molho_queijo:
         blitter = massa_molho_queijo_peperonni
         pygame.mixer.Sound.play(click)
    if oven_button.collidepoint(mouse_pos) and any(mouse_clicked) and blitter not in (massa_molho_queijo_feita, massa_molho_queijo_peperonni_feita, massa, massa_molho):
         if blitter == massa_molho_queijo_peperonni: blitter = massa_molho_queijo_peperonni_feita
         if blitter == massa_molho_queijo: blitter = massa_molho_queijo_feita
         pygame.mixer.Sound.play(cooking)
         pygame.mixer.Sound.play(click)
         
    if send_button.collidepoint(mouse_pos) and any(mouse_clicked) and blitter in (massa_molho_queijo_peperonni_feita, massa_molho_queijo_feita):
         if blitter == massa_molho_queijo_peperonni_feita: argent += 2.43
         if blitter == massa_molho_queijo_feita: argent += 1.93
         blitter = nada
         pygame.mixer.Sound.play(click)
####


    if blitter != None:
        screen.blit(blitter, (136, 50))
    screen.blit(argent_text, (594, 16))
     
    pygame.display.flip()
    clock.tick(60)