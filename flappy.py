# importing modules
import pygame
import random
import time

# initialing pygame module
pygame.init()

# game window attributes

window_len = 700
window_wd = 480
window = pygame.display.set_mode((window_wd, window_len))
pygame.display.set_caption("Flappy Bird Remake")

# colors

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (79, 230, 66)
blue = (0, 180, 180)
yellow = (240, 240, 0)

# game variables

run_game = True
clock = pygame.time.Clock()
fps = 60
score = 00
high_score = 00
# bird attributes

bird_x = 200
bird_y = 100
bird_wd = 30

# velocity

velocity_x = 2
velocity_y = -2

# obstacles attributes

pipe_wd = 100
pipe_x = 800
pipe_y = 0
pipe_len = random.randint(100, 450)
pipe2_x = 800
pipe2_y = pipe_len + 100
pipe3_x = 1200
pipe3_y = 0
pipe_len2 = random.randint(100, 450)
pipe4_x = 1200
pipe4_y = pipe_len2 + 100
pipe5_x = 1600
pipe5_y = 0
pipe_len3 = random.randint(100, 450)
pipe6_x = 1600
pipe6_y = pipe_len3 + 100
# attributes for random pipes generating
pipe_rx = 800
pipe2_rx = 1200
pipe3_rx = 1600
pipe_ry = 0
pipe2_ry = 0
pipe3_ry = 0
piped_rx = 800
piped2_rx = 1200
piped3_rx = 1600
piped_ry = pipe_len + 100
piped2_ry = pipe_len2 + 100
piped3_ry = pipe_len3 + 100
piper_lend1 = window_len - pipe_ry
piper_lend2 = window_len - pipe2_ry
piper_lend3 = window_len - pipe3_ry

pipe_lend = window_len - pipe2_ry
pipe_lend1 = window_len - pipe2_ry
pipe_lend2 = window_len - pipe3_ry

# images

bg_img = pygame.image.load("C:/Users/Amogh Sawant/PycharmProjects/project2/flappy_bird_bg.png")
grass = pygame.image.load("C:/Users/Amogh Sawant/PycharmProjects/project2/stripes.jpg")
flappy_bird = pygame.image.load("C:/Users/Amogh Sawant/PycharmProjects/project2/flpy_brd.png")
flappy_bird2 = pygame.image.load("C:/Users/Amogh Sawant/PycharmProjects/project2/flpy_brddwn.png")

# game start screen

font = pygame.font.SysFont("Snap ITC", 25)
text = font.render("press space to play the game", True, white)
font1 = pygame.font.SysFont("Haettenschweiler", 40)
font2 = pygame.font.SysFont("Snap ITC", 50)
text3 = font2.render(" GAME OVER ", True, white)
text4 = font.render("press space to play again", True, white)
font3 = pygame.font.SysFont("Haettenschweiler", 85)


x = 0
grass_x = 0

# GAME LOOP

while run_game:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run_game = False
        if event.type is pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if x == 2:
                    # resetting bird attributes
                    bird_x = 200
                    bird_y = 100
                    bird_wd = 20
                    # resetting pipe attributes
                    pipe_rx = 800
                    pipe2_rx = 1200
                    pipe3_rx = 1600
                    pipe_ry = 0
                    pipe2_ry = 0
                    pipe3_ry = 0
                    piped_rx = 800
                    piped2_rx = 1200
                    piped3_rx = 1600
                    # resetting score
                    score = 0

                x = 1
                velocity_y = 4.5

# game physics

    if x == 1:
        velocity_y -= 0.32
        bird_y -= velocity_y
        pipe_x -= velocity_x
        pipe2_x -= velocity_x
        pipe3_x -= velocity_x
        pipe4_x -= velocity_x
        pipe5_x -= velocity_x
        pipe6_x -= velocity_x
        pipe_rx -= velocity_x
        pipe2_rx -= velocity_x
        pipe3_rx -= velocity_x
        piped_rx -= velocity_x
        piped2_rx -= velocity_x
        piped3_rx -= velocity_x
        grass_x -= velocity_x

# Game graphics

    window.fill(blue)
    window.blit(bg_img, (0, 0))

    if grass_x == -1420:
        grass_x = 0

    # pygame.draw.rect(window, yellow, [bird_x, bird_y, bird_wd, bird_wd])

    if x == 0:
        window.blit(text, (40, 300))

