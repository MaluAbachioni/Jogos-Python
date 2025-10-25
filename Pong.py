import pygame

pygame.mixer.init()
pygame.init()
#variaveis
ALTURA_TELA = 600
LARGURA_TELA = 800

tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
pygame.display.set_caption('Pong')

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

fonte_pontos = pygame.font.Font(None, 90)
pontos1 = 0
pontos2 = 0

LARGURA_RAQUETE = 15
ALTURA_RAQUETE = 100

#Classe - Bloco de Código - Molde
class Raquete:
    #o que vai acontecer quando eu criar uma raquete
    def __init__ (self, x, y):
        self.rect = pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE)

    def desenhar(self, tela):
        pygame.draw.rect(tela, BRANCO, self.rect)

    def mover(self, tecla_cima, tecla_baixo):

        teclas = pygame.key.get_pressed()

        if teclas[tecla_cima] and  self.rect.top > 0:
            self.rect.y -= 8
        if teclas[tecla_baixo] and  self.rect.bottom < 600:
            self.rect.y += 8


raquete1 = Raquete(10, 300)
raquete2 = Raquete(780, 300)
    

RAIO_BOLA = 10
VELOCIDADE_BOLA_X = 5
VELOCIDADE_BOLA_Y = 5

class Bola:
    def __init__ (self, x, y):
        self.rect = pygame.Rect(x - RAIO_BOLA, y - RAIO_BOLA, RAIO_BOLA * 2, RAIO_BOLA * 2)

        self.vel_x = VELOCIDADE_BOLA_X
        self.vel_y = VELOCIDADE_BOLA_Y

    def desenhar (self, tela):
        pygame.draw.ellipse(tela, BRANCO, self.rect)

    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def verificar_colisao(self, raquete1, requete2):
        #Se bateu na parede
        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.vel_y *= -1

        #Se bateu na raquete
        if self.rect.colliderect(raquete1) or self.rect.colliderect(raquete2):
            self.vel_x *= -1

        

    def resetar(self):
        self.rect.x = LARGURA_TELA / 2 - RAIO_BOLA
        self.rect.y = ALTURA_TELA / 2 - RAIO_BOLA

        pygame.time.delay(1000)


bola = Bola(400,300)



relogio = pygame.time.Clock()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    

    tela.fill(PRETO)
    raquete1.desenhar(tela)
    raquete2.desenhar(tela)
    bola.desenhar(tela)

    raquete1.mover(pygame.K_w, pygame.K_s)
    raquete2.mover(pygame.K_UP, pygame.K_DOWN)
    bola.mover()
    bola.verificar_colisao(raquete1.rect, raquete2.rect)
    if bola.rect.left < 0:
            pontos2 += 1 
            bola.resetar()

    if bola.rect.right > LARGURA_TELA:
            pontos1 += 1
            bola.resetar()

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()  