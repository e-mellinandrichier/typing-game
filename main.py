import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 600))

running = True

img = pygame.image.load("assets/fruit.png").convert()
img = pygame.transform.scale(img, (50, 50))
img2 = pygame.image.load("assets/fraise.jpg").convert()
img2 = pygame.transform.scale(img, (50, 50))

x = random.randint(0, 600)


def x et def y 
y = 550
y2 = y
def truc():
    movement = random.randint(-5, 5)
    limit = random.randint(-100, 350)
    return movement

def mouv(y):
    y -= 1
    return y

def mouvback(y):
    y += 1
    return y 

while running: 
    for event in pygame.event.get():
        if event.type == pygame.K_ESCAPE:
            running = False
    if y2 > limit: 
        y = mouv(y)
        y2 = mouv(y2)
        x += movement
    if y2 <= limit:
        y = mouvback(y)
        x += movement
    screen.fill((0, 0, 0))
    screen.blit(img, (x, y))
    screen.blit(img2, (x, y))
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
