import sys
import pygame
import random
from pygame.locals import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
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
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 500-40), 0)
    
    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 500:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(160, 420), 0)

while running:
     # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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