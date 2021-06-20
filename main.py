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
enemyX_change = 5
enemyY_change = 1

#bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

#game cycle
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(bulletX, bulletY)

    #player cycle
    playerX += playerX_change
    # game border for player
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0

    #enemy cycle
    enemyX += enemyX_change
    enemyY += enemyY_change
    #game border for enemy
    if enemyX <= 0:
        enemyX_change = 0.5
    if enemyX >= 736:
        enemyX_change = -0.5

    #bullet cycle
    if bullet_state == 'fire':
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    fire_bullet(playerX, bulletY)
    pygame.display.update()
