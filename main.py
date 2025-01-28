import random
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

running = True

img = pygame.image.load("assets/fruit.png").convert()
img = pygame.transform.scale(img, (50, 50))
img2 = pygame.image.load("assets/fraise.jpg").convert()
img2 = pygame.transform.scale(img2, (50, 50))
def create():
    movement = random.randint(-2, 2)
    limit = random.randint(-100, 350)
    x = random.randint(0, 600)
    y = 550
    y2 = y
    return [movement, limit, x, y, y2]

def mouv(y):
    return y - 1

def mouvback(y):
    return y + 1

def mouvy(y, movement, y2, limit):
    if y2 > limit: 
        y = mouv(y)
        y2 = mouv(y2)
    if y2 <= limit:
        y = mouvback(y)
    return [y, y2]

def mouvx(x, movement):
    return x + movement

current_obj = create()

while running: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    screen.fill((0, 0, 0))
    
    movement, limit, x, y, y2 = current_obj
    x = mouvx(x, movement)
    y, y2 = mouvy(y, movement, y2, limit)
    
    if y > 600 or x < -50 or x > 600:
        current_obj = create()
    else:
        current_obj = [movement, limit, x, y, y2]
    
    screen.blit(img, (x, y))
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()