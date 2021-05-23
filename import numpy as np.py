import random
import math as m
import pygame as pg
import sys
import datetime
import tkinter as tk
from tkinter import simpledialog

from pygame.time import delay

ROOT = tk.Tk()

ROOT.withdraw()
# Ovo dialog popbox-a
USER_INP = simpledialog.askstring(title="Unesite broj",
                                  prompt="Unesite koliko puta želite da se igla baci: ")

# Ovo je input korisnika
interval = int(USER_INP)

print("Korisnik je uneo ", USER_INP)

pg.init()
pg.font.init()
txtfont = pg.font.SysFont('digital-7', 25)
screen = pg.display.set_mode([1000, 1000])
font = pg.font.SysFont("tahoma", 14, True)
running = True

centar_x = 500
centar_y = 500
centar = (centar_x, centar_y)
polup = 500
pogodak = 0
pokusaj = 0

pg.display.set_caption("Monte Karlo veravatnoća igle")
screen.fill((0, 0, 0))

pg.draw.circle(screen, pg.Color("white"), centar, polup)
pg.draw.circle(screen, pg.Color("black"), centar, (polup-2))

for interval in range(1, interval + 1):
    
    random_x = random.uniform(0, 1000)
    random_y = random.uniform(0, 1000)

    poz_x = abs(random_x - 500)
    poz_y = abs(random_y - 500)

    diagonala = m.sqrt(poz_x * poz_x + poz_y * poz_y)
    if diagonala <= polup:
        pg.draw.circle(screen, pg.Color("green"), (random_x, random_y), 2)
        pogodak += 1
        pokusaj += 1
    
    else:
        pg.draw.circle(screen, pg.Color("red"), (random_x, random_y), 2)
        pokusaj += 1
    
    pi = 4*pogodak/interval

    text = txtfont.render("Verovatnoća je " + str(pi), False, (255, 255, 255))
    screen.blit(text,(0, 0))
    
    text = txtfont.render(str(pokusaj) + "/" + str(int(USER_INP)), False, (255, 255, 255))
    screen.blit(text,(0, 20))

    pg.display.update()
    pg.time.delay(5)

    text = txtfont.render("Verovatnoća je " + str(pi), False, (0, 0, 0))
    screen.blit(text,(0, 0))
    text = txtfont.render(str(pokusaj) + "/" + str(int(USER_INP)), False, (0, 0, 0))
    screen.blit(text,(0, 20))


text = txtfont.render("Verovatnoća je " + str(pi), False, (255, 255, 255))
screen.blit(text,(0, 0))
text = txtfont.render(str(pokusaj) + "/" + str(interval), False, (255, 255, 255))
screen.blit(text,(0, 20))


pg.display.update()
while pg.event.wait().type != pg.QUIT:
    running = False
pg.quit()