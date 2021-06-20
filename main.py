import pygame, random

#install pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

#title window and icon
pygame.display.set_caption('Space invaders')
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

#set background
bg = pygame.image.load('assets/background.png')

#player
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = pygame.image.load('assets/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 0.1

#bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = playerX
bulletY = 480
bulletX_change = 0
bulletY_change = -0.2
bullet_state = 'ready'

def player():
    screen.blit(playerImg, (playerX, playerY))

def enemy():
    screen.blit(enemyImg, (enemyX, enemyY))

def fire_bullet():
    if bullet_state == 'fire':
        screen.blit(bulletImg, (bulletX, bulletY))

#game cycle
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
            if event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_state = 'fire'

    #player cycle
    playerX += playerX_change
    player()

    #enemy cycle
    enemy()
    enemyX += enemyX_change
    enemyY += enemyY_change

    #bullet cycle
    bulletY += bulletY_change
    fire_bullet()


    #game border for player
    if playerX > 736:
        playerX = 736
    if playerX < 0:
        playerX = 0

    #game border for enemy
    if enemyX > 736:
        enemyX = 736
    if enemyX < 0:
        enemyX = 0

    pygame.display.update()
