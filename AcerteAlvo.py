import pygame
import random

pygame.mixer.init()
pygame.init()
#variaveis
ALTURA_TELA = 600
LARGURA_TELA = 800

tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
pygame.display.set_caption('Acerte o Alvo')

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL = (0, 0, 139)

relogio = pygame.time.Clock()
rodando = True

TAMANHO_ALVO = 50

#onde ele vai estar, x, y
alvo_rect = pygame.Rect(375, 275, TAMANHO_ALVO, TAMANHO_ALVO)

pontuacao = 0
fonte = pygame.font.SysFont("papyrus", 65)
som_acerto = pygame.mixer.Sound("acerto.ogg")
som_erro = pygame.mixer.Sound("erro.ogg")



while rodando:
    #Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if alvo_rect.collidepoint(evento.pos):
                alvo_rect.x = random.randrange(0, 750) #largura da tela - tamanho_alvo
                alvo_rect.y = random.randrange(0, 550) #Altura da tela - tamanho_alvo
                pontuacao += 1
                som_acerto.play()

            else:
                pontuacao -= 2
                som_erro.play()
                if pontuacao < 0:
                    pontuacao = 0




    tela.fill(PRETO)

    pygame.draw.rect(tela, AZUL, alvo_rect)

    texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)

    tela.blit(texto_pontos, (10, 10))

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()        

