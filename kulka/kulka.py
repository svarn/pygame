import sys
import os
import pygame
import random
import math
from pygame.locals import *

pygame.init()


"""" eventy """
def event(events):
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
#        else:
#            print(event)


# losowy cel kulki
def los():
    global los_wsp
    a = [random.randint(0, 500), 0]
    b = [500, random.randint(0, 500)]
    c = [random.randint(0, 500), 500]
    d = [0, random.randint(0, 500)]
    z = random.randint(1, 4)
    if z == 1:
        los_wsp = a
    elif z == 2:
        los_wsp = b
    elif z == 3:
        los_wsp = c
    elif z == 4:
        los_wsp = d
    print("cel kulki: " + str(los_wsp))
    return los_wsp


# zegar
FPS = 120
fps_clock = pygame.time.Clock()

# kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (255, 0, 0)
zielony = (0, 255, 0)
niebieski = (0, 0, 255)


# wspolrzedne ekranu
W = 500
H = 500
pol_W = W / 2
pol_H = H / 2

# ekran
EKRAN = pygame.display.set_mode((W, H))
pygame.display.set_caption("kulka")

# region zmienne
j = 0
kulka_x = pol_W
kulka_y = pol_H
doc_x = kulka_x
doc_y = kulka_y
kier_x = 0
kier_y = 0
r_x = 0
r_y = 0
szybkosc = 2
# endregion

while True:
    event(pygame.event.get())

    if j == 0:
        r = los()
        r_x = r[0]
        r_y = r[1]
        j += 1

    if j == 1:
        radiany = math.atan2(r_y - doc_y, r_x - doc_x)
        kier_x = math.cos(radiany) * szybkosc
        kier_y = math.sin(radiany) * szybkosc
        j += 1

    if j == 2:
        kulka_x += kier_x
        kulka_y += kier_y
        if kulka_x < 10:
            j = 3
        elif kulka_x > 490:
            j = 3
        elif kulka_y < 10:
            j = 4
        elif kulka_y > 490:
            j = 4

    if j == 3:
        kulka_x -= kier_x
        kulka_y += kier_y
        if kulka_x < 10:
            j = 2
        elif kulka_x > 490:
            j = 2
        elif kulka_y < 10:
            j = 5
        elif kulka_y > 490:
            j = 5

    if j == 4:
        kulka_x += kier_x
        kulka_y -= kier_y
        if kulka_x < 10:
            j = 5
        elif kulka_x > 490:
            j = 5
        elif kulka_y < 10:
            j = 2
        elif kulka_y > 490:
            j = 2

    if j == 5:
        kulka_x -= kier_x
        kulka_y -= kier_y
        if kulka_x < 10:
            j = 4
        elif kulka_x > 490:
            j = 4
        elif kulka_y < 10:
            j = 3
        elif kulka_y > 490:
            j = 3

    print(kulka_x, kulka_y)
    pygame.draw.circle(EKRAN, bialy, (int(kulka_x), int(kulka_y)), 10, 0)
    pygame.display.update()
    fps_clock.tick(FPS)
    EKRAN.fill(czarny)
