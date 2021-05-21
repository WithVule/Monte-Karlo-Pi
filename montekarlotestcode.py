import math
import random
import sys

import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((500, 600))
pygame.init()
font = pygame.font.SysFont("tahoma", 14, True)


START_X = 20
START_Y = 20
EDGE = 460
RADIUS = EDGE//2
CENTER = (START_X + EDGE//2, START_Y + EDGE//2)
END_X = START_X + EDGE
END_Y = START_Y + EDGE


def clear_scr():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(START_X, START_Y, EDGE, EDGE), 2)
    pygame.draw.circle(screen, WHITE, CENTER, 4)
    pygame.draw.circle(screen, GREEN, CENTER, RADIUS, 2)


clear_scr()
pygame.display.update()

n = 0
k = 0


def update(num=1):
    global n, k

    for _ in range(num):
        n += 1

        x = random.uniform(START_X, END_X)
        y = random.uniform(START_Y, END_Y)

        cx, cy = CENTER

        color = RED
        dist_sq = (x-cx)**2 + (y-cy)**2
        if dist_sq <= RADIUS**2:
            k += 1
            color = BLUE

        pygame.draw.circle(screen, color, (int(x), int(y)), 3)

    calculated_pi = 4*k/n
    err = abs(math.pi - calculated_pi) / math.pi * 100

    n_text = font.render("All points: {:d}".format(n), True, WHITE)
    k_text = font.render("Points inside circle: {:d}".format(k), True, WHITE)
    pi_text = font.render("Pi approx. = {:f}".format(calculated_pi), True, WHITE)
    err_text = font.render("Error = {:.4f}%".format(err), True, WHITE)

    pygame.draw.rect(screen, BLACK, pygame.Rect(0, END_Y+5, 500, 100))
    ty = END_Y + 10
    screen.blit(k_text, (10, ty))
    ty += 20
    screen.blit(n_text, (10, ty))
    ty += 20
    screen.blit(pi_text, (10, ty))
    ty += 20
    screen.blit(err_text, (10, ty))

    pygame.display.update()


running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            update(1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            update(5)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            update(50)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            update(200)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
            update(1000)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            update(10000)


pygame.quit()
sys.exit()