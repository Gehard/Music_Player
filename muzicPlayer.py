import pygame
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((600,400))
mixer.music.load('file.mp3')
mixer.music.play()

print('press 'r' to pause 'r' to resume ')
print('press 'Q' to quit')

running = True
while running:
    for event in pygame.event.g