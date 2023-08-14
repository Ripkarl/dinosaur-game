import pygame

pygame.init()

win = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

background = pygame.image.load('PlayfulWeeklyGuppy-mobile.jpg')
background = pygame.transform.scale(background, (800, 400))

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
    def __init__(self, filename, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):

        if self.rect.x > 800:
            self.rect.x = 0
        
        if self.rect.x < 0:
            self.rect.x = 800

cactus = Cactus('cactus_cool.png', 700, 190, 50, 50)
cactus1 = Cactus('cactus_cool.png', 500, 190, 50, 50)
cactus2 = Cactus('cactus_cool.png', 250, 190, 50, 50)
cactus_list = [cactus, cactus1, cactus2]

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
#        elif dino.rect.y > 15:
            
    
    dino.rect.y -= vy
    if dino.rect.y < 190:
        vy -= 1

    if dino.rect.y > 190:
        vy = 0
        dino.rect.y = 190

    win.blit(background, (0, 0))
    dino.draw (win)
    Cactus.draw (win)
    for c in cactus_list:
        c.draw (win)
    pygame.display.update()
    clock.tick(60)