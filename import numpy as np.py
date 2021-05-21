import random
import pygame
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

screen = pg.display.set_mode([500, 500])
pygame.init()
font = pygame.font.SysFont("tahoma", 14, True)
running = True

centar_x = 250
centar_y = 250
centar = (centar_x, centar_y)
precnic = 100

pg.display.set_caption("Monte Karlo")
screen.fill((0, 0, 0))

def crtez():
    pg.draw.circle(screen, pg.Color("white"), centar, precnic)

crtez()

pg.display.update()
while pg.event.wait().type != pg.QUIT:
    pass
pg.quit()