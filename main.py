import pygame as pyg
import random
import math

pyg.init()

# Displaying the screen
screen = pyg.display.set_mode((800, 600))
score = 0

# Title and Icon
pyg.display.set_caption("Space Invaders")
icon = pyg.image.load('Icons/rocket.png')
pyg.display.set_icon(icon)

#Setting the background of the game
background = pyg.image.load('Icons/back.png')

# Player
playerimg = pyg.image.load('Icons/spaceship.png')
px = 368
py = 480
px_move = 0

# Enemy
en_img = pyg.image.load('Icons/alien.png')
ex = random.randint(0, 736)
ey = random.randint(50, 150)
en_move_x = 4
en_move_y = 40

# Bullet
bulletimg = pyg.image.load('Icons/bullet.png')
bulletx = 0
bullety = 480
bullet_move_x = 0
bullet_move_y = 10
bull_state = "ready"

# Defining functions for player, enemy and bullets
def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y):
    screen.blit(en_img, (x, y))

def fire_bullet(x, y):
    global bull_state
    bull_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def is_collision(ex, ey, bulletx, bullety):
    dist = math.sqrt((math.pow(ex - bulletx, 2)) + (math.pow(ey - bullety, 2)))
    if dist < 27:
        return True
    else:
        return False


run = True
while run:
    # Background color
    screen.fill((0, 0, 0))

    # Overwrite on background screen(blit())
    screen.blit(background, (0, 0))

    # Loops through all event happening in the game
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False

        # Setting the event type
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT:
                px_move = -5
            if event.key == pyg.K_RIGHT:
                px_move = 5
            if event.key == pyg.K_SPACE:
                if bull_state is "ready":
                    bulletx = px
                    fire_bullet(bulletx, bullety)

        if event.type == pyg.KEYUP:
            if event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT:
                px_move = 0

    px += px_move
    if px <= 0:
        px = 0
    elif px >= 736:
        px = 736

    ex += en_move_x
    if ex <= 0:
        en_move_x = 4
        ey += en_move_y
    elif ex >= 736:
        en_move_x = -4
        ey += en_move_y

    if bullety <= 0:
        bullety = 480
        bull_state = "ready"

    if bull_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullet_move_y

    # Collision
    coll = is_collision(ex, ey, bulletx, bullety)
    if coll:
        bullety = 480
        bull_state = "ready"
        score += 1

        ex = random.randint(0, 736)
        ey = random.randint(50, 150)

    player(px, py)
    enemy(ex, ey)
    pyg.display.update()
