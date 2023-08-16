import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 900))

player = pygame.image.load('test.png')

player_x = 50
player_y = 50


while True:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                player_y -= 10

            if event.key == pygame.K_DOWN:
                player_y += 10

            if event.key == pygame.K_LEFT:
                player_x -= 10

            if event.key == pygame.K_RIGHT:
                player_x += 10

    screen.blit(player, (player_x, player_y))

    pygame.display.flip()