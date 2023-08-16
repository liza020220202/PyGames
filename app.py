import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))

rect = pygame.Rect(50, 100, 50, 100)
pygame.draw.rect(screen, (0, 255, 0), rect)

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()