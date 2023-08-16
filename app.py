import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((700, 600))

rect = pygame.Rect(50, 100, 50, 100)


while True:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP:
            rect.move_ip(0, -20)

    pygame.draw.rect(screen, (0, 255, 0), rect)
    pygame.display.flip()