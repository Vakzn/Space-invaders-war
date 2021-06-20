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

def player():
    screen.blit(playerImg, (playerX, playerY))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #цвета в pygame работают в pgb
    screen.fill((0, 0, 0))
    player()
    pygame.display.update()
