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

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                rect.move_ip(0, -20)

            if event.key == pygame.K_DOWN:
                rect.move_ip(0, 20)

            if event.key == pygame.K_LEFT:
                rect.move_ip(-20, 0)

            if event.key == pygame.K_RIGHT:
                rect.move_ip(20, 0)



    pygame.draw.rect(screen, (0, 255, 0), rect)
    pygame.display.flip()