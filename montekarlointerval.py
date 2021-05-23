import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
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
USER_INP = simpledialog.askstring(title="Unesite broj",
                                  prompt="Unesite koliko želite da prvo x bude: ")

A = int(USER_INP)
    
ROOT = tk.Tk()

ROOT.withdraw()
    
USER_INP2 = simpledialog.askstring(title="Unesite broj",
                                  prompt="Unesite koliko želite da drugo x bude: ")
    
B = int(USER_INP2)
    
ROOT = tk.Tk()

ROOT.withdraw()

USER_INP3 = simpledialog.askstring(title="Unesite broj",
                                  prompt="Unesite koliko želite da maksimalno f(x) bude: ")
    
T = int(USER_INP3)

random_f = random.uniform(0, T)
random_x = random.uniform(A, B)


def f(x):
    x**2
    return x

plt.plot(x, f(x))
plt.axhline(color = "white")
plt.fill_between(x, f(x), where=[(x > 0) and (x < 2) for x in x])
plt.show()


pg.display.update()
while pg.event.wait().type != pg.QUIT:
    running = False
pg.quit()