import pygame, random, math

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
enemyX = 370
enemyY = 120
enemyX_change = 5
enemyY_change = 4

#bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = playerX
bulletY = 480
bulletX_change = 0
bulletY_change = 15
bullet_state = 'ready'

#score
score = 0

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 28:
        return True
    else:
        return False

def theCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + math.pow(enemyY - playerY, 2))
    if distance < 28:
        return True
    else:
        return False

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
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

    #player cycle
    playerX += playerX_change
    # game border for player
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0
    collisionPl = theCollision(enemyX, enemyY, playerX, playerY)
    if collisionPl:
        playerY = 480
        bullet_state = 'ready'
        running = False

    #enemy cycle
    enemyX += enemyX_change
    enemyY += enemyY_change
    if enemyX <= 0:
        enemyX_change = 4
    if enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyX = random.randint(0, 800)
        enemyY = random.randint(50, 150)


    #bullet cycle
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #game over
    if enemyY > playerY:
        print('game over')

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