#    pygame.draw.rect(window, green, [pipe_x, pipe_y, pipe_wd, pipe_len])
#    pygame.draw.rect(window, green, [pipe2_x, pipe2_y, pipe_wd, pipe_lend])
#    pygame.draw.rect(window, green, [pipe3_x, pipe3_y, pipe_wd, pipe_len2])
#    pygame.draw.rect(window, green, [pipe4_x, pipe4_y, pipe_wd, pipe_lend1])
#    pygame.draw.rect(window, green, [pipe5_x, pipe5_y, pipe_wd, pipe_len3])
#    pygame.draw.rect(window, green, [pipe6_x, pipe6_y, pipe_wd, pipe_lend2])

# following code draws pipes countless times with random lengths

    if pipe_rx + pipe_wd == 0:
        pipe_rx = pipe_rx + 1200
        piped_rx = piped_rx + 1200
        pipe_len = random.randint(100, 450)
        piped_ry = pipe_len + 100
        piper_lend1 = window_len - pipe_ry
    pygame.draw.rect(window, green, [pipe_rx, pipe_ry, pipe_wd, pipe_len])
    pygame.draw.rect(window, green, [piped_rx, piped_ry, pipe_wd, piper_lend1])

    if pipe2_rx + pipe_wd == 0:
        pipe2_rx = pipe2_rx + 1200
        piped2_rx = piped2_rx + 1200
        pipe_len2 = random.randint(300, 450)
        piped2_ry = pipe_len2 + 100
        piper_lend2 = window_len - piped2_ry
    pygame.draw.rect(window, green, [pipe2_rx, pipe2_ry, pipe_wd, pipe_len2])
    pygame.draw.rect(window, green, [piped2_rx, piped2_ry, pipe_wd, piper_lend2])

    if pipe3_rx + pipe_wd == 0:
        pipe3_rx += 1200
        piped3_rx += 1200
        pipe_len3 = random.randint(100, 450)
        piped3_ry = pipe_len3 + 100
        piper_lend3 = window_len - piped3_ry
    pygame.draw.rect(window, green, [pipe3_rx, pipe3_ry, pipe_wd, pipe_len3])
    pygame.draw.rect(window, green, [piped3_rx, piped3_ry, pipe_wd, piper_lend3])

# blitting bird's image after drawing pipes to overlap
    if velocity_y > 0:
        window.blit(flappy_bird, (bird_x, bird_y))
    if velocity_y < 0:
        window.blit(flappy_bird2, (bird_x, bird_y))

# writing this function here so that it can blit upon the downside of pipes
    window.blit(grass, (grass_x, 600))

# collision mechanics

    if bird_x + bird_wd+12 > pipe_rx and bird_x < pipe_rx + pipe_wd:
        if bird_y < pipe_len:
            x = 2
    if bird_x + bird_wd+12 > pipe2_rx and bird_x < pipe2_rx + pipe_wd:
        if bird_y < pipe_len2:
            x = 2
    if bird_x + bird_wd+12 > pipe3_rx and bird_x < pipe3_rx + pipe_wd:
        if bird_y < pipe_len3:
            x = 2
    if bird_x + bird_wd+12 > pipe_rx and bird_x < pipe_rx + pipe_wd:
        if bird_y + bird_wd+20 > piped_ry:
            x = 2
    if bird_x + bird_wd+12 > pipe2_rx and bird_x < pipe2_rx + pipe_wd:
        if bird_y + bird_wd+20 > piped2_ry:
            x = 2
    if bird_x + bird_wd+12 > pipe3_rx and bird_x < pipe3_rx + pipe_wd:
        if bird_y + bird_wd+20 > piped3_ry:
            x = 2


# game over screen
    if high_score < score:
        high_score = score

    if bird_y + bird_wd+20 >= 590:
        x = 2

    if x == 2:
        window.blit(text3, (30, 180))
        text1 = font1.render("your score: " + str(score) + "         " + "high score: " + str(high_score) , True, white)
        window.blit(text1, (40, 250))
        window.blit(text4, (65, 330))

# score counter

    text1 = font3.render(str(score), True, white)

    if bird_x == pipe_rx:
        score += 1
    if bird_x == pipe2_rx:
        score += 1
    if bird_x == pipe3_rx:
        score += 1

    window.blit(text1, ((window_wd/2)-10, 50))

# constantly updating display with next frame

    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()