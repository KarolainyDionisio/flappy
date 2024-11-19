import pygame
from scripts.cenas import Partida
from scripts.cenas import Menu
#from scripts.jogador import Jogador
#from scripts.cano import Cano
pygame.init()

tamanhotela = [600,400]
tela = pygame.display.set_mode(tamanhotela)
pygame.display.set_caption("FlappyBird")
relogio = pygame.time.Clock()
corFundo = (89, 148, 214)

listaCenas = {
    'partida': Partida(tela),
    'menu' : Menu(tela)
}

cenaAtual = 'menu'
#jog = Jogador(tela,100,100)
#cano = Cano(tela)
while True: 
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    tela.fill(corFundo)
 
    cenaAtual = listaCenas[cenaAtual].atualizar()
    #jog.atualizar()
    #jog.desenhar()
    #cano.atualizar()
    #cano.desenhar()
    relogio.tick(60)
    pygame.display.flip()
