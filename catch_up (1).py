import pygame
import random
import json

pygame.init()

win = pygame.display.set_mode((1000, 400))
clock = pygame.time.Clock()

font = pygame.font.Font (None, 36)
lose_msg = font.render ('HAHA, YOU LOSE!!!!', False, (255, 255, 255))

background = pygame.image.load('PlayfulWeeklyGuppy-mobile.jpg')
background = pygame.transform.scale(background, (1000, 400))

class Dino(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

dino = Dino('dino_cool.png', 50, 190, 50, 50)

class Cactus(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, width, height ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += -5

        if self.rect.x > 1000:
            self.rect.x = 0
        
        if self.rect.x < 0:
            self.rect.x = 1000 

cactus = pygame.sprite.Group()
a = Cactus('cactus_cool.png', 700, 190, 70, 50)
a1 = Cactus('cactus_cool.png', 500, 190, 70, 50)
a2 = Cactus('cactus_cool.png', 250, 190, 70, 50)
cactus.add(a1)
cactus.add(a2)
cactus.add(a)


vy = 0
run = True    
while run:
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                vy = 15

    cactus_collisions = pygame.sprite.spritecollide(dino, cactus , False)
    for a in cactus_collisions:
        if a.rect.width > 25:
            lose_msg.blit( )

    dino.rect.y -= vy
    if dino.rect.y < 190:
        vy -= 1

    if dino.rect.y > 190:
        vy = 0
        dino.rect.y = 190

    win.blit(background, (0, 0))
    dino.draw (win)
    cactus.update ()
    
    for c in cactus:
        c.draw (win)
    pygame.display.update()
    clock.tick(60)