import pygame

#иннициализируем pygame
pygame.init()

#создаем экран
screen = pygame.display.set_mode((800, 600))

#название окна и иконка
pygame.display.set_caption('Space invaders')
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = pygame.image.load('assets/enemy.png')
enemyX = 370
enemyY = 120
enemyX_change = 0
enemyY_change = 0

def player():
    screen.blit(playerImg, (playerX, playerY))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2

    playerX += playerX_change
    player()
    pygame.display.update()
