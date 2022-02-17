import sys
import pygame
import random
from pygame.locals import *

pygame.init()

# Set up the drawing window
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
blue = pygame.Color(0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
running = True
FPS = 60
frame_per_sec = pygame.time.Clock()
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('/Users/KhalilAMcFarlane/Desktop/Pitt 2021-22/pygame-test/GitHub/sprites/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
    
    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/KhalilAMcFarlane/Desktop/Pitt 2021-22/pygame-test/GitHub/sprites/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 500:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

p1 = Player()
e1 = Enemy()
while running:
     # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    p1.update()
    e1.move()

    screen.fill(white)
    p1.draw(screen)
    e1.draw(screen)

    pygame.display.update()
    frame_per_sec.tick(FPS)
    '''
    # Fill the background with white
    screen.fill(white)
    pygame.mixer.music.load("Dramaturgy.mp3")
    pygame.mixer.music.play(1)

    #pygame.mixer.music.load("lofi.mp3")

    pygame.draw.line(screen, red, (150, 130), (130, 170))
    pygame.draw.line(screen, red, (150, 130), (170, 170))
    pygame.draw.line(screen, red, (130, 170), (170, 170))

        
    pygame.draw.line(screen, red, (350, 130), (330, 170))
    pygame.draw.line(screen, red, (350, 130), (370, 170))
    pygame.draw.line(screen, red, (330, 170), (370, 170))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, red, (250, 250), 75)

    # Flip the display
    pygame.display.flip()
    '''
# Done! Time to quit.
pygame.quit()
sys.exit()