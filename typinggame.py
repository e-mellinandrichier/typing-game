import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Fruits Slicer")

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)

font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 36)

fruits_images = [
    pygame.image.load("pictures/fraise.jpg"),
    pygame.image.load("pictures/fraise.jpg"),
    pygame.image.load("pictures/banana.jpg"),
    pygame.image.load("pictures/banana.jpg"),
    pygame.image.load("pictures/cherry.jpg"),
    pygame.image.load("pictures/cherry.jpg"),
    pygame.image.load("pictures/orange.jpg"),
    pygame.image.load("pictures/orange.jpg"),
    pygame.image.load("pictures/glaçon.jpg"),
    pygame.image.load("pictures/bomb.png")
]

fruit_images = [pygame.transform.scale(img,(60,60)) for img in fruits_images]


LETTERS = "ABC"

class Fruit : 
    def __init__(self):
        self.image = random.choice(fruit_images)
        self.letter = random.choice(LETTERS)
        self.x = random.randint(0, 600)
        self.y = 550
        self.speed = 10
        self.mouv = random.randint(-3, 3)
    
    def update(self):
        self.x += self.mouv
        self.speed -= 0.2
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        text = font.render(self.letter, True, BLACK)
        screen.blit(text, (self.x + 20, self.y + 15))

fruits = [Fruit() for _ in range(2)]
score = 0
lives = 3

running = True
clock = pygame.time.Clock()

while running : 
    screen.fill(WHITE)
    score_text = score_font.render(f"Score : {score}", True, BLACK)
    lives_text = score_font.render(f"Lives : {lives}", True, BLACK)
    ice_text = score_font.render("Ice", True, RED)
    screen.blit(score_text, (10,10))
    screen.blit(lives_text, (10,40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            key_pressed = event.unicode.upper()
            for fruit in fruits :
                if fruit.letter == key_pressed :
                    fruits.remove(fruit)
                    fruits.append(Fruit())
                    if fruit.image == fruit_images[-2]:
                        screen.blit(ice_text, (40,100))
                        time.sleep(2)
                        pygame.display.flip()
                    if fruit.image == fruit_images[-1]:
                        running = False
                    score += 1
                    break

    for fruit in fruits : 
        fruit.update()
        fruit.draw(screen)

        if fruit.y > HEIGHT:
            fruits.remove(fruit)
            fruits.append(Fruit())
            if fruit.image != fruit_images[-1]:
                lives -= 1
        if lives == 0:
            running = False
    
    pygame.display.flip()
    clock.tick(30)
pygame.quit()