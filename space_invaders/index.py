import pygame
import random
from math import sqrt, pow

#inicializa o pygame
pygame.init()

#cria uma tela, passando uma tupla com as dimensões
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load("icons/background.jpg")

#define o título e icone da tela
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icons/arcade_space.png')
pygame.display.set_icon(icon)

# Jogador
playerImg = pygame.image.load('icons/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Inimigo
enemyImg = pygame.image.load('icons/enemy.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 10

# Bala
bulletImg = pygame.image.load('icons/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0
def player(x, y):
    #coloca um elemento na posição indicada
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def enemy(x, y):
    #coloca um elemento na posição indicada
    screen.blit(enemyImg, (x, y))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = sqrt(pow(enemyX-bulletX, 2) + pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    return False

#Loop infinito do jogo
running = True
while running:
    # cor de fundo (RGB)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: #verifica se alguma tecla foi pressionada
            # dependendo da tecla, executa uma ação
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE and bullet_state is "ready":
                # seta a coordenada da bala com as coordenadas atuais da nave
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # quando os personagens atingem as bordas da tela do jogo
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    # movimento do inimigo
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    # Movimento da bala
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # verifica colisao
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()