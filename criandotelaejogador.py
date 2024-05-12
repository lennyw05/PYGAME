#importando bibliotecas
import random
import pygame

pygame.init()

largura_tela = 1000
altura_tela = 600
tela = pygame.display.set_mode([largura_tela, altura_tela]) 
superficie = pygame.Surface((largura_tela, altura_tela), pygame.SRCALPHA)
pygame.display.set_caption('Jetpack Joyride Remake in Python!')
fps = 60
timer = pygame.time.Clock()
fonte = pygame.font.Font('freesansbold.ttf', 32)
cor_bg = (128, 128, 128)
lines = [0, largura_tela/4, 2*largura_tela/4, 3*altura_tela/4]
velocidade_jogo = 12
pause = False
init_y = altura_tela - 130
player_y = init_y
booster = False


#todo código para mover as linhas e desenhar imagens 
def desenhar_tela(line_list):
    tela.fill('black')
    pygame.draw.rect(superficie, (cor_bg[0], cor_bg[1], cor_bg[2], 50), [0, 0, largura_tela, altura_tela])
    tela.blit(superficie, (0, 0))
    top = pygame.draw.rect(tela, 'gray', [0, 0, largura_tela, 50])
    bot = pygame.draw.rect(tela, 'gray', [0, altura_tela - 50, largura_tela, 50])
    for i in range(len(line_list)):
        pygame.draw.line(tela, 'black', (line_list[i], 0), (line_list[i], 50), 3)
        pygame.draw.line(tela, 'black', (line_list[i], altura_tela - 50), (line_list[i], altura_tela), 3)
        if not pause:
            line_list[i] -= velocidade_jogo
        if line_list[i] < 0:
            line_list[i] = largura_tela
    return line_list, top, bot    


#desenhando jogador e animações
def desenhar_jogador():
    play = pygame.rect.Rect((120, player_y + 10), (25, 60))
    pygame.draw.rect(tela, 'green', play, 5)
    if player_y <= init_y or pause:
        if booster:
            pygame.draw.ellipse(tela, 'red', [100, player_y + 50, 20, 30])
            pygame.draw.ellipse(tela, 'orange', [105, player_y + 50, 10, 30])
            pygame.draw.ellipse(tela, 'yellow', [110, player_y + 50, 5, 30])
        pygame.draw.rect(tela, 'yellow', [128, player_y + 60, 10, 20], 0, 3)  
        pygame.draw.rect(tela, 'orange', [130, player_y + 60, 10, 20], 0, 3)   
    # jetpack, corpo e cabeça
    pygame.draw.rect(tela, 'white', [100, player_y + 20, 20, 30], 0, 5)
    pygame.draw.ellipse(tela, 'orange', [120, player_y + 20, 20, 50])
    pygame.draw.circle(tela, 'orange', (135, player_y + 15), 10)
    pygame.draw.circle(tela, 'black', (138, player_y + 12), 3)
    return play

run = True
while run:
    timer.tick(fps)
    lines, top_plat, bot_plat = desenhar_tela(lines)
    jogador = desenhar_jogador()


    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run == False

    pygame.display.flip()
pygame.quit()
