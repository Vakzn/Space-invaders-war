import pygame, random, math
from pygame import mixer

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

#fone music
mixer.music.load('assets/background.wav')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

#player
playerImg = pygame.image.load('assets/player.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
#bullet
bulletImg = pygame.image.load('assets/bullet.png')
bulletX = playerX
bulletY = 480
bulletX_change = 0
bulletY_change = 15
bullet_state = 'ready'

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#game over
overfont = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text(x, y):
    over_text = font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def show_Score(x, y):
    score = font.render('Score : '+ str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

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
                    bullet_sound = mixer.Sound('assets/laser.wav')
                    bullet_sound.set_volume(0.08)
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

    #player cycle
    playerX += playerX_change
    # game border for player
    if playerX > 736:
        playerX = 736
    elif playerX < 0:
        playerX = 0

    #enemy cycle
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            enemyX = 963
            enemyY = 800
            game_over_text(200, 250)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 8
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -8
            enemyY[i] += enemyY_change[i]

    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
        explosion_sound = mixer.Sound('assets/explosion.wav')
        explosion_sound.set_volume(0.1)
        explosion_sound.play()
        bulletY = 480
        bullet_state = 'ready'
        score_value += 1
        enemyX[i] = random.randint(0, 735)
        enemyY[i] = random.randint(50, 150)
    enemy(enemyX[i], enemyY[i], i)

    #bullet cycle
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_Score(textX, textY)
    pygame.display.update()