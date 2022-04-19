import pygame
import sys

ancho = 640
alto = 480
fondo = (0,0,64)

##########CLASES PARA EL JUEGO########
class Pelota(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load('img/pelota.png')
    self.rect = self.image.get_rect()
    self.rect.centerx = ancho / 2
    self.rect.centery = alto / 2
    self.speed = [5,5]

  def update(self):
        if self.rect.bottom >= alto or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ancho or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
        
        self.rect.move_ip(self.speed)

pantalla = pygame.display.set_mode((640,480))
pygame.display.set_caption('JUEGO PYTHON')

reloj = pygame.time.Clock()
pygame.key.set_repeat(30)

bolita = Pelota()

while True:
  reloj.tick(60)

  for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

  bolita.update()
  pantalla.fill(fondo)
  pantalla.blit(bolita.image,bolita.rect)
  pygame.display.flip()