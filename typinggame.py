import pygame
import random
import time
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Fruits Slicer")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 36)
menu_font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

# Load fruit images
fruits_images = [
    pygame.image.load("pictures/fraise.jpg"),
    pygame.image.load("pictures/fraise.jpg"),
    pygame.image.load("pictures/banana.jpg"),
    pygame.image.load("pictures/strawberry.jpg"),
    pygame.image.load("pictures/banana.jpg"),
    pygame.image.load("pictures/cherry.jpg"),
    pygame.image.load("pictures/cherry.jpg"),
    pygame.image.load("pictures/orange.jpg"),
    pygame.image.load("pictures/orange.jpg"),
    pygame.image.load("pictures/glaçon.jpg"),
    pygame.image.load("pictures/bomb.png")
]

fruit_images = [pygame.transform.scale(img, (60, 60)) for img in fruits_images]

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SCORE_FILE = "scores.txt"

class Fruit:
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
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text('Fruit Slicer', menu_font, BLACK, screen, WIDTH/2, 100)


while running : 
    screen.fill(WHITE)
    score_text = score_font.render(f"Score : {score}", True, BLACK)
    lives_text = score_font.render(f"Lives : {lives}", True, BLACK)
    ice_text = score_font.render("Ice", True, RED)
    screen.blit(score_text, (10,10))
    screen.blit(lives_text, (10,40))
        mx, my = pygame.mouse.get_pos()

        btn_play = pygame.Rect(WIDTH/2 - 100, 200, 200, 50)
        btn_scores = pygame.Rect(WIDTH/2 - 100, 300, 200, 50)
        btn_quit = pygame.Rect(WIDTH/2 - 100, 400, 200, 50)
        

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
        pygame.draw.rect(screen, GREEN, btn_play)
        pygame.draw.rect(screen, GREEN, btn_scores)
        pygame.draw.rect(screen, GREEN, btn_quit)
        
        draw_text('Play', button_font, BLACK, screen, WIDTH/2, 225)
        draw_text('High Scores', button_font, BLACK, screen, WIDTH/2, 325)
        draw_text('Quit', button_font, BLACK, screen, WIDTH/2, 425)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.collidepoint((mx, my)):
                    game_loop()
                if btn_scores.collidepoint((mx, my)):
                    show_scores()
                if btn_quit.collidepoint((mx, my)):
                    pygame.quit()
                    return

        pygame.display.update()

def show_scores():
    if not os.path.exists(SCORE_FILE):
        open(SCORE_FILE, 'w').close()
    
    with open(SCORE_FILE, 'r') as f:
        scores = [line.strip() for line in f.readlines() if line.strip().isdigit()]

    
    scores = sorted([int(s) for s in scores], reverse=True)[:10]

    running = True
    while running:
        screen.fill(WHITE)
        draw_text('Score History', menu_font, BLACK, screen, WIDTH/2, 50)

        for i, score in enumerate(scores):
            draw_text(f"{i+1}. {score}", button_font, BLACK, screen, WIDTH/2, 150 + i*50)

        pygame.draw.rect(screen, GREEN, (WIDTH/2 - 100, 500, 200, 50))
        draw_text('Back', button_font, BLACK, screen, WIDTH/2, 525)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if pygame.Rect(WIDTH/2 - 100, 500, 200, 50).collidepoint((mx, my)):
                    running = False

        pygame.display.update()

def save_score(score):
    with open(SCORE_FILE, 'a') as f:
        f.write(f"{score}\n")

def game_loop():
    fruits = [Fruit() for _ in range(3)]
    score = 0
    running = True
    clock = pygame.time.Clock()

    while running: 
        screen.fill(WHITE)
        score_text = score_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    key_pressed = event.unicode.upper()
                    for fruit in fruits:
                        if fruit.letter == key_pressed:
                            fruits.remove(fruit)
                            fruits.append(Fruit())
                            score += 1
                            break

        for fruit in fruits: 
            fruit.update()
            fruit.draw(screen)

            if fruit.y > HEIGHT:
                fruits.remove(fruit)
                fruits.append(Fruit())
    
        pygame.display.flip()
        clock.tick(30)
    
    save_score(score)

if __name__ == "__main__":
    main_menu()