import random
import math as m
import pygame as pg
import sys
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# Ovo dialog popbox-a
USER_INP = simpledialog.askstring(title="Unesite broj",
                                  prompt="Unesite koliko puta želite da se igla baci: ")

# Ovo je input korisnika
interval = int(USER_INP)

print("Korisnik je uneo ", USER_INP)

pg.init()
screen = pg.display.set_mode([500, 500])
font = pg.font.SysFont("tahoma", 14, True)
running = True

centar_x = 250
centar_y = 250
centar = (centar_x, centar_y)
polup = 250
pogodak = 0

pg.display.set_caption("Monte Karlo veravatnoća igle")
screen.fill((0, 0, 0))

def crtez():
    pg.draw.circle(screen, pg.Color("white"), centar, polup)
    pg.draw.circle(screen, pg.Color("black"), centar, (polup-2))

crtez()

for interval in range(1, interval):
    random_x = random.uniform(0, 500)
    random_y = random.uniform(0, 500)

    poz_x = abs(random_x - 250)
    poz_y = abs(random_y - 250)

    diagonala = m.sqrt(poz_x * poz_x + poz_y * poz_y)
    #print("Prečnik tačke je", diagonala)
    if diagonala <= polup:
        pg.draw.circle(screen, pg.Color("green"), (random_x, random_y), 2)
        pogodak += 1
    
    if diagonala >= polup:
        pg.draw.circle(screen, pg.Color("red"), (random_x, random_y), 2)

def pi():
    pi = 4*pogodak/interval
    print(pi)

pi()
    
pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()