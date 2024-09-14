import pygame
from time import sleep

pygame.init()
pygame.mixer.init()

# Creating a display
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

pygame.mixer.music.load('soothing1.mp3')

pygame.mixer.music.play()
sleep(5)

pygame.mixer.music.load('scary2.mp3')
pygame.mixer.music.play()
sleep(1)

image = pygame.image.load('h2.png')
window.blit(image,(0,0))

pygame.display.update()
sleep(5)